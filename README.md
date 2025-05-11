# 📊 PDF Risk Analysis Web App

This is a Flask web application that performs **risk sentiment analysis** on uploaded PDF documents. It uses natural language processing (NLP) techniques to classify risk levels based on text sentiment, supports **Kannada and Hindi translations**, and provides **BLEU score evaluation** and **visual risk distribution** charts.

---

## 🚀 Features

- Upload and extract text from PDF documents.
- Perform sentiment-based risk classification (High / Medium / Low).
- Translate extracted text into Kannada and Hindi using Google Translate.
- Calculate BLEU scores for translated text to evaluate translation accuracy.
- Display results with visual charts (pie chart).
- Interactive web UI.

---

## 🛠️ Technologies Used

- **Flask** – Web framework
- **PyMuPDF (`fitz`)** – PDF text extraction
- **TextBlob** – Rule-based sentiment analysis
- **Hugging Face Transformers** – BERT-based sentiment classifier
- **Googletrans** – Translation to Kannada and Hindi
- **NLTK** – BLEU score calculation
- **Matplotlib** – Visualization (risk pie chart)

---

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/pdf-risk-analysis.git
   cd pdf-risk-analysis
Set up a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Example requirements.txt:
makefile
Copy
Edit
Flask
PyMuPDF
textblob
transformers
scikit-learn
matplotlib
numpy
nltk
googletrans==4.0.0-rc1
torch  # Required for transformers
Download NLTK resources:

python
Copy
Edit
import nltk
nltk.download('punkt')
🧪 Running the App
bash
Copy
Edit
python app.py
Then open your browser and navigate to:
👉 http://127.0.0.1:5000/

📂 File Structure
graphql
Copy
Edit
pdf-risk-analysis/
│
├── app.py                   # Main Flask app
├── templates/
│   └── index.html           # HTML template for frontend
├── static/
│   └── risk_pie_chart.png   # Generated risk pie chart
├── uploads/                 # Directory for uploaded PDFs
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
