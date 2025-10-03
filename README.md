
# Face Recognition Attendance System

This project is an automated attendance system that uses computer vision and facial recognition to identify individuals and log their attendance in real-time. The system captures video from a webcam, recognizes registered faces, and records their entry time into a daily CSV file.

## ✨ Features

  * **Real-Time Face Recognition**: Detects and identifies faces from a live video stream.
  * **Automated Attendance Logging**: Automatically records the name and timestamp of the first time a person is seen each day.
  * **Dynamic Database**: Easily add new individuals by simply placing their image in the dataset folder.
  * **Daily Reports**: Generates a new CSV file for each day's attendance records.

## 🛠️ Tech Stack & Dependencies

  * Python 3.8+
  * **OpenCV**: For video capture and image processing.
  * **face\_recognition**: A powerful and simple library for face recognition. (Built on top of `dlib`).
  * **NumPy**: For numerical operations.


### 2\. Prerequisites (Important\!)

The `face_recognition` library relies on `dlib`, which needs to be compiled. You may need to install `cmake` and a C++ compiler first.

  * **On macOS or Linux:**
    ```bash
    # Install dependencies (example for Ubuntu)
    sudo apt-get update
    sudo apt-get install build-essential cmake
    sudo apt-get install libopenblas-dev liblapack-dev
    sudo apt-get install libx11-dev libgtk-3-dev
    ```
  * **On Windows:**
      * You will need to install `cmake` and have Microsoft Visual Studio (or the C++ build tools) installed.
      * For detailed instructions, please follow the official **[face\_recognition installation guide](https://www.google.com/search?q=https://github.com/ageitgey/face_recognition%23installation)**.

### 3\. Create a Virtual Environment & Install Packages

It is highly recommended to use a Python virtual environment.

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install the required libraries
pip install opencv-python numpy face_recognition
```

## 🚀 How to Use

### 1\. Add Known Faces

Create a folder named `Dataset` in the project's root directory. Add images of the individuals you want to recognize into this folder.

  * Each image should contain a clear, front-facing picture of one person.
  * The filename of the image will be used as the person's name (e.g., `elon_musk.jpg`, `bill_gates.png`).

### 2\. Run the Application

Execute the main script to start the attendance system.

```bash
python Main.py
```

  * A window will open showing the feed from your webcam.
  * When a known face is detected, a green rectangle will appear around it with the person's name.
  * The system will automatically mark their attendance.

### 3\. View Attendance Records

  * An `Attendence` folder will be created automatically.
  * Inside this folder, a CSV file will be generated for the current date (e.g., `03-10-2025.csv`).
  * The file will contain the names of the attendees and the time they were first recognized.

## 📂 Project Structure

```
.
├── Dataset/
│   ├── person1_name.jpg
│   └── person2_name.png
├── Attendence/
│   └── 03-10-2025.csv
├── Main.py              # The main script to run the application
├── basic.py             # A simple script for testing face comparison
├── test.py              # A utility script for reading attendance files
└── README.md
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.
