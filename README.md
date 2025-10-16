# 🏋️‍♂️ AI Fitness Tracker  
**Real-time Pose Detection & Exercise Counter using OpenCV + MediaPipe**

This project uses **computer vision** to detect human body poses and automatically count **push-ups** and **bicep curls** with live feedback on form and motion accuracy — all through your webcam or video file.

---

## 🚀 Features

- 🤖 **Pose Detection** using [MediaPipe](https://google.github.io/mediapipe/)
- 🧍 Tracks body landmarks (shoulder, elbow, hip, wrist)
- 🧮 Counts **Push-ups** and **Bicep Curls** automatically
- 📊 Displays progress bars & percentage completion
- ⚡ Real-time feedback for incorrect form
- 🎥 Works with both **webcam** and **video input**

---

## 🧩 Project Structure

📂 AI-Fitness-Tracker
├── PoseModule.py # Handles pose detection & angle calculations
├── PushUpCounter.py # Push-up counter with form validation
├── BicepCurlCounter.py # Bicep curl counter using arm angles
└── README.md # Project documentation


---

## 🧠 How It Works

1. **PoseModule.py** – Creates a custom `poseDetector` class using MediaPipe Pose.  
   - Detects 33 human body landmarks  
   - Calculates joint angles (e.g., elbow, shoulder, hip)  
   - Visualizes pose landmarks on frames  

2. **PushUpCounter.py** –  
   - Uses the `poseDetector` to track arm and hip angles  
   - Counts push-ups based on full range of motion  
   - Provides live feedback ("Up", "Down", "Fix Form")  

3. **BicepCurlCounter.py** –  
   - Detects elbow flexion and extension  
   - Counts curls when motion completes full range  
   - Gives real-time form correction  

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/AI-Fitness-Tracker.git
cd AI-Fitness-Tracker


| Tool         | Purpose                                |
| ------------ | -------------------------------------- |
| 🧠 MediaPipe | Pose estimation and landmark detection |
| 🎥 OpenCV    | Frame capture and drawing              |
| 🔢 NumPy     | Math & interpolation calculations      |
| 🧱 imutils   | Image resizing utilities               |

🖼️ Example Output

When you run the code:

You’ll see your pose skeleton drawn on screen

A counter at the bottom tracking your reps

A progress bar showing your motion range

Real-time form feedback on screen
