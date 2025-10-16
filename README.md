# 🏋️‍♂️ AI Fitness Tracker
**Real-time Pose Detection & Exercise Counter using OpenCV + MediaPipe**

This project uses **computer vision** to detect human body poses and automatically count **push-ups** and **bicep curls** with live feedback on form and motion accuracy — all through your webcam or video file.

---

## 🚀 Features

- Pose Detection using MediaPipe
- Tracks body landmarks (shoulder, elbow, hip, wrist)
- Counts Push-ups and Bicep Curls automatically
- Displays progress bars & percentage completion
- Real-time feedback for incorrect form
- Works with both webcam and video input

---

## 🧠 How It Works

### PoseModule.py
- Creates a custom `poseDetector` class using MediaPipe Pose
- Detects 33 human body landmarks
- Calculates joint angles (elbow, shoulder, hip)
- Visualizes pose landmarks on video frames

### PushUpCounter.py
- Uses `poseDetector` to track arm and hip angles
- Counts push-ups based on full range of motion
- Provides live feedback ("Up", "Down", "Fix Form")

### BicepCurlCounter.py
- Detects elbow flexion and extension
- Counts curls when motion completes full range
- Gives real-time form correction

---

## 🧩 Project Structure

📂 AI-Fitness-Tracker  
├── PoseModule.py           # Handles pose detection & angle calculations  
├── PushUpCounter.py        # Push-up counter with form validation  
├── BicepCurlCounter.py     # Bicep curl counter using arm angles  
└── README.md               # Project documentation

## 🧱 Dependencies
| Tool        | Purpose                                |
| ----------- | -------------------------------------- |
| MediaPipe   | Pose estimation and landmark detection |
| OpenCV      | Frame capture and drawing              |
| NumPy       | Math & interpolation calculations      |
| imutils     | Image resizing utilities               |

## ▶️ Usage

### Run with Webcam
```bash
python PushUpCounter.py
# or
python BicepCurlCounter.py
```

### Run with Video File
```python
cap = cv2.VideoCapture("path_to_your_video.mp4")
```

### 🖼️ Example Output
### When you run the code:
- 🧍 Your pose skeleton is drawn on the screen 
- 🔢 A counter at the bottom tracks your reps 
- 📊 A progress bar shows your motion range 
- ⚠️ Real-time form feedback appears on screen

---

### 🙌 Author

**Naveen Kumar B**  
*Associate Software Developer*
