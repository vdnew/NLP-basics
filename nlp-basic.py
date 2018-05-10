'''
This program is simple showing what is word and sentance tokenizer by using example_text
'''
from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello Mr. Dasadiya, how are you doing today? The wather is great and python is awesome. The sky is pinkish-blue. You should not eat cardboard."

print(sent_tokenize(example_text))

print(word_tokenize(example_text))

#for i in word_tokenize(example_text):
    print(i)

