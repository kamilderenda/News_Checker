import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model

# Assuming the model is already trained and saved as 'fake_news_model.h5'
model = load_model('fake_news_model.h5')


def check_fake_news(self):
    # Get input from the user
    title = self.textEdit.toPlainText()
    article_text = self.textEdit_2.toPlainText()

    # Preprocess input (you can add more text preprocessing here)
    input_text = title + " " + article_text

    # Convert input text to features the model expects
    # For example, you can tokenize the text and pad it (depending on your model)
    # Assuming the model uses tokenized and padded inputs (this depends on your training setup)
    input_features = self.text_to_features(input_text)

    # Make prediction (Fake: 0, Real: 1)
    prediction = model.predict(input_features)

    # Display the result in label_4
    if prediction[0] > 0.5:
        self.label_4.setText("REAL")
        self.label_4.setStyleSheet("color: green; font-size: 30px; font-weight: bold;")
    else:
        self.label_4.setText("FAKE")
        self.label_4.setStyleSheet("color: red; font-size: 30px; font-weight: bold;")


def text_to_features(self, text):
    # This function should transform your text into the format your model expects
    # Example: tokenizing and padding (if using a text classifier model)
    # You'll need to use the same tokenizer and preprocessing used during model training

    # For this example, assuming the model uses a simple vectorizer or tokenizer
    # Here you would implement the specific text-to-feature transformation

    # Convert text to a NumPy array (e.g., using tokenizer and padding if necessary)
    # For now, return a dummy array as a placeholder
    return np.array([[0.0]])  # Replace this with the real feature extraction process