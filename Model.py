import tensorflow as tf
import numpy as np
import joblib
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer


# Load the saved model
classifier = joblib.load('news_checker.pkl')

def text_to_features(title, article_text):
    corpus = []
    all_text=title+' '+article_text
    all_text=re.sub('[^a-zA-Z]', ' ', all_text)
    all_text=all_text.lower()
    all_text=all_text.split()
    ps=PorterStemmer()
    all_stopwords=stopwords.words('english')
    all_stopwords.remove('not')
    all_text=[ps.stem(word) for word in all_text if not word in set(all_stopwords)]
    all_text=' '.join(all_text)
    corpus.append(all_text)
    cv = CountVectorizer(max_features=1800)
    corpus = cv.fit_transform(corpus).toarray()
    return corpus

def check_fake_news(corpus):
    prediction = classifier.predict(corpus)
    return prediction


