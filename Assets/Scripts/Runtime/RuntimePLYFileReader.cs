using System.Collections.Generic;
using System.IO;
using Unity.Collections;
using UnityEngine;
using System;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

namespace GaussianSplatting.Runtime
{
    public struct InitialJointPositions
    {
        public Vector3 jPos;
        public byte r, g, b, a;
    }

    public class RuntimePLYFileReader
    {
        public static NativeArray<InitialJointPositions> ReadJointsPLYFile(string filePath)
        {
            NativeArray<byte> jointsRawData;
            ReadJointsFile(filePath, out var jointsCount, out var jointsStride, out List<string> attributes, out jointsRawData);

            NativeArray<InitialJointPositions> joints;
            joints = jointsRawData.Reinterpret<InitialJointPositions>(1);

            return joints;
        }

        public static void ReadJointsFile(string filePath, out int jointsCount, out int jointsStride, out List<string> attributesNames, out NativeArray<byte> jointsRawData)
        {
            using var fs = new FileStream(filePath, FileMode.Open, FileAccess.Read);
            ReadHeaderImpl(filePath, out jointsCount, out jointsStride, out attributesNames, fs, out _);

            jointsRawData = new NativeArray<byte>(jointsCount * jointsStride, Allocator.Persistent);
            var readBytes = fs.Read(jointsRawData);
            if (readBytes != jointsRawData.Length)
                throw new IOException($"PLY {filePath} read error, expected {jointsRawData.Length} data bytes got {readBytes}");
        }

        public static NativeArray<float> ReadSkinningWeightsPLYFile(string filePath, int numberOfJoints, out Constants.SplatRotationMode splatRotMode, out int shOrderRotation)
        {
            int N_WEIGHTS_PER_SPLAT = numberOfJoints;
            int N_COORDS = 3;
            int N_BYTES_PER_FLOAT = 4;
            // This contains not only the skinning weights bytes from the file, but also vertex position, and the faces lists bytes
            NativeArray<byte> skinningWeightsRawData;
            ReadSkinningWeightsFile(filePath, out var vertexCount, out var vertexStride, out List<string> attributes, out skinningWeightsRawData, out string splatRotationMode);

            splatRotMode = splatRotationMode switch
            {
                "none" => Constants.SplatRotationMode.None,
                "lbs" => Constants.SplatRotationMode.LBS,
                "lbs_v" => Constants.SplatRotationMode.LBS,
                "qlbs" => Constants.SplatRotationMode.QLBS,
                "qlbs_v" => Constants.SplatRotationMode.QLBS,
                "qlbs_sh1_v" => Constants.SplatRotationMode.QLBS,
                "qlbs_sh2_v" => Constants.SplatRotationMode.QLBS,
                _ => Constants.SplatRotationMode.None,
            };

            shOrderRotation = 0;
            Match match = Regex.Match(splatRotationMode, @"sh\d+");
            if (match.Success)
            {
                shOrderRotation = int.Parse(match.Value.Remove(0, 2));
            }
            // This contains only the bytes for the 
            NativeArray<byte> skinningWeightsBytes = new NativeArray<byte>(vertexCount * N_WEIGHTS_PER_SPLAT * N_BYTES_PER_FLOAT, Allocator.Persistent);
            for (int i = 0; i < vertexCount; i++)
            {
                NativeArray<byte>.Copy(skinningWeightsRawData, i * N_BYTES_PER_FLOAT * N_COORDS + i * N_BYTES_PER_FLOAT * N_WEIGHTS_PER_SPLAT + N_COORDS * N_BYTES_PER_FLOAT, skinningWeightsBytes, i * N_BYTES_PER_FLOAT * N_WEIGHTS_PER_SPLAT, N_BYTES_PER_FLOAT * N_WEIGHTS_PER_SPLAT);
            }

            return skinningWeightsBytes.Reinterpret<float>(1);
        }

        public static void ReadSkinningWeightsFile(string filePath, out int vertexCount, out int vertexStride, out List<string> attributesNames, out NativeArray<byte> skinningWeightsRawData, out string splatRotationMode)
        {
            using var fs = new FileStream(filePath, FileMode.Open, FileAccess.Read);
            ReadHeaderImpl(filePath, out vertexCount, out vertexStride, out attributesNames, fs, out splatRotationMode);

            skinningWeightsRawData = new NativeArray<byte>(vertexCount * vertexStride, Allocator.Persistent);
            var readBytes = fs.Read(skinningWeightsRawData);
            if (readBytes != skinningWeightsRawData.Length)
                throw new IOException($"PLY {filePath} read error, expected {skinningWeightsRawData.Length} data bytes got {readBytes}");
        }

        static void ReadHeaderImpl(string filePath, out int vertexCount, out int vertexStride, out List<string> attrNames, FileStream fs, out string splatRotationMode)
        {
            // C# arrays and NativeArrays make it hard to have a "byte" array larger than 2GB :/
            if (fs.Length >= 2 * 1024 * 1024 * 1024L)
                throw new IOException($"PLY {filePath} read error: currently files larger than 2GB are not supported");

            // read header
            vertexCount = 0;
            vertexStride = 0;
            attrNames = new List<string>();
            const int kMaxHeaderLines = 9000;
            splatRotationMode = "none";
            int faceCount = 0;
            for (int lineIdx = 0; lineIdx < kMaxHeaderLines; ++lineIdx)
            {
                var line = ReadLine(fs);
                if (line == "end_header" || line.Length == 0)
                    break;
                var tokens = line.Split(' ');

                if (tokens.Length == 3 && tokens[0] == "element" && tokens[1] == "vertex")
                    vertexCount = int.Parse(tokens[2]);
                if (tokens.Length == 2 && tokens[0] == "comment")
                    splatRotationMode = tokens[1];
                if (tokens.Length == 3 && tokens[0] == "property")
                {
                    ElementType type = tokens[1] switch
                    {
                        "float" => ElementType.Float,
                        "double" => ElementType.Double,
                        "uchar" => ElementType.UChar,
                        _ => ElementType.None
                    };
                    vertexStride += TypeToSize(type);
                    attrNames.Add(tokens[2]);
                }

                if (tokens.Length == 3 && tokens[0] == "element" && tokens[1] == "face")
                    faceCount = int.Parse(tokens[2]);
            }
            //Debug.Log($"PLY {filePath} vtx {vertexCount} stride {vertexStride} attrs #{attrNames.Count} {string.Join(',', attrNames)}");
        }

        enum ElementType
        {
            None,
            Float,
            Double,
            UChar
        }

        static int TypeToSize(ElementType t)
        {
            return t switch
            {
                ElementType.None => 0,
                ElementType.Float => 4,
                ElementType.Double => 8,
                ElementType.UChar => 1,
                _ => throw new ArgumentOutOfRangeException(nameof(t), t, null)
            };
        }

        static string ReadLine(FileStream fs)
        {
            var byteBuffer = new List<byte>();
            while (true)
            {
                int b = fs.ReadByte();
                if (b == -1 || b == '\n')
                    break;
                byteBuffer.Add((byte)b);
            }
            // if line had CRLF line endings, remove the CR part
            if (byteBuffer.Count > 0 && byteBuffer.Last() == '\r')
                byteBuffer.RemoveAt(byteBuffer.Count - 1);
            return Encoding.UTF8.GetString(byteBuffer.ToArray());
        }
    }
}