import cv2
import mediapipe as mp
import numpy as np
import PoseModule as pm

cap = cv2.VideoCapture('videos\001.mp4')
detector = pm.poseDetector()
count = 0
direction = 0
form = 0
feedback = "Fix Form"

while cap.isOpened():
    ret, img = cap.read() #640 x 480

    # Determine dimensions of video - Help with creation of box in Line 43
    width  = cap.get(3)  # float `width`
    height = cap.get(4)  # float `height`
    
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)

    if len(lmList) != 0:
        ankle = detector.findAngle(img, 24, 26, 28)
        knee = detector.findAngle(img, 26, 24, 12)
        hip = detector.findAngle(img, 24, 12, 14)

        # Percentage of success of squat
        per = np.interp(ankle, (70, 150), (0, 100))

        # Bar to show squat progress
        bar = np.interp(ankle, (70, 150), (380, 50))

        # Check to ensure right form before starting the program
        if ankle > 150 and knee > 170 and hip > 170:
            form = 1

        # Check for full range of motion for the squat
        if form == 1:
            if per == 0:
                if ankle <= 70 and hip > 170:
                    feedback = "Down"
                    if direction == 0:
                        count += 1
                        direction = 1
                else:
                    feedback = "Fix Form"
            if per == 100:
                if ankle > 150 and knee > 170 and hip > 170:
                    feedback = "Up"
                    if direction == 1:
                        direction = 0
                else:
                    feedback = "Fix Form"

        # Draw Bar
        if form == 1:
            cv2.rectangle(img, (580, 50), (600, 380), (0, 255, 0), 3)
            cv2.rectangle(img, (580, int(bar)), (600, 380), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, f'{int(per)}%', (565, 430), cv2.FONT_HERSHEY_PLAIN, 2,
                        (255, 0, 0), 2)

        # Squat counter
        cv2.rectangle(img, (0, 380), (100, 480), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (25, 455), cv2.FONT_HERSHEY_PLAIN, 5,
                    (255, 0, 0), 5)

        # Feedback
        cv2.rectangle(img, (500, 0), (640, 40), (255, 255, 255), cv2.FILLED)
        cv2.putText(img, feedback, (500, 40), cv2.FONT_HERSHEY_PLAIN, 2,
                    (0, 255, 0), 2)

    cv2.imshow('Squat counter', img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
