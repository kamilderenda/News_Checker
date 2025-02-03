import tensorflow as tf
import numpy as np
import joblib
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer


classifier = joblib.load('news_checker.pkl')
cv = joblib.load('vectorizer.pkl')

def text_to_features(title, article_text):
    all_text = title + ' ' + article_text
    all_text = re.sub('[^a-zA-Z]', ' ', all_text)
    all_text = all_text.lower().split()

    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    all_text = [ps.stem(word) for word in all_text if word not in all_stopwords]

    processed_text = ' '.join(all_text)
    corpus = [processed_text]

    features = cv.transform(corpus).toarray()
    return features

def check_fake_news(title, article_text):
    corpus_features = text_to_features(title, article_text)
    prediction = classifier.predict(corpus_features)
    return "FAKE" if prediction[0] == 0 else "APPROVED"


