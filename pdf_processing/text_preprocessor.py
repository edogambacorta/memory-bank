def clean_text(text):
    # Basic cleaning: remove extra whitespace and strip
    return ' '.join(text.split())

def preprocess_text(text):
    return clean_text(text)
