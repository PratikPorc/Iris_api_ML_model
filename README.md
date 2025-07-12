# 🌸 Iris Classifier API

A FastAPI-based machine learning API that classifies Iris flower species using a Decision Tree model. The app is fully Dockerized and ready for deployment.

---

## 🚀 Features

- ✅ Predict species from Sepal & Petal measurements
- ✅ Uses a trained Decision Tree model
- ✅ Built with FastAPI + Uvicorn
- ✅ Dockerized for easy deployment
- ✅ Auto docs at `/docs` (Swagger)

---

## 🧪 Example Request

POST `/predict` → `http://localhost:8000/predict`

**JSON Body:**
```json
{
  "SepalLengthCm": 5.1,
  "SepalWidthCm": 3.5,
  "PetalLengthCm": 1.4,
  "PetalWidthCm": 0.2
}
```
**Response:**
```json

{
  "species": "setosa",
  "class_index": 0
}
```
## 🐳 Docker Usage

### 1. Build the image
```bash
docker build -t iris-api .
```
### 2. Run the container
```bash
docker run -d -p 8000:8000 iris-api
```
### 3. Visit the API docs
http://localhost:8000/docs

### 🛠 Tech Stack
Python 3.11
scikit-learn
FastAPI
Uvicorn
Docker

### 🧠 Model Info
Trained on Iris dataset (150 samples, 3 classes)

Preprocessed using label encoding

Model: DecisionTreeClassifier from scikit-learn

Saved using joblib

### 📂 Project Structure
```css
Copy
Edit
iris-api/
├── app/
│   ├── main.py
│   └── iris_model.pkl
├── requirements.txt
├── Dockerfile
└── README.md
```
### 📜 License
MIT License © 2025 Pratik Guha Roy
