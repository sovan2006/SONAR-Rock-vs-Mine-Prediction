# 🚢 SONAR Rock vs Mine Prediction

An AI-powered web application that classifies underwater objects as **Rock (R)** or **Mine (M)** using SONAR signal data and Machine Learning.

🌐 **Live Demo:** https://sonar-rock-vs-mine-prediction.onrender.com/

---

## 📌 Project Overview

This project uses a **Logistic Regression Machine Learning model** trained on the SONAR dataset to identify whether an object detected underwater is:

* 🪨 **Rock (R)**
* 💣 **Mine (M)**

The model analyzes **60 SONAR frequency measurements** and predicts the object category with a confidence score.

---

## ✨ Features

* Modern Web UI
* Real-Time Prediction
* Confidence Score Display
* Flask Backend API
* Machine Learning Classification
* Render Cloud Deployment
* Input Validation (Exactly 60 Features Required)

---

## 🧠 Machine Learning Model

**Algorithm Used:** Logistic Regression

### Input

The model accepts:

* 60 SONAR signal values
* Comma-separated numerical inputs
* Values ranging between 0 and 1

Example:

```text
0.0307,0.0523,0.0653,0.0521,0.0618,...
```

### Output

```text
🪨 ROCK
```

or

```text
💣 MINE
```

with confidence percentage.

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Flask
* NumPy
* Pickle

### Machine Learning

* Scikit-learn
* Logistic Regression
* Pandas

### Deployment

* Render

---

## 📂 Project Structure

```text
SONAR-Rock-vs-Mine-Prediction/
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
├── SONAR_Rock_vs_Mine_Prediction.ipynb
│
├── templates/
│   └── index.html
│
└── sonar data.csv
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/sovan2006/SONAR-Rock-vs-Mine-Prediction.git
cd SONAR-Rock-vs-Mine-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📊 Dataset

Dataset Used:

**SONAR Rock vs Mine Dataset**

* Total Features: 60
* Target Classes: Rock (R), Mine (M)
* Binary Classification Problem

---

## 🚀 Deployment

The application is deployed on Render:

https://sonar-rock-vs-mine-prediction.onrender.com/

---

## 📸 Screenshots

### Home Page
<img width="1133" height="776" alt="Screenshot 2026-06-25 at 10 03 48 AM" src="https://github.com/user-attachments/assets/4a40f5c2-1874-406e-a0f4-1a318249d51d" />


---

## 👨‍💻 Author

**Sovan Barik**

B.Tech Artificial Intelligence & Machine Learning

* GitHub: https://github.com/sovan2006
* LinkedIn: www.linkedin.com/in/sovan-barik-711bba326

