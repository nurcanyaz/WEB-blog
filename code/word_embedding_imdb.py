# import libraries 
import pandas as pd
import matplotlib.pyplot as plt
import re

from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

from gensim.models import Word2Vec
from gensim.utils import simple_preprocess

# load dataset
df = pd.read_csc("C:\Users\yaznu\natural-language-processing\dataset\IMDB Dataset.csv")

documents = df["review"]

# mmetin temizleme
def clean_text(text):
    text = text.lower()
    text = re.sub(r"\d+","",text)
    text = re.sub(r"[^\ws]","",text)
    text = " ".join([word for word in text.split() if len(word) >2])

    return text


clean_text("ASDAS 1551 ½$  ImerhabA")
cleaned_documents = [clean_text(doc) for doc in documents]

# text tokenization
tokenized_documents = [simple_preprocess(doc)  for doc in cleaned_documents]