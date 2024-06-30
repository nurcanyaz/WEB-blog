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

# word2vec modeli tanımla
model = Word2Vec(sentences=tokenized_documents, vector_size=50, window=5, min_count=1, sg=0)
word_vectors = model.wv

words = list(word_vectors.index_to_key)[:500]
vectors = [word_vectors[word] for word in words]

#clustering kmeans k=2
kmeans = KMeans(n_clusters=2)
kmeans.fit(vectors)
clusters = kmeans.labels_

# PCA
pca = PCA(n_components=2)
reduced_vectors = pca.fit_transform(vectors)

plt.figure()
plt.scatter(reduced_vectors[:,0],reduced_vectors[:,1], c= clusters, cmap="viridis")

centers = pca.transform(kmeans.cluster_centers_)
plt.scatter(centers[:,0], centers[:,1], c ="red", marker = "x", s=150, label = "Center")
plt.legend()

# figur üzerine kelmelerin eklenmesi
for i, word in enumerate(words):
    plt.text(reduced_vectors[i,0], reduced_vectors[i,1],word, fontsize=7)
plt.title("Word2vec")