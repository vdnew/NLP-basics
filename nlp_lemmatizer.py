from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("friends"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("programs"))
print(lemmatizer.lemmatize("movies"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run", pos="v"))
