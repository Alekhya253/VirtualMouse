import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands(min_detection_confidence=0.5)
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

# Initialize x_index and y_index

x_index, y_index = 0, 0  
right_click_triggered = False

while True:
    _, frame = cap.read()

    frame = cv2.resize(frame, (840, 680))

    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark

            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if id == 4:  # Thumb tip
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y

                    # Check for left click gesture
                    if abs(y_index - thumb_y) < 20 and abs(x_index - thumb_x) < 20:
                        pyautogui.click()
                        print("Left Click!")

                if id == 8:  # Index finger tip
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    x_index = screen_width / frame_width * x
                    y_index = screen_height / frame_height * y

                    # to move the cursor along the index finger
                    pyautogui.moveTo(x_index, y_index)

                if id == 12:  # Middle finger tip
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    middle_finger_x = screen_width / frame_width * x
                    middle_finger_y = screen_height / frame_height * y

                    # Check if index and middle fingers are close for right click
                    if (
                        abs(x_index - middle_finger_x) < 20
                        and abs(y_index - middle_finger_y) < 20
                    ):
                        if not right_click_triggered:
                
                            pyautogui.rightClick()
                            print("Right Click!")
                            right_click_triggered = True

                    # Reset right_click_triggered if fingers are not close
                    if (
                        abs(x_index - middle_finger_x) >= 20
                        or abs(y_index - middle_finger_y) >= 20
                    ):
                        right_click_triggered = False

    cv2.imshow('Virtual Mouse', frame)

    # 'q' key press to quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture

cap.release()
cv2.destroyAllWindows()
