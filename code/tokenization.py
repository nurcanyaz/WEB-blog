import nltk # natural language toolkit

nltk.download("punkt")  # metni kelime ve cüme bazında tokenlara ayırabilmek için gerekli

text = " Hello world! How are ou? Hello,hi"

# kelime tokenizasyonu: word_tokenize:mmetni kelimelere ayırır.
# noktalama işaretleri ve boşluklar ayrı birertoken olaraka elde edilecektir.
word_tokens = nltk.word_tokenize(text)

# cümle tokenizasyonu: sent_tokenize:metni cümlelere ayırır. her bircümle birer token olur.
sentence_tokens = nltk.sent_tokenize(text)
