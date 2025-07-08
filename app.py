from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

# Load a fake-news compatible model
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "No input text provided"}), 400

    prediction = classifier(data["text"])[0]
    return jsonify({"label": prediction["label"]})

if __name__ == "__main__":
    app.run(debug=True)
