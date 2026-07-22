# Facial Recognition Event Finder

⚠️ **Status:** In Development / Work in Progress

## 📝 Description
A Python-based backend API and facial recognition system built leveraging OpenCV, Dlib, and face_recognition libraries. The system is designed to receive a user's photo, scan image repositories stored in the cloud, and identify matching individuals using biometric data.

---

## 🧠 Project & Learning Objectives
This project is being developed to master Python backend architecture, cloud storage integration, and computer vision. The main technical goals of this development are:

* **Computer Vision & Biometrics:** To build a complete facial recognition pipeline, extracting facial landmarks, processing image vectors (embeddings), and handling face comparison.
* **Database & ORM Integration:** To implement relational database communication using **SQLAlchemy** and **MySQL** for data persistence and user metadata tracking.
* **Cloud Storage Management:** To explore cloud integration for storing, retrieving, and processing large volumes of images efficiently.
* **Security & Environment Management:** To apply security best practices by using `python-dotenv` to isolate and safeguard sensitive credentials and API keys.
* **Application Observability:** To integrate Python's standard `logging` library to efficiently track application behavior, request processing, and manage errors during debugging.

---

## 🛠️ Tech Stack & Libraries
* **Language:** Python 3.x
* **Computer Vision:** OpenCV (`cv2`), Dlib, `face_recognition`
* **Database & ORM:** MySQL, SQLAlchemy
* **Security:** `python-dotenv`
* **Infrastructure / Cloud:** *To be selected (AWS S3, Google Cloud Storage, or similar)*

---

## 🗺️ Roadmap & Next Steps
Here is what has been planned for the backend development lifecycle (subject to adjustments as cloud architecture is defined):

- [ ] 🟡 **In Progress:** Initialize facial recognition pipeline setup with OpenCV and Dlib.
- [X] Configure system logging library for debugging and tracking backend events.
- [X] Implement environment variable security (`.env`).
- [X] Model the database schema and establish connections using **SQLAlchemy** and **MySQL**.
- [ ] Integrate a cloud storage solution to handle and scan stored images.
- [ ] Develop the web API endpoints to receive user uploads and return recognition results.