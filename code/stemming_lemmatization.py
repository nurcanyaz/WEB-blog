# Stemming and lemmatization

import nltk

nltk.download("wordnet")
#  wordnet:lemmatization işlemi için gerekli veritabanı
from  nltk.stem import PorterStemmer # steemming için fonksiyon

# porter stemmer nesnesini olustue
stemmer = PorterStemmer()
words = ["running", "runner","ran","runs","better","go","went"]

# Kelimelerin stemlerini buluyoruz, bunu yapattrken de porter stemmerin stem()kullanıyoruz
stems = [stemmer.stem(w)  for w in words]
print(f"Stems:{stems}")


# Lemmatization

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
words = ["running", "runner","ran","runs","better","go","went"]
lemmas = [lemmatizer.lemmatize(w) for w in words]
print(f"Lemmas:{lemmas}")
