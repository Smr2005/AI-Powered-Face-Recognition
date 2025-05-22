# Use a compatible Python image
FROM python:3.10-slim

# Install system packages required by dlib and face_recognition
RUN apt-get update && apt-get install -y \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    build-essential \
    && apt-get clean

# Upgrade pip
RUN pip install --upgrade pip

# ✅ Install prebuilt dlib wheel directly (bypasses compile!)
RUN pip install https://github.com/RPi-Distro/python-dlib/releases/download/v19.22.99/dlib-19.22.99-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl

# Install face_recognition and other dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app source code
WORKDIR /app
COPY . .

# Expose port and run
EXPOSE 5000
CMD ["python", "face_app.py"]
