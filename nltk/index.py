from nltk.tokenize import sent_tokenize, word_tokenize
# tokenizing - word tokenizers, sentence tokenizers
# lexicon and corporas
# corpora - body of text. ex: medical journals, presidential speeches, English language
# lexicon - words and their means

# investor - speak ... regular english-speak
# investor speak 'bull'= someone who is positive about the market
# english-speak 'bull'= animal

example_text = "hellow Mr. Smith, how are you doing today? The weather is great and Python is awesome. The sky is pinkish blue."
print(sent_tokenize(example_text))
print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)