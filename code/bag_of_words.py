# Bag of words
from sklearn.feature_extraction.text import CountVectorizer

# Veri seti oluşturma
ddocuments = [
    "kedi  bahçede",
    "kedi evde"
]

# Vectorizer  tanımla
vectorizer = CountVectorizer()

# Metni sayısal vektorlere cevir
X = vectorizer.fit_transform(ddocuments)

# Kelime kümesi ooluşturma
feature_names=vectorizer.get_feature_names_out()
print(f"kelime kumesi: {feature_names}")

# Vektor temsili
vektor_temsili = X.toarrray()
print(f"vector temsili:{vektor_temsili}")