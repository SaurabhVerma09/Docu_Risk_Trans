from flask import Flask, render_template, request
from utils.nlp_utils import analyze_risk
from utils.pdf_utils import extract_text_from_pdf
from utils.translation_utils import translate_risk_analysis  # Import the translation function

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    """Handles PDF upload and risk analysis."""
    uploaded_file = request.files['pdf']
    if uploaded_file:
        # Extract text from the uploaded PDF
        text = extract_text_from_pdf(uploaded_file)
        
        # Analyze risks from the extracted text
        risks = analyze_risk(text)

        # Add translations (Kannada and Hindi) to each risk
        for risk in risks:
            risk_kn, risk_hi = translate_risk_analysis(risk['text'])  # Translate each risk
            risk['text_kn'] = risk_kn
            risk['text_hi'] = risk_hi

        # Render the result page with summary and risk analysis
        return render_template('index.html', risks=risks)

if __name__ == "__main__":
    app.run(debug=True)
