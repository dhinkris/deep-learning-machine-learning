from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

sample = gutenberg.raw ("bible-kjv.txt")

tok = sent_tokenize(sample)

for i in tok:
    print(i)