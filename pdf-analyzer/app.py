import os
import fitz  # PyMuPDF
from flask import Flask, render_template, request
from textblob import TextBlob
from transformers import pipeline
from sklearn.metrics import precision_recall_fscore_support
import matplotlib.pyplot as plt
import numpy as np
from nltk.translate.bleu_score import sentence_bleu
from googletrans import Translator  # For translation

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Load BERT Sentiment Analysis Model
bert_sentiment = pipeline("sentiment-analysis")

# Initialize Translator
translator = Translator()

# Function to extract text from PDFs
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = " ".join(page.get_text("text") for page in doc)
    return text

# Function to classify risk based on sentiment
def classify_risk(text):
    textblob_score = TextBlob(text).sentiment.polarity
    bert_score = bert_sentiment(text)[0]['score']
    
    if textblob_score < -0.5 or bert_score < 0.2:
        return "high"
    elif textblob_score < 0 or bert_score < 0.5:
        return "medium"
    else:
        return "low"

# Function for translating text to Kannada and Hindi
def translate_risk_analysis(text):
    translated_kn = translator.translate(text, src='en', dest='kn').text
    translated_hi = translator.translate(text, src='en', dest='hi').text
    return translated_kn, translated_hi

# Function to calculate BLEU score for translations
def calculate_bleu_score(reference, hypothesis):
    return sentence_bleu([reference.split()], hypothesis.split())

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pdf_file = request.files["pdf"]
        if pdf_file:
            pdf_path = os.path.join(app.config["UPLOAD_FOLDER"], pdf_file.filename)
            pdf_file.save(pdf_path)
            text = extract_text_from_pdf(pdf_path)

            # Risk classification
            risks = [{"text": line, "risk": classify_risk(line)} for line in text.split(".") if line]

            # Categorize risks
            categorized_risks = {"high": [], "medium": [], "low": []}
            for risk in risks:
                categorized_risks[risk["risk"]].append(risk)

            # Add translations and BLEU score calculation for each risk
            for risk in risks:
                risk_kn, risk_hi = translate_risk_analysis(risk["text"])
                risk["text_kn"] = risk_kn
                risk["text_hi"] = risk_hi
                risk["bleu_kn"] = calculate_bleu_score(risk["text"], risk_kn)
                risk["bleu_hi"] = calculate_bleu_score(risk["text"], risk_hi)

            # Generate Visualization
            generate_visualizations(categorized_risks)

            return render_template(
                "index.html", 
                categorized_risks=categorized_risks,
                risks=risks
            )
    return render_template("index.html")

# Function to generate visualization
def generate_visualizations(categorized_risks):
    labels = ["High", "Medium", "Low"]
    values = [len(categorized_risks["high"]), len(categorized_risks["medium"]), len(categorized_risks["low"])]

    plt.figure(figsize=(6,6))
    plt.pie(values, labels=labels, autopct="%1.1f%%", colors=["red", "orange", "green"])
    plt.title("Risk Severity Distribution")
    plt.savefig("static/risk_pie_chart.png")

if __name__ == "__main__":
    app.run(debug=True)
