# Fake News Checker

## Overview

This project is a Fake News Detection System built using PyQt5 for the graphical user interface (GUI) and a Machine Learning Model for classification. The application allows users to input a news article's title and text, then determines whether the news is "FAKE" or "APPROVED" using a pre-trained Gaussian Naïve Bayes Model.

## Features

* User-friendly GUI built with PyQt5

* Machine Learning Fake News Detection

* Preprocessing of text using NLP techniques

* Model trained on a large dataset of news articles

* Uses a trained classifier (news_checker.pkl) and a vectorizer (vectorizer.pkl)

## Installation

### Prerequisites

Ensure you have Python installed along with the following dependencies:

pip install PyQt5 tensorflow numpy joblib nltk scikit-learn

## Setup

## Clone the repository:

git clone https://github.com/kamilderenda/fake-news-checker.git
cd fake-news-checker

## Download required NLTK Stopwords:

import nltk
nltk.download('stopwords')

Ensure news_checker.pkl and vectorizer.pkl are in the project directory.

## How to Run

python main.py

## Usage

Enter a title of the news article.

Enter the article text in the text box.

Click "Check" to classify the news.

The result will be displayed:

* APPROVED (Green) → If the news is real.

* FAKE NEWS (Red) → If the news is fake.

* Warning Message (Yellow) → If input fields are empty.

GUI Screenshots

Empty Input Warning: (User didn't enter text)

Approved News: (Model classified as real)

Fake News: (Model classified as fake)

![1](https://github.com/user-attachments/assets/3f7cf2f4-8c3f-47e0-beb4-1f1e2a751794)

![2](https://github.com/user-attachments/assets/c89805ea-a3a5-48d4-9480-9eb28b7ebc40)

![3](https://github.com/user-attachments/assets/9a5ba7e9-40cd-485e-8877-44069eed0fba)


Project Structure

├── GUI.py  # PyQt5 GUI Interface
├── Model.py  # Text processing and ML model
├── main.py  # Runs the application
├── news_checker.pkl  # Pre-trained classifier model
├── vectorizer.pkl  # Fitted CountVectorizer
└── README.md  # Documentation

## Technical Details

* GUI (GUI.py): Uses PyQt5 for UI elements.

* Model (Model.py):

  * Uses NLTK for text preprocessing.

  * Implements stemming and stopword removal.

  * Vectorizes text using CountVectorizer.

  * Classifies news using a Gaussian Naïve Bayes model.

* Data Preprocessing: Cleans text by removing special characters and stopwords.

## Future Enhancements

* Improve model accuracy with advanced NLP techniques (e.g., TF-IDF, deep learning models)

* Add support for multilingual fake news detection

* Deploy the application as a web-based tool
