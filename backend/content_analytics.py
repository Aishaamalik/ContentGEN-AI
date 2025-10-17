import re
from textstat import flesch_reading_ease
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download NLTK data if not already downloaded
try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

def calculate_keyword_density(text, keyword):
    """Calculate keyword density in the text."""
    if not text or not keyword:
        return 0.0

    # Clean text and keyword
    text = text.lower()
    keyword = keyword.lower()

    # Count occurrences
    word_count = len(re.findall(r'\b\w+\b', text))
    keyword_count = len(re.findall(r'\b' + re.escape(keyword) + r'\b', text))

    if word_count == 0:
        return 0.0

    density = (keyword_count / word_count) * 100
    return round(density, 2)

def analyze_sentiment(text):
    """Analyze sentiment of the text using NLTK's VADER."""
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)

    # Return compound score and interpretation
    compound = sentiment['compound']
    if compound >= 0.05:
        sentiment_label = "Positive"
    elif compound <= -0.05:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    return {
        'compound_score': round(compound, 2),
        'sentiment': sentiment_label,
        'positive': round(sentiment['pos'], 2),
        'negative': round(sentiment['neg'], 2),
        'neutral': round(sentiment['neu'], 2)
    }

def calculate_readability_score(text):
    """Calculate readability score using Flesch Reading Ease."""
    if not text.strip():
        return 0.0

    score = flesch_reading_ease(text)

    # Interpret the score
    if score >= 90:
        level = "Very Easy"
    elif score >= 80:
        level = "Easy"
    elif score >= 70:
        level = "Fairly Easy"
    elif score >= 60:
        level = "Standard"
    elif score >= 50:
        level = "Fairly Difficult"
    elif score >= 30:
        level = "Difficult"
    else:
        level = "Very Difficult"

    return {
        'score': round(score, 2),
        'level': level
    }

def analyze_content(text, keyword=None):
    """Comprehensive content analysis."""
    analysis = {
        'readability': calculate_readability_score(text),
        'sentiment': analyze_sentiment(text)
    }

    if keyword:
        analysis['keyword_density'] = calculate_keyword_density(text, keyword)

    return analysis
