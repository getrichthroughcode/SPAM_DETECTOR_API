# Necessary libraries

import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, recall_score
import joblib


def load_data(file_path):
    df = pd.read_csv(file_path, sep=',',usecols=[0,1], names=['v1', 'v2'],encoding='ISO-8859-1',skiprows=1)
    return df

def preprocess_data(df):
    df['v1'] = df['v1'].map({'spam': 1, 'ham': 0})
    df['v2'].fillna('', inplace=True) 
    df = df[df['v2'].str.strip() != '']
    df['v2'] = df['v2'].astype(str)
    print(df.head())
    return df


def feature_extraction(df):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['v2'])
    y = df['v1']
    return X,y,vectorizer

def train_model(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)
    model = MultinomialNB()
    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    recall   = recall_score(y_test,y_pred)

    print(f"Accuracy: {accuracy}")
    print(f"Recall: {recall}")
    print(f"Classification report: {classification_report(y_test,y_pred)}")
    
    return model 


def save_model(model,vectorizer,model_path,vectorizer_path):
    joblib.dump(model,model_path)
    joblib.dump(vectorizer,vectorizer_path)



if __name__ == "__main__":

    file_path = "data/spam.csv"

    df = load_data(file_path)
    df = preprocess_data(df)

    X, y, vectorizer = feature_extraction(df)

    model = train_model(X,y)

    save_model(model,vectorizer,model_path="models/model.pkl",vectorizer_path="models/vectorizer.pkl")

