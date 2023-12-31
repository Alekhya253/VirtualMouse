# Virtual Mouse using Hand Gestures
This Python script utilizes the MediaPipe library and OpenCV to create a virtual mouse controlled by hand gestures. The program detects hand landmarks, tracks the movement of the index finger, and simulates left-click and right-click actions based on defined gestures.

## Prerequisites
Libraries required to run the program:
* OpenCV (cv2)
* MediaPipe (mediapipe)
* PyAutoGUI (pyautogui)
## Usage
* Run the script: python virtual_mouse.py
* Hold your hand in front of the camera.
* Move your index finger to control the cursor.
* Perform gestures to trigger left-click and right-click actions.
## Controls
- Left-Click Gesture: Bring the thumb close to the index finger.
- Right-Click Gesture: Bring the middle finger close to the index finger.
### Additional Configurations
- Adjust the min_detection_confidence parameter for hand detection confidence.
- Modify the scaling factors for cursor speed.
