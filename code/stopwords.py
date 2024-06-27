#Stopwords
import nltk
from nltk.corpus import  stopwords

nltk.download("stopwords") # farkllı dillerdeen çok kullanılan stopwords  içeren veri seti
stop_words = set(stopwords.words("english"))
print(f"stopwords {stop_words}")

text = "There are some examples of handling stop words from some texts."
text_list = text.split()
filtered_words = [word for word in text_list if word.lower() not in stop_words]
print(f"Filtered words: {filtered_words}")
