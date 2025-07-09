using System.Collections.Generic;
using UnityEngine;
using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using Newtonsoft.Json.Linq;
using System.Linq;
using System.Data;
using PimDeWitte.UnityMainThreadDispatcher;

public class SocketReadThreading : MonoBehaviour
{
    // The port used for receiving data
    public int listenPort = -1;
    // Flag that signifies if the port has been defined
    public bool portNumberSetFlag = false;
    // The number of actors expected to be streamed from the studio
    public int numberOfCharactersToStream = 1;
    public string IP;
    // Flag that signifies if the receiving process is running
    private bool isRunning = true;
    // UDP listener for receiving animation data
    UdpClient updListener;
    // Ip endpoint for receiving animation data
    IPEndPoint groupEP;
    // Chunks of the initialization data for one actor
    Dictionary<string, List<string>> initChunks = new Dictionary<string, List<string>>();
    // Ids of chunks of the initialization data
    Dictionary<string, List<int>> initChunksIds = new Dictionary<string, List<int>>();
    // Sorted version of the ids of the chunks
    List<int> initChunksIdsSorted = new List<int>();
    // Number of packets/chunks that the initialization data of each actor consists of
    Dictionary<string, int> packets = new Dictionary<string, int>();
    // The initialization data of each actor
    public Dictionary<string, InitializationData> initializationDataForSubject = new Dictionary<string, InitializationData>();
    // Flags that signify if the initialization data of each actor have been successfully received
    public Dictionary<string, bool> initializationDataReadyForSubject = new Dictionary<string, bool>();
    // The skeleton data for each actor
    public Dictionary<string, List<JointData>> skeletonDataForSubject = new Dictionary<string, List<JointData>>();
    // Flags that signify if the skeleton data of each actor have been successfully received
    public Dictionary<string, bool> skeletonDataReadyForSubject = new Dictionary<string, bool>();
    // The animation data for each actor
    public Dictionary<string, List<Quaternion>> animationDataForSubject = new Dictionary<string, List<Quaternion>>();
    // The global translation for each actor
    public Dictionary<string, Vector3> globalTranslationForSubject = new Dictionary<string, Vector3>();
    // The actors' names
    public HashSet<string> subjectNames = new HashSet<string>();
    // Inside the actor Initialization message the joints are in this order.
    public static string[] jointOrderInitializationInStream = new string[] {
        "moverserig_Pelvis",
        "moverserig_LeftHip", "moverserig_RightHip", "moverserig_Spine1",
        "moverserig_LeftKnee", "moverserig_RightKnee", "moverserig_Spine2",
        "moverserig_LeftAnkle", "moverserig_RightAnkle", "moverserig_Spine3",
        "moverserig_LeftFoot", "moverserig_RightFoot", "moverserig_Neck",
        "moverserig_LeftCollar", "moverserig_RightCollar", "moverserig_Head",
        "moverserig_LeftShoulder", "moverserig_RightShoulder",
        "moverserig_LeftElbow", "moverserig_RightElbow",
        "moverserig_LeftWrist", "moverserig_RightWrist",
        "moverserig_LeftHand", "moverserig_RightHand"};
    // But inside the Character Subject and Character Animation messages they have the order of this array.
    public static string[] jointOrderInSkeletonAnimationStream = new string[] {
        "moverserig_Pivot", "moverserig_Pelvis",
        "moverserig_LeftHip", "moverserig_LeftKnee", "moverserig_LeftAnkle", "moverserig_LeftFoot",
        "moverserig_RightHip", "moverserig_RightKnee", "moverserig_RightAnkle", "moverserig_RightFoot",
        "moverserig_Spine1", "moverserig_Spine2", "moverserig_Spine3",
        "moverserig_LeftCollar", "moverserig_LeftShoulder", "moverserig_LeftElbow", "moverserig_LeftWrist", "moverserig_LeftHand",
        "moverserig_Neck", "moverserig_Head",
        "moverserig_RightCollar", "moverserig_RightShoulder", "moverserig_RightElbow", "moverserig_RightWrist", "moverserig_RightHand"};
    // Conversions between the two previous arrays
    public static int[] initializationIdsToSkeletonIds;
    // Last valid Pelvis rotation received from the stream
    Quaternion lastValidPelvisRotationQuaternion;
    // Thread used for receiving the initialization data through a TCP socket
    Thread tcpReceivingThread;
    // Thread used for continuously receiving the animation data a UDP socket
    Thread udpReceivingThread;
    // Byte array used for reading data from the TCP Receive Buffer
    byte[] bytes = new byte[65635];
    // TCP listener for receiving initialization data
    TcpListener tcpListener = null;
    // One actor's name. Used inside the TCP process
    string actorName;
    // One actor's received chunk number. Used inside the TCP process 
    int chunksNum;

    /// <summary>
    /// The initialization data of an actor
    /// </summary>
    public struct InitializationData
    {
        public Vector3[] verticesCoords;
        public Dictionary<string, Vector3> jointPositions; // joint name and position
        public int[] faces;
        public Dictionary<int, Utils.VertexSkinningWeights> skinningInfo; // vertex id and corresponding skinning info
    }

    /// <summary>
    /// The data that describe one body joint
    /// </summary>
    public struct JointData
    {
        public string Name;
        public int ParentId;
        public int Id;
    }

    // TODO Not used. Remove
    /// <summary>
    /// The animation data of an joint
    /// </summary>
    public struct AnimationData
    {
        public Vector3 Location;
        public Vector3 Rotation;
        public Vector3 Scale;
    }

    // Start is called before the first frame update
    async void Start()
    {
        // Wait for the port number of the socket to be defined by the user
        await WaitForSocketNumberAsync();

        initializationIdsToSkeletonIds = Enumerable.Range(0, jointOrderInitializationInStream.Length).Select(i => Array.FindIndex(jointOrderInSkeletonAnimationStream, j => j == jointOrderInitializationInStream[i])).ToArray();

        // Initialize the TCP Listener for receiving the initialization data 
        //IPAddress localAddr = IPAddress.Parse("0.0.0.0");
        IPAddress localAddr = IPAddress.Parse(this.IP);
        tcpListener = new TcpListener(localAddr, listenPort);
        tcpListener.Server.SetSocketOption(SocketOptionLevel.Tcp, SocketOptionName.ReuseAddress, true);
        tcpListener.Server.ReceiveBufferSize = 65535;
        tcpListener.Start();

        // Start a thread to receive initialization data of the actors through a TCP socket
        tcpReceivingThread = new Thread(() => ReceiveInitData());
        tcpReceivingThread.IsBackground = true;
        tcpReceivingThread.Start();

        // Wait until the initialization data for all actors have been received thorough the TCP socket
        await WaitForInitializationCompleteAsync();
        tcpReceivingThread.Join();

        // Initialize the UDP Listener for continuous receiving of the skeleton and animation data
        groupEP = new IPEndPoint(IPAddress.Any, listenPort);
        updListener = new UdpClient(listenPort);
        updListener.Client.ReceiveBufferSize = 65635;

        // Start a thread to receive skeleton and animation data through a UDP socket
        udpReceivingThread = new Thread(ReceiveUdpData);
        udpReceivingThread.IsBackground = true;
        udpReceivingThread.Start();
    }

    void OnApplicationQuit()
    {
        isRunning = false;
        tcpListener.Stop();
        updListener.Close();
        udpReceivingThread.Join();
    }

    /// <summary>
    /// This method is used for receiving the initialization data of all the actors, through a TCP socket. It runs on a separate thread.
    /// </summary>
    void ReceiveInitData()
    {
        Debug.Log($"Started receiving TCP initialization data on thread {Thread.CurrentThread.ManagedThreadId}");

        // While there are still actors whose data have not been completely received
        while (initializationDataReadyForSubject.Keys.Count != numberOfCharactersToStream ||
              (initializationDataReadyForSubject.Keys.Count == numberOfCharactersToStream &&
               !initializationDataReadyForSubject.All(element => element.Value)))
        {
            actorName = "";
            chunksNum = 0;
            int b;
            byte[] response;

            // Initialize the TCP socket
            Debug.Log("Waiting for TCP connection...");
            Socket sock = tcpListener.AcceptSocket();
            // sock.ReceiveTimeout = 100;
            Debug.Log("TCP Connected");

            // Keep getting chunks until all are received
            do
            {
                StringBuilder completeMessage = new StringBuilder();

                // Keep reading from the TCP socket until I have received the whole chunk
                do
                {
                    try
                    {
                        // Receive data from TCP socket
                        b = sock.Receive(bytes);
                        Debug.Log($"RECEIVED TCP DATA: {b} bytes");

                        // Add bytes to the chunk message
                        completeMessage.Append(Encoding.ASCII.GetString(bytes, 0, b));
                    }
                    catch (SocketException ex)
                    {
                        Debug.Log($"TCP Socket error: {ex.Message}, code: {ex.ErrorCode}, {ex.NativeErrorCode}, {ex.SocketErrorCode}");

                        // If receiving data failed, ask the server to send the current chunk again
                        // response = System.Text.Encoding.ASCII.GetBytes("r");
                        // sock.Send(response);

                        completeMessage = new StringBuilder();
                        continue;
                    }
                    catch (Exception ex)
                    {
                        Debug.Log($"TCP Unexpected error: {ex.Message}");
                        completeMessage = new StringBuilder();
                        return;
                    }
                    // ! the detection of the end of the message should be done in a more robust way and not just detecting "}]}"
                } while ((completeMessage.ToString().Length > 0) && !(completeMessage.ToString().Substring((int)MathF.Max(completeMessage.ToString().Length - 3, 0)) == "}]}"));

                try
                {
                    // Process the received message
                    Processing(completeMessage.ToString());

                    // Ask from the server to send the next chunk
                    response = System.Text.Encoding.ASCII.GetBytes("a");
                    sock.Send(response);
                }
                catch (Exception ex)
                {
                    Debug.Log($"Exception {ex.Message}");

                    // If processing the chunk failed, ask the server to send the current chunk again
                    // response = System.Text.Encoding.ASCII.GetBytes("r");
                    // sock.Send(response);

                    completeMessage = new StringBuilder();
                    continue;
                }

                Debug.Log($"actorName: {actorName}, chunks Number: {chunksNum}, packets: {packets[actorName]}");

            } while (actorName == "" || chunksNum < packets[actorName]);

            sock.Close();
        }
    }

    /// <summary>
    /// This method is used for receiving the animation data of all the actors, through a UDP socket. It runs on a separate thread.
    /// </summary>
    void ReceiveUdpData()
    {
        isRunning = true;

        Debug.Log($"Started receiving UDP data on thread {Thread.CurrentThread.ManagedThreadId}");

        while (isRunning)
        {
            try
            {
                // Receive data from UDP socket
                byte[] bytes = updListener.Receive(ref groupEP);

                // Preprocess/decode the message on the main thread
                string message = Encoding.ASCII.GetString(bytes, 0, bytes.Length);
                ProcessOnMainThread(message);
            }
            catch (SocketException ex)
            {
                Debug.Log($"UDP Socket error: {ex.Message}");
                isRunning = false;
            }
            catch (Exception ex)
            {
                Debug.Log($"UDP Unexpected error: {ex.Message}");
                isRunning = false;
            }
        }
    }

    /// <summary>
    /// Send the message to the main Unity thread for processing
    /// </summary>
    /// <param name="message">The message to process</param>
    void ProcessOnMainThread(string message)
    {
        UnityMainThreadDispatcher.Instance().Enqueue(() => Processing(message));
    }

    /// <summary>
    /// This method is used to process a received string message
    /// </summary>
    /// <param name="message"></param>
    async void Processing(string message)
    {
        // Debug.Log(message);

        // Convert the string message to a Json object
        JObject msg = JObject.Parse(message);

        // property.Name is the name of the actor
        JProperty property = msg.Properties().First();
        actorName = property.Name;
        // Debug.Log(property.Name);

        // For the first time of receiving data of this actor
        if (!packets.ContainsKey(property.Name))
        {
            subjectNames.Add(property.Name);
            packets[property.Name] = -1;
            initChunks[property.Name] = new List<string>();
            initChunksIds[property.Name] = new List<int>();
        }

        // Get the type of data that the message contains. CharacterInitialization or CharacterAnimation or CharacterSubject
        string frameType = msg[property.Name][0]["Type"].ToString();
        // Debug.Log(frameType);

        if (frameType == "CharacterInitialization")
        {
            // Get the number of initialization data packets to expect
            packets[property.Name] = msg[property.Name][0]["Packets"].ToObject<int>();

            // Add the data packet and index to the list of received packets and ids
            initChunks[property.Name].Add(msg[property.Name][0]["Chunk"].ToString());
            initChunksIds[property.Name].Add(msg[property.Name][0]["Index"].ToObject<int>());

            Debug.Log($"Current Packet ID {msg[property.Name][0]["Index"].ToObject<int>()}, {initChunks[property.Name].Count} of {packets[property.Name]}");
        }

        else if (frameType == "CharacterAnimation")
        {
            ProcessAnimationDataAsync(msg[property.Name], property.Name);
        }

        else if (frameType == "CharacterSubject")
        {
            // Debug.Log($"Received Character Subject (Skeleton) data");
            ProcessSkeletonInitializationDataAsync(msg[property.Name], property.Name);

        }

        chunksNum = initChunks[property.Name].Count;

        // If we received all the expected initialization data packets
        if (initChunks.ContainsKey(property.Name) && (initChunks[property.Name].Count == packets[property.Name]))
        {
            Debug.Log($"Received all initialization chunks of {property.Name}, processing data.");

            initChunksIdsSorted.AddRange(initChunksIds[property.Name]);
            initChunksIdsSorted.Sort();

            // Check packets received order
            if (!initChunksIdsSorted.SequenceEqual(initChunksIds[property.Name]))
            {
                Debug.Log("Chunks did not arrive in correct sequence");
                // print(string.Join(" ", initChunksIds[property.Name]));
                // print(string.Join(" ", initChunksIds[property.Name]));
            }
            else
            {
                string data = string.Join("", initChunks[property.Name]);
                ProcessCharacterInitializationDataAsync(data, property.Name);
            }

            initChunks[property.Name].Clear();
            initChunksIds[property.Name].Clear();
            initChunksIdsSorted.Clear();
        }
    }

    /// <summary>
    /// This method is used for processing the initialization data of an actor
    /// </summary>
    /// <param name="data">Initialization data in a string</param>
    /// <param name="subjectName">The actor's name</param>
    /// <returns></returns>
    public async Task ProcessCharacterInitializationDataAsync(string data, string subjectName)
    {
        // Debug.Log(data);
        JObject dataJObject = JObject.Parse(data);
        // Debug.Log(string.Join(",", dataJObject.Properties().Select(p => p.Name).ToList()));

        InitializationData initData = new InitializationData();

        // The index of the actor that is being processed
        int subjectId = subjectNames.ToList().IndexOf(subjectName);

        // For each category of initialization data. Could be vertices or template_joints or faces or skinning_weights.
        foreach (string p in dataJObject.Properties().Select(p => p.Name).ToList())
        {
            // Debug.Log(p);

            // Get the rows and columns that the data should be formatted to
            int rows = int.Parse(dataJObject[p]["shape"].ToString().Split('x')[0]);
            int cols = int.Parse(dataJObject[p]["shape"].ToString().Split('x')[1]);

            if (p == "vertices")
            {
                // Get the vertices positions and save them to the initialization data 
                Vector3[] allVerticesCoords = Utils.ConvertToVector3Array(dataJObject[p]["data"].Select(t => t.ToObject<float>()).ToArray());

                Vector3[] verticesCoords = new Vector3[6890];
                Array.Copy(allVerticesCoords, subjectId * verticesCoords.Length, verticesCoords, 0, verticesCoords.Length);

                initData.verticesCoords = verticesCoords;
                Debug.Log($"Initialized vertices for {subjectName}");
            }
            else if (p == "template_joints")
            {
                // Get the joint positions at T-pose and save them to the initialization data
                Vector3[] allJointPositions = Utils.ConvertToVector3Array(dataJObject[p]["data"].Select(t => t.ToObject<float>()).ToArray());

                Vector3[] jointPositions = new Vector3[jointOrderInitializationInStream.Length];
                Array.Copy(allJointPositions, subjectId * jointPositions.Length, jointPositions, 0, jointPositions.Length);

                initData.jointPositions = new Dictionary<string, Vector3>();
                for (int i = 0; i < jointPositions.Length; i++)
                {
                    // initData.jointPositions[jointOrderInitializationInStream[i]] = jointPositions[i];
                    initData.jointPositions[jointOrderInitializationInStream[i]] = new Vector3(-1 * jointPositions[i].x, jointPositions[i].y, jointPositions[i].z);
                }
                Debug.Log($"Initialized joints for {subjectName}");
            }
            else if (p == "faces")
            {
                // Get the triangle faces and save them to the initialization data
                initData.faces = dataJObject[p]["data"].Select(t => t.ToObject<int>()).ToArray();
                Debug.Log($"Initialized faces for {subjectName}");
            }
            else if (p == "skinning_weights")
            {
                // Get the skinning weights and convert the to a 2D Matrix
                Dictionary<int, Utils.VertexSkinningWeights> skinningInfo = new Dictionary<int, Utils.VertexSkinningWeights>();
                float[,] dataArray = Utils.ConvertTo2DArray(dataJObject[p]["data"].Select(t => t.ToObject<float>()).ToArray(), cols, rows);

                for (int vid = 0; vid < dataArray.GetLength(0); vid++)
                {
                    float[] weightsOfVertex = new float[dataArray.GetLength(1)];

                    for (int bid = 0; bid < dataArray.GetLength(1); bid++)
                    {
                        weightsOfVertex[bid] = dataArray[vid, bid];
                    }
                    // Debug.Log($" weights before sorting {string.Join(",", weightsOfVertex)}");
                    // Here initially the ids of the joints correspond to the id in the "jointOrderInitializationInStream" array, i.e. in the order they arrive inside the character initialization message, so we give them the proper ids.
                    int[] jointIds = Enumerable.Range(0, dataArray.GetLength(1)).Select(x => initializationIdsToSkeletonIds[x]).ToArray();
                    // Debug.Log($" joints before sorting {string.Join(",", jointIds)}");

                    // Ascending sort
                    Array.Sort(weightsOfVertex, jointIds);
                    // Debug.Log($" weights after sorting {string.Join(",", weightsOfVertex)}");
                    // Debug.Log($" joints after sorting {string.Join(",", jointIds)}");

                    // Reverse them to get descending order
                    Array.Reverse(weightsOfVertex);
                    Array.Reverse(jointIds);
                    // Debug.Log($" weights after reversing {string.Join(",", weightsOfVertex)}");
                    // Debug.Log($" joints after reversing {string.Join(",", jointIds)}");

                    // For each vertex keep only the 4 vertices with the greatest weight
                    skinningInfo[vid] = new Utils.VertexSkinningWeights { bonesIds = new int[] { jointIds[0], jointIds[1], jointIds[2], jointIds[3] }, weights = new float[] { weightsOfVertex[0], weightsOfVertex[1], weightsOfVertex[2], weightsOfVertex[3] } };

                    // Debug.Log(string.Join(", ", weightsOfVertex));
                    // Debug.Log(string.Join(", ", jointIds));
                }
                initData.skinningInfo = skinningInfo;
                Debug.Log($"Initialized skinning weights for {subjectName}");
            }
        }

        // Save the initialization data of the actor
        initializationDataForSubject[subjectName] = initData;
        initializationDataReadyForSubject[subjectName] = true;

    }

    /// <summary>
    /// This method is used to process the Skeleton Data of an actor
    /// </summary>
    /// <param name="data">The data</param>
    /// <param name="subjectName">The actor's name</param>
    /// <returns></returns>
    public async Task ProcessSkeletonInitializationDataAsync(JToken data, string subjectName)
    {
        if (skeletonDataReadyForSubject.ContainsKey(subjectName) && skeletonDataReadyForSubject[subjectName])
        {
            return;
        }

        // Debug.Log(data);

        List<JointData> joints = new List<JointData>();
        var elements = data.Children().ToList();
        // Skip first because it just contains the frame type
        for (int i = 1; i < elements.Count(); i++)
        {
            joints.Add(new JointData { Name = elements[i]["Name"].ToString(), Id = i - 1, ParentId = elements[i]["Parent"].ToObject<int>() });
        }

        skeletonDataForSubject[subjectName] = joints;
        skeletonDataReadyForSubject[subjectName] = true;

        Debug.Log($"Initialized skelton data for {subjectName}");
    }

    /// <summary>
    /// This method is used to process the Animation Data of an actor
    /// </summary>
    /// <param name="data">The data</param>
    /// <param name="subjectName">the actor's name</param>
    /// <returns></returns>
    public async Task ProcessAnimationDataAsync(JToken data, string subjectName)
    {
        // Debug.Log(data);

        List<Quaternion> animationParameters = new List<Quaternion>();
        var elements = data.Children().ToList();
        // Debug.Log(elements.Count);
        // Debug.Log(data.ToString());

        // Skip first because it just contains the frame type
        // Read the animation parameters for each joint
        for (int i = 1; i < elements.Count; i++)
        {
            if (i == 1) // Root
            {
                // x_quat_unity = -x_quat_unreal, y_quat_unity = -y_quat_unreal, z_quat_unity = z_quat_unreal, w_quat_unity = w_quat_unreal
                animationParameters.Add(new Quaternion(-1 * elements[i]["Rotation"][0].ToObject<float>(), -1 * elements[i]["Rotation"][1].ToObject<float>(), elements[i]["Rotation"][2].ToObject<float>(), elements[i]["Rotation"][3].ToObject<float>()));

                // Correct standing up direction
                animationParameters[i - 1] *= Quaternion.Euler(new Vector3(-90, 0, 0));
            }
            else if (i == 2) // Pelvis
            {
                // x_unity = x_unreal, y_unity = z_unreal, z_unity = -y_unreal, scaled by 0.01 to convert to meters and scaled by (-1, 1, -1)
                globalTranslationForSubject[subjectName] = new Vector3(-1 * elements[i]["Location"][0].ToObject<float>(), elements[i]["Location"][2].ToObject<float>(), elements[i]["Location"][1].ToObject<float>()) * 0.01f;
                // Debug.Log($"Pelvis location {elements[i]["Location"][0].ToObject<float>()}, {elements[i]["Location"][1].ToObject<float>()}, {elements[i]["Location"][2].ToObject<float>()}");

                if (((JArray)elements[i]["Rotation"]).All(token => token.Type != JTokenType.Null))
                {
                    // If the pelvis rotation that was received was valid save it as the last valid 
                    // x_quat_unity = -x_quat_unreal, y_quat_unity = -y_quat_unreal, z_quat_unity = z_quat_unreal, w_quat_unity = w_quat_unreal
                    lastValidPelvisRotationQuaternion = new Quaternion(-1 * elements[i]["Rotation"][0].ToObject<float>(), -1 * elements[i]["Rotation"][1].ToObject<float>(), elements[i]["Rotation"][2].ToObject<float>(), elements[i]["Rotation"][3].ToObject<float>());
                }
                else
                {
                    Debug.Log("Pelvis rotation is NULL");
                }

                animationParameters.Add(lastValidPelvisRotationQuaternion);

                // Debug.Log($"Pelvis rotation quaternion {elements[i]["Rotation"][0].ToObject<float>()}, {elements[i]["Rotation"][1].ToObject<float>()}, {elements[i]["Rotation"][2].ToObject<float>()}, {elements[i]["Rotation"][3].ToObject<float>()}");
                // Vector3 rotVec = (new Quaternion(-1*elements[i]["Rotation"][0].ToObject<float>(), -1*elements[i]["Rotation"][1].ToObject<float>(), elements[i]["Rotation"][2].ToObject<float>(), elements[i]["Rotation"][3].ToObject<float>())).eulerAngles;
                // Debug.Log($"Pelvis rotation vector3 {rotVec.x}, {rotVec.y}, {rotVec.z}");
            }
            else
            {
                // x_quat_unity = -x_quat_unreal, y_unity = -y_quat_unreal, z_unity = z_quat_unreal
                animationParameters.Add(new Quaternion(-1 * elements[i]["Rotation"][0].ToObject<float>(), -1 * elements[i]["Rotation"][1].ToObject<float>(), elements[i]["Rotation"][2].ToObject<float>(), elements[i]["Rotation"][3].ToObject<float>()));
            }
        }

        animationDataForSubject[subjectName] = animationParameters;
    }

    /// <summary>
    /// This method is used to wait for the port number to be set by the user
    /// </summary>
    /// <returns></returns>
    private async Task WaitForSocketNumberAsync()
    {
        Debug.Log("Waiting for socket number to be set");
        while (listenPort == -1)
        {
            await Task.Delay(500); // Poll every 500ms asynchronously
        }
        Debug.Log($"Socket number set to {listenPort}");
    }

    /// <summary>
    /// This method is used to wait for the initialization data to be received for all actors
    /// </summary>
    /// <returns></returns>
    private async Task WaitForInitializationCompleteAsync()
    {
        Debug.Log("Waiting for initialization data to be completed (TCP socket)");
        while (initializationDataReadyForSubject.Keys.Count != numberOfCharactersToStream || (initializationDataReadyForSubject.Keys.Count == numberOfCharactersToStream && !initializationDataReadyForSubject.All(element => element.Value)))
        {
            await Task.Delay(500); // Poll every 500ms asynchronously
        }

        Debug.Log("Initialization data received (TCP socket)");
    }

    public void RestartInitialization()
    {
        Debug.Log("Resetting Initialization");
        initChunks = new Dictionary<string, List<string>>();
        chunksNum = 0;
        initChunksIds = new Dictionary<string, List<int>>();
        initChunksIdsSorted = new List<int>();
        packets = new Dictionary<string, int>();
        subjectNames = new HashSet<string>();
    }
}
