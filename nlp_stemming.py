'''
This programs is for stemming of text data
'''
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python", "pythoning", "pythoner", "pythoned", "pythonly"]

for w in example_words:
    print(ps.stem(w))

new_text = "It is very import to be pythonly write you are pythoning with python. All pythoners have pythoned poorly at least once."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
