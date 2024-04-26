import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
from sklearn.preprocessing import LabelEncoder

# Downloading NLTK resources (to be executed once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Loading the data
data = pd.read_table('SMSSpamCollection.csv', header=None, encoding='UTF-8')
classes = data[0]

encoder = LabelEncoder()
Y = encoder.fit_transform(classes)

# Initializing the lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Text preprocessing function
def preprocess_text(text):
    # Replacing email addresses
    processed = re.sub(r'^.+@[^\.].*\.[a-z]{2,}$', 'emailaddress', text)
    # Replacing currency symbols
    processed = re.sub(r'£|\$', 'moneysymb', processed)
    # Replacing phone numbers
    processed = re.sub(r'^\(?[\d]{3}\)?[\s-]?[\d]{3}[\s-]?[\d]{4}$', 'phonenumber', processed)
    # Replacing numbers
    processed = re.sub(r'\d+(\.\d+)?', 'number', processed)
    # Removing special characters and converting to lowercase
    processed = re.sub(r'[^\w\d\s]', ' ', processed.lower())
    # Removing extra spaces
    processed = re.sub(r'\s+', ' ', processed).strip()
    # Tokenization
    tokens = word_tokenize(processed)
    # Removing stopwords and lemmatizing
    processed_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(processed_tokens)

# Preprocessing the texts
data[1] = data[1].apply(preprocess_text)



