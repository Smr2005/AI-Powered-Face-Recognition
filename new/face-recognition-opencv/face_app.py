# Flask GUI Face Recognition App with Auto Training and Cosine Similarity
from flask import Flask, render_template, Response, request, redirect, url_for
import cv2
import os
import face_recognition
import pickle
import numpy as np
import base64
from datetime import datetime
import re
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

DATASET_DIR = "dataset"
ENCODINGS_PATH = "encodings.pkl"
SIMILARITY_THRESHOLD = 0.6

if not os.path.exists(DATASET_DIR):
    os.makedirs(DATASET_DIR)

# ========== Utility Functions ==========
def train_model():
    encodings_dict = {}
    for user_folder in os.listdir(DATASET_DIR):
        path = os.path.join(DATASET_DIR, user_folder)
        for img_name in os.listdir(path):
            img_path = os.path.join(path, img_name)
            image = face_recognition.load_image_file(img_path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                encodings_dict.setdefault(user_folder, []).append(encodings[0])
    with open(ENCODINGS_PATH, "wb") as f:
        pickle.dump(encodings_dict, f)


# ========== Flask Routes ==========
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        images = request.form.getlist("images[]")

        if not name or not images:
            return "❌ Name or images missing", 400

        user_dir = os.path.join(DATASET_DIR, name)
        os.makedirs(user_dir, exist_ok=True)

        for idx, data_url in enumerate(images):
            try:
                if "," not in data_url:
                    print(f"⚠️ Skipping invalid image at index {idx}")
                    continue
                header, encoded = data_url.split(",", 1)
                img_data = base64.b64decode(encoded)
                img_path = os.path.join(user_dir, f"img_{idx}.png")
                with open(img_path, "wb") as f:
                    f.write(img_data)
            except Exception as e:
                print(f"❌ Error saving image {idx}: {e}")

        train_model()
        return redirect(url_for("home"))

    return render_template("register.html")


def gen():
    if not os.path.exists(ENCODINGS_PATH):
        return
    with open(ENCODINGS_PATH, "rb") as f:
        encodings_dict = pickle.load(f)
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, faces)
        for (top, right, bottom, left), encoding in zip(faces, encodings):
            best_match = None
            best_score = 0.0
            for name, known_encs in encodings_dict.items():
                for known_enc in known_encs:
                    score = cosine_similarity([encoding], [known_enc])[0][0]
                    if score > best_score:
                        best_score = score
                        best_match = name
            label = best_match if best_score > SIMILARITY_THRESHOLD else "Unknown"
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route("/recognize")
def recognize():
    return render_template("recognize.html")

@app.route("/video_feed")
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/developer")
def developer():
    return render_template("developer.html")


if __name__ == '__main__':
    app.run(debug=True)
