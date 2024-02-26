import cv2
import mediapipe as mp
import numpy as np
import PoseModule as pm

cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
count = 0
direction = 0
feedback = "Start"

while cap.isOpened():
    ret, img = cap.read() #640 x 480
    
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)

    if len(lmList) != 0:
        knee = detector.findAngle(img, 26, 24, 22) # Update landmark indices for knee
        hip = detector.findAngle(img, 24, 12, 14)  # Update landmark indices for hip

        # Percentage of success of squats
        per = np.interp(knee, (70, 160), (0, 100))

        # Bar to show squat progress
        bar = np.interp(knee, (70, 160), (380, 50))

        # Check for correct squat form before starting the count
        if hip > 160:
            feedback = "Start"
            count = 0

        # Check for proper squat movement
        if per == 0:
            if knee <= 70 and hip > 160:
                feedback = "Down"
                if direction == 0:
                    count += 0.5
                    direction = 1
            else:
                feedback = "Fix Form"

        if per == 100:
            if knee > 160 and hip > 160:
                feedback = "Up"
                if direction == 1:
                    count += 0.5
                    direction = 0
            else:
                feedback = "Fix Form"

        # Draw progress bar
        cv2.rectangle(img, (580, 50), (600, 380), (0, 255, 0), 3)
        cv2.rectangle(img, (580, int(bar)), (600, 380), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'{int(per)}%', (565, 430), cv2.FONT_HERSHEY_PLAIN, 2,
                    (255, 0, 0), 2)

        # Draw squat counter
        cv2.rectangle(img, (0, 380), (100, 480), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (25, 455), cv2.FONT_HERSHEY_PLAIN, 5,
                    (255, 0, 0), 5)

        # Draw feedback text
        cv2.rectangle(img, (500, 0), (640, 40), (255, 255, 255), cv2.FILLED)
        cv2.putText(img, feedback, (500, 40), cv2.FONT_HERSHEY_PLAIN, 2,
                    (0, 255, 0), 2)

    cv2.imshow('Squat counter', img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
