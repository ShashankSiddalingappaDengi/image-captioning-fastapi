# 🖼️ Image Captioning with CNN-LSTM (FastAPI + Docker)

## 📌 Overview
This project implements an **Image Captioning API** that generates textual descriptions for input images.  
It combines a **Convolutional Neural Network (CNN)** (ResNet-50) for **feature extraction** and an **LSTM** for **caption generation**.  
The model is exposed as a REST API built with **FastAPI**, containerized using **Docker**, and ready for cloud deployment (AWS EC2 compatible).

---

## ⚙️ Tech Stack
- **Python 3.10**
- **PyTorch** (Deep Learning Framework)
- **FastAPI + Uvicorn** (High-performance API framework)
- **Docker** (Containerization)
- **COCO Dataset** (Training and evaluation)
- **NLTK, Pillow, PyCocoTools** (Preprocessing & tokenization)

---

## 🧠 Model Architecture
- **Encoder:** CNN (ResNet-50) pre-trained on ImageNet, outputs visual features  
- **Decoder:** LSTM network generating captions word-by-word  
- **Vocabulary Builder:** Uses COCO annotations to tokenize and threshold frequent words  
- **Inference:** Greedy decoding to predict sentence sequences  

---

## 📂 Project Structure
image-captioning-fastapi/
│
├── app.py # FastAPI application entrypoint
├── model.py # CNN-LSTM model architecture
├── vocabulary.py # Vocabulary class to tokenize captions
├── requirements.txt # Python dependencies
├── Dockerfile # Docker build file
└── .gitignore


---

## 🚀 Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YourUsername/image-captioning-fastapi.git
cd image-captioning-fastapi
```

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run FastAPI app
uvicorn app:app --reload


Now open 👉 http://127.0.0.1:8000/docs

Upload an image and get a generated caption instantly.

🐳 Run with Docker
1️⃣ Build Docker image
docker build -t image-captioning-app .

2️⃣ Run the container
docker run -p 8000:8000 image-captioning-app


Access the API at 👉 http://localhost:8000/docs

🧩 Example Request (Python)
import requests

url = "http://127.0.0.1:8000/predict"
files = {"file": open("example.jpg", "rb")}
response = requests.post(url, files=files)
print(response.json())


Response:

{
  "caption": "a group of people sitting around a table with food"
}

🧱 Vocabulary Generation

To rebuild vocabulary from COCO dataset:

python vocabulary.py


You can adjust:

vocab_threshold

annotations_file path (for COCO captions)



📸 Example Output
Input Image	Predicted Caption
🧍‍♂️ Person riding a bike	“a man riding a bicycle down a city street”
🐶 Dog playing in park	“a dog running through grass with a ball”
