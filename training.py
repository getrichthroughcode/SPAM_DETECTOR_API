# training.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from preprocessing import preprocess_text  # Import the preprocessing function from preprocessor.py
import joblib  # Import joblib to save the trained model

# Load data
data = pd.read_table('SMSSpamCollection.csv', header=None, encoding='UTF-8')
X = data[1]  # Text data
y = data[0]  # Labels

# Preprocess text data
X_preprocessed = X.apply(preprocess_text)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_preprocessed, y, test_size=0.2, random_state=42)

# Vectorize text data
vectorizer = TfidfVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

# Initialize and train SVM model
model = SVC(kernel='linear')
model.fit(X_train_vectors, y_train)

# Predict on test set
y_pred = model.predict(X_test_vectors)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Print results
print("Accuracy:", accuracy)
print("Classification Report:\n", report)

# Save the trained model and vectorizer
joblib.dump(model, 'spam_classifier_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
