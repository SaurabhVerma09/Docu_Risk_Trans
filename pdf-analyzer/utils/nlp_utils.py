import spacy
from textblob import TextBlob

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

def analyze_risk(text):
    """Identifies potential risks and provides sentiment analysis."""
    doc = nlp(text)
    risk_keywords = ["breach", "penalty", "fine", "risk", "litigation", "obligation", "liability", "compliance"]
    risks = [sent.text for sent in doc.sents if any(keyword in sent.text.lower() for keyword in risk_keywords)]

    # Sentiment analysis on each risk
    risks_with_sentiment = []
    for risk in risks:
        sentiment = TextBlob(risk).sentiment
        risks_with_sentiment.append({
            "text": risk,
            "polarity": sentiment.polarity,
            "subjectivity": sentiment.subjectivity
        })

    return risks_with_sentiment
