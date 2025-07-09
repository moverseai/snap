using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraMovement : MonoBehaviour
{
    GameObject mainCamera;
    float horizontalInput;
    float verticalInput;
    public float rotationSpeed = 1000f;
    public float zoomSpeed = 100f;
    public float panSpeed = 100f;
    public float moveSpeed = 10f;
    float scrollWheel;

    // Start is called before the first frame update
    void Start()
    {
        mainCamera = GameObject.Find("Main Camera");
        mainCamera.transform.position = new Vector3(0, 1, -10);
    }

    // Update is called once per frame
    void Update()
    {
        // Mouse look
        if (Input.GetMouseButton(0)) {
            horizontalInput = Input.GetAxis("Mouse X");
            verticalInput = Input.GetAxis("Mouse Y");

            mainCamera.transform.Rotate(Vector3.up, horizontalInput * rotationSpeed * Time.deltaTime, Space.World);
            mainCamera.transform.Rotate(Vector3.right, -verticalInput * rotationSpeed * Time.deltaTime, Space.Self);
        }

        // WASD movement
        float moveHorizontal = Input.GetAxis("Horizontal"); // A, D
        float moveVertical = Input.GetAxis("Vertical"); // W, S

        Vector3 movement = new Vector3(moveHorizontal, 0.0f, moveVertical);
        mainCamera.transform.Translate(movement * moveSpeed * Time.deltaTime, Space.Self);
    }
}