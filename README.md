# 🩺 Skin Disease Classifier using Deep Learning

A Django-based web application that classifies skin diseases from uploaded images using a trained **EfficientNet-B4** deep learning model built with **PyTorch**.

---

## 📖 Project Overview

Skin diseases are among the most common health issues worldwide. Early diagnosis helps improve treatment outcomes, but access to dermatologists may not always be available.

This project uses Deep Learning to automatically classify skin disease images into different categories. Users can upload an image through a simple web interface and receive the predicted disease.

The application is built using:

- Django (Backend)
- PyTorch (Deep Learning)
- EfficientNet-B4
- HTML/CSS
- SQLite

---

## ✨ Features

- User Registration and Login
- Upload Skin Disease Images
- Image Classification using EfficientNet-B4
- Displays Predicted Disease
- Django Admin Panel
- Responsive User Interface
- Local SQLite Database
- Deployed on PythonAnywhere

---

## 🏗️ Project Structure

```
SkinDiseaseClassifier/
│
├── classifier/
│   ├── migrations/
│   ├── templates/
│   │   └── classifier/
│   │       ├── auth.html
│   │       ├── home.html
│   │       ├── login.html
│   │       └── result.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── SkinDiseaseClassifier/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
├── best_model_b4_optimized.pth
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 🧠 Deep Learning Model

Model Used:

- EfficientNet-B4

Framework:

- PyTorch

Purpose:

- Image Classification

---

## 📊 Disease Classes

The model predicts one of the following skin diseases:

1. Actinic Keratosis
2. Atopic Dermatitis
3. Benign Keratosis
4. Dermatofibroma
5. Melanocytic Nevus
6. Melanoma
7. Squamous Cell Carcinoma
8. Tinea Ringworm Candidiasis
9. Vascular Lesion

---

## 🛠 Technologies Used

### Programming Language

- Python 3.11

### Backend

- Django

### Deep Learning

- PyTorch
- Torchvision

### Frontend

- HTML
- CSS

### Database

- SQLite

### Deployment

- PythonAnywhere

### Version Control

- Git
- GitHub

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/GovardhanReddy731/SkinDiseaseClassifier.git
```

---

### Move into Project

```bash
cd SkinDiseaseClassifier
```

---

### Create Virtual Environment

Windows

```bash
python -m venv myvenv
```

Activate

```bash
myvenv\Scripts\activate
```

Linux

```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Apply Migrations

```bash
python manage.py migrate
```

---

### Start Development Server

```bash
python manage.py runserver
```

---

Open browser

```
http://127.0.0.1:8000/
```

---

## 🚀 Deployment

The application is deployed using **PythonAnywhere**.

Deployment steps include:

- Upload project
- Configure virtual environment
- Configure WSGI
- Collect static files
- Reload Web App

---

## 📷 Application Workflow

1. User opens the application.
2. User logs in.
3. User uploads a skin disease image.
4. Image is preprocessed.
5. EfficientNet-B4 predicts the disease.
6. Prediction is displayed.

---

## 📌 Future Improvements

- Mobile Application
- Confidence Score Display
- Disease Description
- Treatment Suggestions
- Multi-language Support
- Cloud Storage
- REST API
- Doctor Recommendation System

---

## 📈 Advantages

- Fast prediction
- Easy to use
- Web-based
- Accurate deep learning model
- Reduces diagnosis time

---

## ⚠ Limitations

- Limited to trained disease classes
- Prediction depends on image quality
- Not a replacement for medical professionals

---

## 📚 References

- Django Documentation
- PyTorch Documentation
- EfficientNet Research Paper
- PythonAnywhere Documentation

---

## 👨‍💻 Author

**Govardhan G A**

AI & Machine Learning Student

New Horizon College of Engineering

GitHub: https://github.com/GovardhanReddy731

LinkedIn: https://www.linkedin.com/in/govardhan-reddy731/

---

## ⭐ Support

If you found this project useful,

⭐ Star this repository

🍴 Fork it

📢 Share it

---

## 📜 License

This project is created for educational and research purposes.
