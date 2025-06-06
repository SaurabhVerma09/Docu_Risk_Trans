from googletrans import Translator  # type: ignore

# Creating function

def translate_risk_analysis(text):
    """Translates the given text to Kannada and Hindi."""
    translator = Translator()
    
    # Translate to Kannada and Hindi
    translation_kn = translator.translate(text, src='en', dest='kn').text
    
    # Translation in Hindi
    translation_hi = translator.translate(text, src='en', dest='hi').text
    
    return translation_kn, translation_hi
