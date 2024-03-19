import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
from sklearn.preprocessing import LabelEncoder

# Chargement des données
data = pd.read_table('SMSSpamCollection.csv',header = None, encoding='UTF-8')

classes = data[0]



encoder = LabelEncoder()

Y  = encoder.fit_transform(classes)

# Preprocessing using regular expression 

texts = data[1]

processed = texts.str.replace(r'^.+@[^\.].*\.[a-z]{2,}$', 'emailaddress')

processed = processed.str.replace(r'£|\$', 'moneysymb')

processed = processed.str.replace(r'^\(?[\d]{3}\)?[\s-]?[\d]{3}[\s-]?[\d]{4}$','phonenumber')

processed = processed.str.replace(r'\d+(\.\d+)?', 'number')

processed = processed.str.replace(r'[^\w\d\s]', ' ')

processed = processed.str.replace(r'\s+', ' ')

processed = processed.str.replace(r'^\s+|\s+?$', '')

processed = processed.str.lower()

print(processed)







