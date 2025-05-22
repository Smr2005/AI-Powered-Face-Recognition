# 🤖 Face Recognition Attendance System

A powerful AI-based face recognition attendance system built using **Python**, **Flask**, **OpenCV**, and **face_recognition**. This application captures, registers, and recognizes faces in real-time using webcam input — beautifully wrapped in a modern animated web UI. It's secure, fast, and built for practical deployments.

---

## 🚀 Features

- 🎥 **Real-time Face Detection** with OpenCV
- 🧠 **Cosine Similarity Matching** using `face_recognition`
- 📦 **Auto Training Pipeline** on Registration
- 📸 **Multiple Image Capture per User**
- 🖼️ **Beautiful Animated Front-End** (HTML/CSS + SVG)
- 🔐 **No Cloud Uploads** – All Local & Private
- 📱 Responsive & Clean UI with Custom Pages:
  - `Home`
  - `Register`
  - `Recognize`
  - `About the Project`
  - `About the Developer`

---

## 📂 Project Structure

face-recognition-app/
│
├── static/
│ └── css/
│ └── style.css
│
├── templates/
│ ├── index.html
│ ├── register.html
│ ├── recognize.html
│ ├── about.html
│ └── developer.html
│
├── dataset/
│ └── [User_Folder]/img_0.png ...
│
├── encodings.pkl
├── face_app.py
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 💻 Technologies Used

| Tech         | Purpose                            |
|--------------|-------------------------------------|
| `Flask`      | Web framework for app routing       |
| `OpenCV`     | Camera access + drawing             |
| `face_recognition` | Face encodings + detection     |
| `NumPy`      | Vector calculations                 |
| `scikit-learn` | Cosine similarity scoring         |
| `HTML/CSS`   | Frontend UI                         |
| `JavaScript` | Webcam access, image capture        |

---

## 📸 How It Works

1. **Register** your face by capturing 4 images.
2. **Model auto-trains** and stores encodings locally.
3. In **Recognize**, webcam matches your face in real-time.
4. Faces are matched using **Cosine Similarity**.
5. If the score > 0.6 → ✅ Marked as *Recognized*.

---

## 📦 Installation

```bash
git clone https://github.com/your-username/face-recognition-attendance.git
cd face-recognition-attendance

# (Optional) create a virtual env
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
python face_app.py
Open your browser: http://127.0.0.1:5000

🌐 Deployment Ready
Works on local LAN.

Can be deployed to Render, Replit, or Heroku.

Add gunicorn and a Procfile for production.

Need help deploying? Just ask!

🧠 Real-World Applications
🏫 Student Attendance

🏢 Employee Monitoring

🛡️ Secure Access Systems

📷 AI Surveillance Integration

🙋‍♂️ About the Developer
Sameer Shaik – B.Tech in AI & Data Science
📧 Email

"I'm passionate about using AI to solve real-world problems.
Outside tech, I'm a poet and storyteller by heart."

📎 LinkedIn
📦 GitHub
📸 Instagram
✍️ Writings


