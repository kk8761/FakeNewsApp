# FakeNewsApp
# 🧠 AI Fake News & Misinformation Detector

This is a full-stack AI-powered web application that detects fake or misleading news using Natural Language Processing (NLP). It uses a pre-trained transformer model from Hugging Face to classify input news as likely **real** or **fake** based on its sentiment and language.

---

## 🌐 Live Demo (optional)
You can host this on platforms like Vercel (frontend) and Render/railway.app (backend) for a free demo.

---

## 🚀 Features

- ✅ Real-time fake news prediction
- 🤖 NLP with Hugging Face Transformers
- ⚡ Fast backend using Python & Flask
- 🧑‍💻 Modern frontend with React.js
- 📦 Easy deployment (no GPU required)

---

## 🧰 Tech Stack

| Layer      | Tools Used                          |
|------------|-------------------------------------|
| Frontend   | HTML, CSS, JavaScript, React        |
| Backend    | Python, Flask, Transformers (Hugging Face) |
| Model      | `distilbert-base-uncased-finetuned-sst-2-english` (Sentiment analysis) |
| Hosting    | Can be deployed on Render/Vercel    |

---

## 📦 Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector

cd backend
pip install -r requirements.txt
python app.py

cd ../frontend
npm install
npm run dev

🧪 Example Usage
Input:
"NASA confirms the discovery of a new Earth-like planet named Kepler-452b that could support life."

Output:
✅ Prediction: POSITIVE → Likely Real

🤖 Model Info
The model used is distilbert-base-uncased-finetuned-sst-2-english, a sentiment analysis model trained on the SST-2 dataset.

POSITIVE = Trusted tone (likely real)

NEGATIVE = Suspicious/fear-based tone (possibly fake)

📁 Folder Structure
bash
Copy
Edit
fake-news-detector/
│
├── backend/             # Flask backend
│   ├── app.py
│   └── requirements.txt
│
├── frontend/            # React frontend
│   ├── index.html
│   └── script.js
