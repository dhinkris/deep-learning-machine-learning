from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example = "This is an example showing off stop word filtration. and"

stopwords = set(stopwords.words("english"))

print(stopwords)
words = word_tokenize(example)
#
# filtered_sentence = []
#
# for w in words:
#     if w not in stopwords:
#         filtered_sentence.append(w)
#
# print(filtered_sentence)

filtered_sentence = [w for w in words if not w in stopwords]

print(filtered_sentence)