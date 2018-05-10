import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenize

train_text = state_union.raw("")
sample_text = sate_union.raw("")

custom_sent_tokenize = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenize.tokenize(sample_text)


def process_content():
        for i in tokenized:
            words = nltk.words_tokenize(i)
            tagged = nltk.pos_tag(words)    

            chunkgram = r"""chunk: {<.*>+} }<VB.?|IN|DT|TO>+{"""
            chunkParser = nltk.RegexpParser(chunkgram)
            chunked = chunkgram.parse(tagged)

            chunked.draw()
