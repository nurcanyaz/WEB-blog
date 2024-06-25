
# Eliminate extra spaces in texts

text = "Hello,    World!     2035"

text.split()

cleaned_text1 = " ".join(text.split())
print (f"text:{text} \n cleaned_text1:{cleaned_text1}")

# Uppercase-lowercase conversion

text = "Hello,World! 2035"
cleaned_text2 = text.lower()
print(f"text:{text}\n cleaned_text2: {cleaned_text2}")

# remove punctuation
text = "Hello,World! 2035"

cleaned_text3 = text.translate(str.maketrans("","", str.punctuation))
print(f"text:{text}\n cleaned_text3: {cleaned_text3}")

#Remove special characters
import re

text = "Hello,World! 2035"
cleaned_text4 = re.sub(r"[A-Za-z0-9\s]", "", text)
print(f"text:{text}\n cleaned_text4: {cleaned_text4}")

# fix typos
from textblob import TextBlob

text = "Hellıo wirld 2035"
cleaned_text5 = TextBlob(text).correct()
print(f"text:{text}\n cleaned_text5: {cleaned_text5}")


# remove html or url tags
from bs4 import BeautifulSoup

html_text = "<div>Hello world 2035</div>"
cleaned_text6 = BeautifulSoup(html_text,"html.parser").get_text()
print(f"text:{text}\n cleaned_text6: {cleaned_text6}")
