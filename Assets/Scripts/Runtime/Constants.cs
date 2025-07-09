using System;
using System.Collections.Generic;

namespace GaussianSplatting.Runtime
{
    public static class Constants
    {
        public enum SMPLType
        {
            SMPL,
            SMPLX,
            None,
        }

        public enum SplatRotationMode
        {
            None,
            LBS,
            QLBS,
        }

        public static readonly Dictionary<SMPLType, int[]> SMPLTypeToParentsIds = new Dictionary<SMPLType, int[]>
        {
            {SMPLType.SMPL, new int[24] { 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 12, 13, 14, 16, 17, 18, 19, 20, 21 }},
            {SMPLType.SMPLX, new int[55] {
                0,          0,          0,          0,          1,
                2,          3,          4,          5,          6,
                7,          8,          9,          9,          9,
               12,         13,         14,         16,         17,
               18,         19,         15,         15,         15,
               20,         25,         26,         20,         28,
               29,         20,         31,         32,         20,
               34,         35,         20,         37,         38,
               21,         40,         41,         21,         43,
               44,         21,         46,         47,         21,
               49,         50,         21,         52,         53
               }
            }
        };

        public static readonly Dictionary<SMPLType, int> SMPLTypeToNumberOfJoints = new Dictionary<SMPLType, int>
        {
            {SMPLType.SMPL, 24},
            {SMPLType.SMPLX, 55}
        };

        public static readonly Dictionary<int, SMPLType> NumberOfJointsToSMPLType = new Dictionary<int, SMPLType>
        {
            {24, SMPLType.SMPL},
            {55, SMPLType.SMPLX}
        };

        public static readonly Dictionary<SMPLType, Dictionary<string, int>> SMPLTypeToMoverseRigToSkeletonIds = new Dictionary<SMPLType, Dictionary<string, int>>()
        {
            { SMPLType.SMPL, new Dictionary<string, int>()
            {
                { "Pelvis", 0 },
                { "LeftHip", 2 },
                { "RightHip", 1 },
                { "Spine1", 3 },
                { "LeftKnee", 5 },
                { "RightKnee", 4 },
                { "Spine2", 6 },
                { "LeftAnkle", 8 },
                { "RightAnkle", 7 },
                { "Spine3", 9 },
                { "LeftFoot", 11 },
                { "RightFoot", 10 },
                { "Neck", 12 },
                { "LeftCollar", 14 },
                { "RightCollar", 13 },
                { "Head", 15 },
                { "LeftShoulder", 17 },
                { "RightShoulder", 16 },
                { "LeftElbow", 19 },
                { "RightElbow", 18 },
                { "LeftWrist", 21 },
                { "RightWrist", 20 },
                { "LeftHand", 23 },
                { "RightHand", 22 }
            }
            },
            { SMPLType.SMPLX, new Dictionary<string, int>()
            {
                { "Pelvis", 0 },
                { "LeftHip", 2 },
                { "RightHip", 1 },
                { "Spine1", 3 },
                { "LeftKnee", 5 },
                { "RightKnee", 4 },
                { "Spine2", 6 },
                { "LeftAnkle", 8 },
                { "RightAnkle", 7 },
                { "Spine3", 9 },
                { "LeftFoot", 11 },
                { "RightFoot", 10 },
                { "Neck", 12 },
                { "LeftCollar", 14 },
                { "RightCollar", 13 },
                { "Head", 15 },
                { "LeftShoulder", 17 },
                { "RightShoulder", 16 },
                { "LeftElbow", 19 },
                { "RightElbow", 18 },
                { "LeftWrist", 21 },
                { "RightWrist", 20 },
                { "LeftIndex1", 40 },
                { "LeftIndex2", 41 },
                { "LeftIndex3", 42 },
                { "LeftMiddle1", 43 },
                { "LeftMiddle2", 44 },
                { "LeftMiddle3", 45 },
                { "LeftPinky1", 46 },
                { "LeftPinky2", 47 },
                { "LeftPinky3", 48 },
                { "LeftRing1", 49 },
                { "LeftRing2", 50 },
                { "LeftRing3", 51 },
                { "LeftThumb1", 52 },
                { "LeftThumb2", 53 },
                { "LeftThumb3", 54 },
                { "RightIndex1", 25 },
                { "RightIndex2", 26 },
                { "RightIndex3", 27 },
                { "RightMiddle1", 28 },
                { "RightMiddle2", 29 },
                { "RightMiddle3", 30 },
                { "RightPinky1", 31 },
                { "RightPinky2", 32 },
                { "RightPinky3", 33 },
                { "RightRing1", 34 },
                { "RightRing2", 35 },
                { "RightRing3", 36 },
                { "RightThumb1", 37 },
                { "RightThumb2", 38 },
                { "RightThumb3", 39 },
            }
            },
        };

        public static readonly int[] skeletonJointsIdsToStreamingIds = new int[24] {1, 6, 2, 10, 7, 3, 11, 8, 4, 12, 9, 5, 18, 20, 13, 19, 21, 14, 22, 15, 23, 16, 24, 17};
    }
}