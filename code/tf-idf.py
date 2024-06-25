#import libraries
import pandas as pd
import numpy as numpy
from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "Kopek çok tatlı bir hayvandır."
    "Kopek ve kuslar cok tatlı hayvanlardır."
    "İnekler süt üretirler."
]

# Vektörleri tanımla
tfidf_vectorizer = TfidfVectorizer()

# Metinleri sayısal hale cevir
X = tfidf_vectorizer.fit_transform(documents)

# Kelime kümesi
feature_names = tfidf_vectorizer.get_feature_names_out()

# Vektor temsili
vektor_temsili = X.toarray()
print(f"tf-idf: {vektor_temsili}")

df_tfidf = pd.DataFrame(vektor_temsili,  columns=feature_names)

# Ortlama tf-idf değeri
tf_idf = df_tfidf.mean(axis=0)