'''
Punkt Tokenizer is the unsupervised machine learning tokenizer
'''
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


train_text = state_union.raw()
sample_text = state_union.raw()

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized[:5]:
            words - nltk.word_tokenize(i)
            tagged = nltk,pos_tag(words)
            print(tagged)

    except Exception as r:
        print(str(e))


process_content()
