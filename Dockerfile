FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    libboost-all-dev \
    && apt-get clean

# Pre-install dlib and face_recognition from wheels
RUN pip install --upgrade pip
RUN pip install face_recognition

# Copy your app
WORKDIR /app
COPY . .

# Install other Python dependencies
RUN pip install -r requirements.txt

# Expose port and run
EXPOSE 5000
CMD ["python", "face_app.py"]
