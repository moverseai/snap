#if (UNITY_EDITOR) 
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using System.Linq;
using System;
using System.IO;
using UnityEditor.VersionControl;

public class AnimationBaker : MonoBehaviour
{
    [SerializeField] private AnimationClip animClip;
    [SerializeField] private int numberOfJoints;
    private float[][][] jointsQuaternionComponentsFromClip; // jointID, quat component, timestamp
    private float[][] pelvisPositionFromClip; // pos component, timestamp
    private int maxCurveDuration;
    private List<int> jointsIdsInAnimationClip = new List<int>();

    [SerializeField] private GaussianSplatting.Runtime.Constants.SMPLType smplModelType;

    // Start is called before the first frame update
    void Start()
    {
        EditorCurveBinding[] curveBindings = AnimationUtility.GetCurveBindings(animClip);

        // foreach (EditorCurveBinding cb in curveBindings)
        // {
        //     Debug.Log(cb.path);
        // }

        // Find maximum curve duration
        maxCurveDuration = Mathf.Max(curveBindings.Select((cb, index) => AnimationUtility.GetEditorCurve(animClip, curveBindings[index]).length).ToArray());

        jointsQuaternionComponentsFromClip = new float[numberOfJoints][][];

        AnimationCurve curve;
        for (int j = 0; j < numberOfJoints; j++)
        {
            jointsQuaternionComponentsFromClip[j] = new float[4][];
        }

        pelvisPositionFromClip = new float[3][];

        for (int i = 0; i < curveBindings.Length; i++)
        {
            string jointName = curveBindings[i].path.Split(':')[^1];
            // jointName = string.Concat(jointName[0].ToString().ToUpper(), jointName.Skip(1).ToString());
            int jointId = GaussianSplatting.Runtime.Constants.SMPLTypeToMoverseRigToSkeletonIds[smplModelType][FirstCharToUpper(jointName)];
            int componentId = curveBindings[i].propertyName switch
            {
                "m_LocalRotation.x" => 0,
                "m_LocalRotation.y" => 1,
                "m_LocalRotation.z" => 2,
                "m_LocalRotation.w" => 3,
                "m_LocalPosition.x" => 4,
                "m_LocalPosition.y" => 5,
                "m_LocalPosition.z" => 6,
                _ => -1
            };

            if (componentId == -1) continue;

            curve = AnimationUtility.GetEditorCurve(animClip, curveBindings[i]);
            float[] values = curve.keys.Select(k => k.value).ToArray();
            if (values.Length != maxCurveDuration) Array.Resize(ref values, maxCurveDuration);
            if (componentId <= 3)
            {
                jointsQuaternionComponentsFromClip[jointId][componentId] = values;
                jointsIdsInAnimationClip.Add(jointId);
            }
            else if (jointId == 0)
            {
                pelvisPositionFromClip[componentId - 4] = values;
            }
        }

        Utils.Save3DFloatArray(Path.Combine(Application.streamingAssetsPath, "jointsQuaternionComponentsFromClip.bin"), jointsQuaternionComponentsFromClip);
        Utils.Save2DFloatArray(Path.Combine(Application.streamingAssetsPath, "pelvisPositionFromClip.bin"), pelvisPositionFromClip);
        Utils.SaveIntList(Path.Combine(Application.streamingAssetsPath, "jointsIdsInAnimationClip.bin"), jointsIdsInAnimationClip);

        Debug.Log("Finished saving animation binaries.");
    }

    public static string FirstCharToUpper(string input) =>
        input switch
        {
            null => throw new ArgumentNullException(nameof(input)),
            "" => throw new ArgumentException($"{nameof(input)} cannot be empty", nameof(input)),
            _ => string.Concat(input[0].ToString().ToUpper(), input.Substring(1))
        };
}
#endif