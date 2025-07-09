using System.Collections.Generic;
using UnityEngine;
using Unity.Collections;
using System;
using System.Linq;
using System.IO;
using System.IO.Compression;

public class Utils : MonoBehaviour
{

    public struct VertexSkinningWeights {
        public int[] bonesIds;
        public float[] weights;
    }

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public static void SetModelToTPose(Transform root) {

        // root.localRotation = Quaternion.identity;

        foreach(Transform child in root) {
            child.localRotation = Quaternion.identity;

            SetModelToTPose(child);
        }
    }

    // Return a Dictionary with keys the id of a vertex and values the bones that this vertex is influenced from and the influence weights.
    public static Dictionary<int, VertexSkinningWeights> GetVertexSkinningInfo(NativeArray<BoneWeight1> cloneBoneWeights, NativeArray<byte> cloneBonesPerVertex) {

        Dictionary<int, VertexSkinningWeights> ret = new Dictionary<int, VertexSkinningWeights>();

        var boneWeightIndex = 0;

        // Iterate over the vertices
        for (var vertIndex = 0; vertIndex < cloneBonesPerVertex.Length; vertIndex++)
        {
            var totalWeight = 0f;
            var numberOfBonesForThisVertex = cloneBonesPerVertex[vertIndex];
            ret.Add(vertIndex, new VertexSkinningWeights{bonesIds=new int[numberOfBonesForThisVertex], weights=new float[numberOfBonesForThisVertex]});
            // Debug.Log("This vertex has " + numberOfBonesForThisVertex + " bone influences");

            // For each vertex, iterate over its BoneWeights
            for (var i = 0; i < numberOfBonesForThisVertex; i++)
            {   
                var currentBoneWeight = cloneBoneWeights[boneWeightIndex];

                ret[vertIndex].bonesIds[i] = currentBoneWeight.boneIndex;
                ret[vertIndex].weights[i] = currentBoneWeight.weight;

                
                totalWeight += currentBoneWeight.weight;
                if (i > 0)
                {
                    Debug.Assert(cloneBoneWeights[boneWeightIndex - 1].weight >= currentBoneWeight.weight);
                }
                boneWeightIndex++;
            }
            Debug.Assert(Mathf.Approximately(1f, totalWeight));
        }

        return ret;
    }

    public static GameObject BuildSkeletonWithHierarchy(Transform source, Transform parent, Dictionary<string, Vector3> newPositions) {
        GameObject node = new GameObject();

        if (parent is not null) {
            node.transform.parent = parent;
        }
        node.transform.localRotation = Quaternion.identity;
        
        // if (parent is null) {
        //     node.transform.position = Vector3.zero;
        //     node.transform.localPosition = Vector3.zero;
        // }
        // else {
        //     node.transform.localPosition = newPositions[source.name];
        // }
        node.transform.position = newPositions[source.name];

        node.name = source.name;
        Debug.Log($"{node.name} -> {node.transform.localPosition} / {newPositions[source.name]}");

        foreach (Transform sourceChild in source) {
            GameObject child = BuildSkeletonWithHierarchy(sourceChild, node.transform, newPositions);
        }

        return node;
    }

    public static GameObject BuildSkeletonWithHierarchy(List<SocketReadThreading.JointData> skeletonData, Dictionary<string, Vector3> jointPositions) {

        // This list will hold the already created joint game objects
        List<GameObject> createdJoints = new List<GameObject>();

        // For each joint received from the studio
        foreach (SocketReadThreading.JointData joint in skeletonData) {

            // Create a new game object and it the name of the joint
            GameObject node = new GameObject();
            node.name = joint.Name;

            // If the joint is not the "root" joint
            if (joint.ParentId != -1) {
                // Find inside the already created joints the node that has the same name as the parent if the current joint and assign it as its parent
                node.transform.parent = createdJoints.Find(n => n.name == SocketReadThreading.jointOrderInSkeletonAnimationStream[joint.ParentId]).transform;
            }

            // Set local rotation to zero
            node.transform.localRotation = Quaternion.identity;
            
            // Set the position
            node.transform.position = jointPositions[joint.Name];

            Debug.Log($"{node.name} -> localPos:{node.transform.localPosition} / Received/GlobalPos:{jointPositions[joint.Name]}");

            createdJoints.Add(node);
        }
        // Return the root joint
        return createdJoints.Find(n => n.name == SocketReadThreading.jointOrderInSkeletonAnimationStream[0]);
    }

    public static void AnimateSkeletonWithHierarchy(Transform node, Dictionary<int, Vector3> animation, Transform[] skeletonBones) {

        // Get the corresponding bone id
        int boneId = Array.FindIndex(skeletonBones, x => x.name == node.name);

        // If there is an animation param for this bone
        if (animation.Keys.ToList().Contains(boneId)) {

            // Rotate it
            node.Rotate(animation[boneId]);
        }

        foreach (Transform childNode in node) {

            AnimateSkeletonWithHierarchy(childNode, animation, skeletonBones);
        }

    }

    public static void AnimateSkeletonWithHierarchy(Transform node, Dictionary<int, Quaternion> animation, Transform[] skeletonBones) {

        // Get the corresponding bone id
        int boneId = Array.FindIndex(skeletonBones, x => x.name == node.name);

        // If there is an animation param for this bone
        if (animation.Keys.ToList().Contains(boneId)) {

            // Rotate it
            node.localRotation = animation[boneId];
        }

        foreach (Transform childNode in node) {

            AnimateSkeletonWithHierarchy(childNode, animation, skeletonBones);
        }

    }

    public static Matrix4x4[] AnimateSkeletonWithHierarchy(Transform root, Dictionary<int, Quaternion> animation, Dictionary<int, int> boneIdToSkeletonArrayBoneId, List<int[]> allPaths) {

        Transform[] skeletonJoints = root.GetComponentsInChildren<Transform>();
        Matrix4x4[] jointIdToAccumulatedRotations = new Matrix4x4[skeletonJoints.Length];

        for (int j=0; j<skeletonJoints.Length; j++) {

            skeletonJoints[boneIdToSkeletonArrayBoneId[j]].localRotation = animation[j];

            jointIdToAccumulatedRotations[j] = Matrix4x4.Rotate(Quaternion.identity);

            int[] parentJointsOfCurrentJoint = Utils.FindParentJointsOf(j, allPaths);
            foreach (int jid in parentJointsOfCurrentJoint) {
                if (animation.Keys.ToList().Contains(jid)) {
                    jointIdToAccumulatedRotations[j] *= Matrix4x4.Rotate(animation[jid]);
                }
            }
        }

        return jointIdToAccumulatedRotations;
    }

    public static Matrix4x4[] AnimateSkeletonWithHierarchy(Transform root, Dictionary<int, Vector3> animation, Dictionary<int, int> boneIdToSkeletonArrayBoneId, List<int[]> allPaths) {

        Transform[] skeletonJoints = root.GetComponentsInChildren<Transform>();
        Matrix4x4[] jointIdToAccumulatedRotations = new Matrix4x4[skeletonJoints.Length];

        for (int j=0; j<skeletonJoints.Length; j++) {
            
            skeletonJoints[boneIdToSkeletonArrayBoneId[j]].Rotate(animation[j]);

            jointIdToAccumulatedRotations[j] = Matrix4x4.Rotate(Quaternion.identity);

            int[] parentJointsOfCurrentJoint = Utils.FindParentJointsOf(j, allPaths);
            foreach (int jid in parentJointsOfCurrentJoint) {
                if (animation.Keys.ToList().Contains(jid)) {
                    jointIdToAccumulatedRotations[j] *= Matrix4x4.Rotate(Quaternion.Euler(animation[jid]));
                }
            }
        }

        return jointIdToAccumulatedRotations;
    }

    public static Matrix4x4[][] AnimateMultipleSkeletonsWithHierarchy(GameObject[] skeletons, Dictionary<int, Vector3>[] animations, Dictionary<int, int> boneIdToSkeletonArrayBoneId, List<int[]> allPaths) {

        
        Matrix4x4[][] jointIdToAccumulatedRotations = new Matrix4x4[skeletons.Length][]; //[skeletonJoints.Length];

        for (int sk=0; sk<skeletons.Length; sk++) {
            Transform[] skeletonJoints = skeletons[sk].transform.GetComponentsInChildren<Transform>();
            jointIdToAccumulatedRotations[sk] = new Matrix4x4[skeletonJoints.Length];

            for (int j=0; j<skeletonJoints.Length; j++) {
                
                skeletonJoints[boneIdToSkeletonArrayBoneId[j]].Rotate(animations[sk][j]);

                jointIdToAccumulatedRotations[sk][j] = Matrix4x4.Rotate(Quaternion.identity);

                int[] parentJointsOfCurrentJoint = Utils.FindParentJointsOf(j, allPaths);
                foreach (int jid in parentJointsOfCurrentJoint) {
                    if (animations[sk].Keys.ToList().Contains(jid)) {
                        jointIdToAccumulatedRotations[sk][j] *= Matrix4x4.Rotate(Quaternion.Euler(animations[sk][jid]));
                    }
                }
            }

        }

        return jointIdToAccumulatedRotations;
    }

    public static Matrix4x4[][] AnimateMultipleSkeletonsWithHierarchy(GameObject[] skeletons, Dictionary<int, Vector3>[] animations, List<int[]> allPaths) {

        // This array of matrices will hold for each skeleton and for each joint of the skeleton the total/accumulated rotation that this joint should do.
        Matrix4x4[][] jointIdToAccumulatedRotations = new Matrix4x4[skeletons.Length][]; //[skeletonJoints.Length];

        // For each skeleton
        for (int sk=0; sk<skeletons.Length; sk++) {

            // Get the joints in an array
            Transform[] skeletonJoints = skeletons[sk].transform.GetComponentsInChildren<Transform>();
            jointIdToAccumulatedRotations[sk] = new Matrix4x4[skeletonJoints.Length];

            // For each joint
            for (int j=0; j<skeletonJoints.Length; j++) {
                
                // Rotate the joint according to the animation parameter (kinematics)
                skeletonJoints[j].Rotate(animations[sk][j]);

                jointIdToAccumulatedRotations[sk][j] = Matrix4x4.Rotate(Quaternion.identity);

                // Find the parent /grandparent etc joints of the current joint
                int[] parentJointsOfCurrentJoint = Utils.FindParentJointsOf(j, allPaths);

                foreach (int jid in parentJointsOfCurrentJoint) {

                    // If any of the parent/grandparent joints has an animation parameter
                    if (animations[sk].Keys.ToList().Contains(jid)) {
                        // Accumulate its rotation for the current joint
                        jointIdToAccumulatedRotations[sk][j] *= Matrix4x4.Rotate(Quaternion.Euler(animations[sk][jid]));
                    }
                }
            }

        }

        return jointIdToAccumulatedRotations;
    }

    public static Matrix4x4[][] AnimateMultipleSkeletonsWithHierarchy(GameObject[] skeletons, List<Quaternion>[] animations, List<int[]> allPaths) {

        // This array of matrices will hold for each skeleton and for each joint of the skeleton the total/accumulated rotation that this joint should do.
        Matrix4x4[][] jointIdToAccumulatedRotations = new Matrix4x4[skeletons.Length][]; //[skeletonJoints.Length];

        // For each skeleton
        for (int sk=0; sk<skeletons.Length; sk++) {

            // Get the joints in an array
            Transform[] skeletonJoints = skeletons[sk].transform.GetComponentsInChildren<Transform>();
            jointIdToAccumulatedRotations[sk] = new Matrix4x4[skeletonJoints.Length];

            // For each joint
            for (int j=0; j<skeletonJoints.Length; j++) {
                
                // Rotate the joint according to the animation parameter (kinematics)
                skeletonJoints[j].localRotation = animations[sk][j];

                jointIdToAccumulatedRotations[sk][j] = Matrix4x4.Rotate(Quaternion.identity);

                // Find the parent /grandparent etc joints of the current joint
                int[] parentJointsOfCurrentJoint = Utils.FindParentJointsOf(j, allPaths);

                foreach (int jid in parentJointsOfCurrentJoint) {

                    // If any of the parent/grandparent joints has an animation parameter
                    // if (animations[sk].Keys.ToList().Contains(jid)) {
                        // Accumulate its rotation for the current joint
                        jointIdToAccumulatedRotations[sk][j] *= Matrix4x4.Rotate(animations[sk][jid]);
                    // }
                }
            }

        }

        return jointIdToAccumulatedRotations;
    }

public static Matrix4x4[] AnimateMultipleSkeletonsWithHierarchy1DOld(GameObject[] skeletons, Dictionary<int, Quaternion>[] animations, Dictionary<int, int> boneIdToSkeletonArrayBoneId, List<int[]> allPaths) {

        
        Matrix4x4[] jointIdToAccumulatedRotations = new Matrix4x4[skeletons.Length * boneIdToSkeletonArrayBoneId.Keys.Count]; //[skeletonJoints.Length];

        for (int sk=0; sk<skeletons.Length; sk++) {
            Transform[] skeletonJoints = skeletons[sk].transform.GetComponentsInChildren<Transform>();

            for (int j=0; j<skeletonJoints.Length; j++) {
                
                skeletonJoints[boneIdToSkeletonArrayBoneId[j]].localRotation = animations[sk][j];

                jointIdToAccumulatedRotations[j + sk * skeletonJoints.Length] = Matrix4x4.Rotate(Quaternion.identity);

                int[] parentJointsOfCurrentJoint = Utils.FindParentJointsOf(j, allPaths);
                foreach (int jid in parentJointsOfCurrentJoint) {
                    if (animations[sk].Keys.ToList().Contains(jid)) {
                        jointIdToAccumulatedRotations[j + sk * skeletonJoints.Length] *= Matrix4x4.Rotate(animations[sk][jid]);
                    }
                }
            }
        }

        return jointIdToAccumulatedRotations;
    }

    public static Matrix4x4[][] AnimateMultipleSkeletonsWithHierarchy(GameObject[] skeletons, Dictionary<int, Quaternion>[] animations, Dictionary<int, int> boneIdToSkeletonArrayBoneId, List<int[]> allPaths) {

        
        Matrix4x4[][] jointIdToAccumulatedRotations = new Matrix4x4[skeletons.Length][]; //[skeletonJoints.Length];

        for (int sk=0; sk<skeletons.Length; sk++) {
            Transform[] skeletonJoints = skeletons[sk].transform.GetComponentsInChildren<Transform>();
            jointIdToAccumulatedRotations[sk] = new Matrix4x4[skeletonJoints.Length];

            for (int j=0; j<skeletonJoints.Length; j++) {
                
                skeletonJoints[boneIdToSkeletonArrayBoneId[j]].localRotation = animations[sk][j];

                jointIdToAccumulatedRotations[sk][j] = Matrix4x4.Rotate(Quaternion.identity);

                int[] parentJointsOfCurrentJoint = Utils.FindParentJointsOf(j, allPaths);
                foreach (int jid in parentJointsOfCurrentJoint) {
                    if (animations[sk].Keys.ToList().Contains(jid)) {
                        jointIdToAccumulatedRotations[sk][j] *= Matrix4x4.Rotate(animations[sk][jid]);
                    }
                }
            }

        }

        return jointIdToAccumulatedRotations;
    }

    public static (Matrix4x4[], Vector4[]) AnimateMultipleSkeletonsWithHierarchy1D(GameObject[] skeletons, List<Quaternion>[] animations, List<int[]> allPaths, int numberOfJoints) {

        if (skeletons == null || skeletons.Length == 0 || animations.Length == 0) {
            return (new Matrix4x4[0], new Vector4[0]);
        }

        // This array of matrices will hold for each skeleton and for each joint of the skeleton the total/accumulated rotation that this joint should do.
        Matrix4x4[] jointIdToAccumulatedRotations = new Matrix4x4[skeletons.Length * numberOfJoints]; //[skeletonJoints.Length];
        Vector4[] animatedJointPosition = new Vector4[skeletons.Length * numberOfJoints];

        // For each skeleton
        for (int sk=0; sk<skeletons.Length; sk++) {
            Transform[] skeletonJoints = skeletons[sk].transform.GetComponentsInChildren<Transform>();

            // For each joint
            for (int j=0; j<skeletonJoints.Length; j++) {

                // Rotate the joint according to the animation parameter (kinematics)
                skeletonJoints[j].localRotation = animations[sk][j];

                jointIdToAccumulatedRotations[j + sk * skeletonJoints.Length] = Matrix4x4.Rotate(skeletonJoints[j].rotation);

                animatedJointPosition[j + sk * skeletonJoints.Length] = skeletonJoints[j].position;

                // jointIdToAccumulatedRotations[j + sk * skeletonJoints.Length] = Matrix4x4.Rotate(Quaternion.identity);

                // // Find the parent /grandparent etc joints of the current joint
                // int[] parentJointsOfCurrentJoint = Utils.FindParentJointsOf(j, allPaths);

                // foreach (int jid in parentJointsOfCurrentJoint) {
                //     jointIdToAccumulatedRotations[j + sk * skeletonJoints.Length] *= Matrix4x4.Rotate(animations[sk][jid]);
                // }
            }
        }

        return (jointIdToAccumulatedRotations, animatedJointPosition);
    }

    public static GameObject[] BuildSkeletonWithoutHierarchy(Transform[] bones) {
        
        // THis version just copies the transformation from the renderer.bones list to the new game objects
        GameObject[] skeleton = new GameObject[bones.Length];

        for (int rj=0; rj<bones.Length; rj++) {
            skeleton[rj] = new GameObject();
            skeleton[rj].transform.position = bones[rj].position;
            skeleton[rj].transform.localRotation = Quaternion.identity;
            skeleton[rj].transform.rotation = Quaternion.identity;
            skeleton[rj].name = bones[rj].name;
        }

        return skeleton;
    }

    public static GameObject[] BuildSkeletonWithoutHierarchy(Transform[] bones, Dictionary<string, Vector3> newJointPositions) {
        
        // THis version just copies the transformation from the renderer.bones list to the new game objects
        GameObject[] skeleton = new GameObject[bones.Length];

        for (int rj=0; rj<bones.Length; rj++) {
            skeleton[rj] = new GameObject();
            skeleton[rj].transform.position = newJointPositions[bones[rj].name];
            skeleton[rj].transform.localRotation = Quaternion.identity;
            skeleton[rj].transform.rotation = Quaternion.identity;
            skeleton[rj].name = bones[rj].name;
        }

        return skeleton;
    }

    public static GameObject[] BuildSkeletonWithoutHierarchy(Transform[] bones, Vector3[] positions) {
        
        // THis version just copies the transformation from the renderer.bones list to the new game objects
        GameObject[] skeleton = new GameObject[bones.Length];

        for (int rj=0; rj<bones.Length; rj++) {
            skeleton[rj] = new GameObject();
            skeleton[rj].transform.position = positions[rj];
            skeleton[rj].transform.localRotation = Quaternion.identity;
            skeleton[rj].transform.rotation = Quaternion.identity;
            skeleton[rj].name = bones[rj].name;
        }

        return skeleton;
    }

    public static void AnimateSkeletonWithoutHierarchy(GameObject[] skeleton, Dictionary<int, Vector3> animation, Transform[] skeletonBones, List<int[]> allPaths) {

        // GameObject[] animatedSkeleton = skeleton.Clone() as GameObject[];

        for (int j=0; j<skeleton.Length; j++) {
            // Get the corresponding bone id
            int boneId = Array.FindIndex(skeletonBones, x => x.name == skeleton[j].name);

            // If there is an animation param for this bone
            if (animation.Keys.ToList().Contains(boneId)) {

                skeleton[boneId].transform.transform.Rotate(animation[boneId]);

                // Get the joint ids of its children
                HashSet<int> childrenJoints = FindChildrenJointsOf(boneId, allPaths);

                // Rotate the all the children joints around this joint by as many degrees as the animation parameter dictates
                foreach (int cj in childrenJoints) {
                    // Here we use world coordinates

                    // Rotate the child joint around the parent joint
                    skeleton[cj].transform.RotateAround(skeleton[boneId].transform.position, skeleton[boneId].transform.right, animation[boneId][0]);
                    skeleton[cj].transform.RotateAround(skeleton[boneId].transform.position, skeleton[boneId].transform.up, animation[boneId][1]);
                    skeleton[cj].transform.RotateAround(skeleton[boneId].transform.position, skeleton[boneId].transform.forward, animation[boneId][2]);
                }
            }
        }

        // return animatedSkeleton;
    }

    public static HashSet<int> FindChildrenJointsOf(int startBone, List<int[]> allPaths) {

        HashSet<int> childrenBones = new HashSet<int>();
        List<int[]> pathsWithBone = allPaths.FindAll(x => x.Contains(startBone));
        foreach (int[] path in pathsWithBone) {
            int[] bonePath = new int[path.Length - Array.IndexOf(path, startBone) - 1];
            Array.Copy(path, Array.IndexOf(path, startBone) + 1, bonePath, 0, bonePath.Length);
            childrenBones.UnionWith(bonePath);
        }

        return childrenBones;
    }

    public static int[] FindParentJointsOf(int startBone, List<int[]> allPaths) {

        int[] pathWithJoint = allPaths.Find(x => x.Contains(startBone));
        int[] parentJoints = new int[Array.IndexOf(pathWithJoint, startBone) + 1];
        Array.Copy(pathWithJoint, parentJoints, parentJoints.Length);

        return parentJoints;
    }

    // Calculate the offsets between each vertex and each one of the bones/joints that it is influenced by. Each offset is in the local space of the corresponding bone.
    public static Dictionary<int, Dictionary<int, Vector3>> GetVerticesAndJointsOffsetsInTPose(Dictionary<int, VertexSkinningWeights> vertexSkinningInfo, Vector3[] vertices, GameObject[] skeletonTPose) {
        
        Dictionary<int, Dictionary<int, Vector3>> offsets = new Dictionary<int, Dictionary<int, Vector3>>();

        // For each vertex
        for (int vid=0; vid<vertices.Length; vid++) {

            offsets[vid] = new Dictionary<int, Vector3>();
            
            foreach (int influenceBoneId in vertexSkinningInfo[vid].bonesIds) {

                // offsets[vid][influenceBoneId] = vertices[vid] - (skeletonTPose[influenceBoneId].transform.position - skeletonTPose[0].transform.position);
                // Calculate the offset between the vertex and the joint, in hte joints local space.
                offsets[vid][influenceBoneId] = skeletonTPose[influenceBoneId].transform.InverseTransformVector(vertices[vid] - skeletonTPose[influenceBoneId].transform.position);
            }
        }

        return offsets;
    }

    public static Dictionary<int, Dictionary<int, Vector3>> GetVerticesAndJointsOffsetsInTPoseInWorldSpace(Dictionary<int, VertexSkinningWeights> vertexSkinningInfo, Vector3[] vertices, GameObject[] skeletonTPose) {
        
        Dictionary<int, Dictionary<int, Vector3>> offsets = new Dictionary<int, Dictionary<int, Vector3>>();

        // For each vertex
        for (int vid=0; vid<vertices.Length; vid++) {

            offsets[vid] = new Dictionary<int, Vector3>();
            
            // For each joint that it is influenced by
            foreach (int influenceBoneId in vertexSkinningInfo[vid].bonesIds) {

                // offsets[vid][influenceBoneId] = vertices[vid] - (skeletonTPose[influenceBoneId].transform.position - skeletonTPose[0].transform.position);
                // Calculate the offset between the vertex and the joint, in world space.
                offsets[vid][influenceBoneId] = vertices[vid] - skeletonTPose[influenceBoneId].transform.position;
            }
        }

        return offsets;
    }

    public static Dictionary<int, Dictionary<int, Vector3>> GetVerticesAndJointsOffsetsInTPoseInWorldSpace(Dictionary<int, VertexSkinningWeights> vertexSkinningInfo, Vector3[] vertices, Dictionary<string, Vector3> jointsPositionsAtTPose) {
        
        Dictionary<int, Dictionary<int, Vector3>> offsets = new Dictionary<int, Dictionary<int, Vector3>>();

        // For each vertex
        for (int vid=0; vid<vertices.Length; vid++) {

            offsets[vid] = new Dictionary<int, Vector3>();
            
            // For each joint that it is influenced by
            foreach (int influenceBoneId in vertexSkinningInfo[vid].bonesIds) {

                // Calculate the offset between the vertex and the joint, in world space.
                offsets[vid][influenceBoneId] = vertices[vid] - jointsPositionsAtTPose[SocketReadThreading.jointOrderInSkeletonAnimationStream[influenceBoneId]];
            }
        }

        return offsets;
    }

    public static GameObject CreateNewMeshAtPosition(Transform position, Vector3[] cloneVertices) {
        Debug.Log($"Creating new mesh at {position.position}");

        GameObject newMesh = new GameObject("newMesh");
        
        newMesh.transform.position = position.position;
        // newMesh.transform.SetParent(newMeshParent.transform);
        newMesh.AddComponent<MeshFilter>();
        newMesh.AddComponent<MeshRenderer>();
        Mesh m = Resources.Load("moverse_mesh") as Mesh;
        Mesh meshInstance = Instantiate(m);

        // meshInstance.vertices = cloneVertices;
        // newMesh.GetComponent<MeshFilter>().mesh = meshInstance;

        newMesh.GetComponent<MeshFilter>().mesh.vertices = cloneVertices;
        newMesh.GetComponent<MeshFilter>().mesh.triangles = meshInstance.triangles;

        // Vector3[] vert = newMesh.GetComponent<MeshFilter>().mesh.vertices;
        // Vector3 vSum = new Vector3();
        // for (int i=0; i<vert.Length; i++) {
        //     vSum += vert[i];
        // }
        // Matrix4x4 transfMatrix = newMesh.GetComponent<MeshRenderer>().localToWorldMatrix;

        newMesh.GetComponent<MeshRenderer>().material = Resources.Load("material 3") as Material;

        return newMesh;
    }

    public static Matrix4x4[] GetJointsAccumulatedRotations(Dictionary<int, Vector3> animation, List<int[]> allPaths, int numJoints) {

        Matrix4x4[] jointIdToAccumulatedRotations = new Matrix4x4[numJoints];

        for (int bId=0; bId<jointIdToAccumulatedRotations.Length; bId++) {

            jointIdToAccumulatedRotations[bId] = Matrix4x4.Rotate(Quaternion.identity);

            int[] parentJointsOfCurrentJoint = Utils.FindParentJointsOf(bId, allPaths);
            foreach (int jid in parentJointsOfCurrentJoint) {
                if (animation.Keys.ToList().Contains(jid)) {
                    jointIdToAccumulatedRotations[bId] *= Matrix4x4.Rotate(Quaternion.Euler(animation[jid]));
                }
            }
        }

        return jointIdToAccumulatedRotations;
    }

    public static Matrix4x4[] GetJointsAccumulatedRotations(Dictionary<int, Quaternion> animation, List<int[]> allPaths, int numJoints) {

        Matrix4x4[] jointIdToAccumulatedRotations = new Matrix4x4[numJoints];

        for (int bId=0; bId<jointIdToAccumulatedRotations.Length; bId++) {

            jointIdToAccumulatedRotations[bId] = Matrix4x4.Rotate(Quaternion.identity);

            int[] parentJointsOfCurrentJoint = Utils.FindParentJointsOf(bId, allPaths);
            foreach (int jid in parentJointsOfCurrentJoint) {
                if (animation.Keys.ToList().Contains(jid)) {
                    jointIdToAccumulatedRotations[bId] *= Matrix4x4.Rotate(animation[jid]);
                }
            }
        }

        return jointIdToAccumulatedRotations;
    }

    public static byte[] CompressData(byte[] data)
    {
        using (var memoryStream = new MemoryStream())
        {
            using (var gzipStream = new GZipStream(memoryStream, System.IO.Compression.CompressionLevel.Optimal, leaveOpen: true))
            {
                gzipStream.Write(data, 0, data.Length);
            }
            return memoryStream.ToArray();
        }
    }

    public static byte[] DecompressData(byte[] compressedData)
    {
        using (var memoryStream = new MemoryStream(compressedData))
        using (var gzipStream = new GZipStream(memoryStream, CompressionMode.Decompress))
        using (var outputStream = new MemoryStream())
        {
            gzipStream.CopyTo(outputStream);
            return outputStream.ToArray();
        }
    }

    public static Vector3[] ConvertToVector3Array (float[] floats)
	{
		List<Vector3> vector3List = new List<Vector3>();
		for ( int i = 0; i < floats.Length; i += 3)
		{
			vector3List.Add( new Vector3(floats[i], floats[i+1], floats[i+2]) );
		}
		return vector3List.ToArray();
	}

    public static float[,] ConvertTo2DArray(float[] floats, int rows, int cols)
	{   
        float[,] array = new float[rows, cols];

		for (int r=0; r<rows; r++)
		{
            for (int c=0; c<cols; c++) {
                array[r,c] = floats[r*cols + c];
            }
		}

		return array;
	}

    public static List<GameObject> VisualizeSkeletonHierarchy(Transform root, List<GameObject> jointVisualizationSpheres) {
        foreach (Transform child in root) {
            GameObject sphere = GameObject.CreatePrimitive(PrimitiveType.Sphere);
            sphere.transform.position = child.position;
            sphere.transform.localScale = new Vector3(0.02f,0.02f,0.02f);
            jointVisualizationSpheres.Add(sphere);
            VisualizeSkeletonHierarchy(child, jointVisualizationSpheres);
        }

        return jointVisualizationSpheres;
    }

    public static void UpdateJointVisualization(Transform root, List<GameObject> jointVisualizationSpheres) {
        Transform[] joints = root.transform.GetComponentsInChildren<Transform>();
        for (int i=0; i<jointVisualizationSpheres.Count; i++) {
            jointVisualizationSpheres[i].transform.position = joints[i+1].position;
        }
    }

    public static void Save3DFloatArray(string path, float[][][] data)
    {
        using (BinaryWriter writer = new BinaryWriter(File.Open(path, System.IO.FileMode.Create)))
        {
            int dimX = data.Length;
            int dimY = data[0].Length;
            int dimZ = data[0][0].Length;

            writer.Write(dimX);
            writer.Write(dimY);
            writer.Write(dimZ);

            for (int x = 0; x < dimX; x++)
            for (int y = 0; y < dimY; y++)
            for (int z = 0; z < dimZ; z++)
            {
                writer.Write(data[x][y][z]);
            }
        }
    }

    public static float[][][] Load3DFloatArray(string path)
    {
        using (BinaryReader reader = new BinaryReader(File.Open(path, System.IO.FileMode.Open)))
        {
            int dimX = reader.ReadInt32();
            int dimY = reader.ReadInt32();
            int dimZ = reader.ReadInt32();

            float[][][] data = new float[dimX][][];

            for (int x = 0; x < dimX; x++)
            {
                data[x] = new float[dimY][];
                for (int y = 0; y < dimY; y++)
                {   
                    data[x][y] = new float[dimZ];
                    for (int z = 0; z < dimZ; z++)
                    {
                        data[x][y][z] = reader.ReadSingle();
                    }
                }
            }
            return data;
        }
    }

    public static void Save2DFloatArray(string path, float[][] data)
    {
        using (BinaryWriter writer = new BinaryWriter(File.Open(path, System.IO.FileMode.Create)))
        {
            int dimX = data.Length;
            int dimY = data[0].Length;

            writer.Write(dimX);
            writer.Write(dimY);

            for (int x = 0; x < dimX; x++)
            for (int y = 0; y < dimY; y++)
            {
                writer.Write(data[x][y]);
            }
        }
    }

    public static float[][] Load2DFloatArray(string path)
    {
        using (BinaryReader reader = new BinaryReader(File.Open(path, System.IO.FileMode.Open)))
        {
            int dimX = reader.ReadInt32();
            int dimY = reader.ReadInt32();

            float[][] data = new float[dimX][];

            for (int x = 0; x < dimX; x++)
            {
                data[x] = new float[dimY];
                for (int y = 0; y < dimY; y++)
                {   
                    data[x][y] = reader.ReadSingle();
                }
            }
            return data;
        }
    }

    public static void SaveIntList(string path, List<int> data)
    {
        using (BinaryWriter writer = new BinaryWriter(File.Open(path, System.IO.FileMode.Create)))
        {
            int dimX = data.Count;

            writer.Write(dimX);

            for (int x = 0; x < dimX; x++)
            {
                writer.Write(data[x]);
            }
        }
    }

    public static List<int> LoadIntList(string path)
    {
        using (BinaryReader reader = new BinaryReader(File.Open(path, System.IO.FileMode.Open)))
        {
            int dimX = reader.ReadInt32();

            List<int> data = new List<int>();

            for (int x = 0; x < dimX; x++)
            {
                data.Add(reader.ReadInt32());
            }
            return data;
        }
    }
}