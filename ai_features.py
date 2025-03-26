from textblob import TextBlob
import nltk
from collections import Counter

nltk.download("punkt")

def summarize(text, num_sentences=2):
    sentences = text.split(". ")
    return ". ".join(sentences[:num_sentences]) + "."

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

def extract_keywords(text, num_keywords=5):
    words = [word.lower() for word in text.split() if len(word) > 3]
    common_words = Counter(words).most_common(num_keywords)
    return [word[0] for word in common_words]
