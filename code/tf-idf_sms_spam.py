#import library

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# load dataset
df = pd.read_csv("C:\Users\yaznu\natural-language-processing\dataset\sms_spam.csv")

# tfidf


vectorizer= TfidfVectorizer()
X = vectorizer.fit_transform(df.text)

feature_names = vectorizer.get_feature_names_out()
tfidf_score = X.mean(axis=0).A1

df_tfidf = pd.DataFrame({"word":feature_names, "tfidf_score": tfidf_score})

df_tfidf_sorted = df_tfidf.sort_values(by="tfidf_score",ascending=False)
print(df_tfidf_sorted.head(10))