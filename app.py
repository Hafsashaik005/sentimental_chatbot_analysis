from flask import Flask, request, jsonify
import speech_recognition as sr
from textblob import TextBlob

app = Flask(__name__)

# Function to analyze sentiment
def analyze_sentiment(text):
    analysis = TextBlob(text).sentiment.polarity
    if analysis > 0:
        return "That sounds positive! 😊"
    elif analysis < 0:
        return "That sounds negative. 😞"
    else:
        return "That's quite neutral. 🫥"

@app.route('/')
def home():
    return "Sentiment Chatbot API is Running!"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get("text", "")
    response = analyze_sentiment(text)
    return jsonify({"response": response})

# Required for Vercel
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
