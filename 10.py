# Lab 12: Frequency of bi-grams in a collection of 3 documents
from collections import Counter
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

doc_1 = ('Convolutional Neural Networks are very similar to ordinary Neural '
         'Networks from the previous chapter.')
doc_2 = ('Convolutional Neural Networks take advantage of the fact that the '
         'input consists of images and they constrain the architecture in a '
         'more sensible way.')
doc_3 = ('In particular, unlike a regular Neural Network, the layers of a '
         'ConvNet have neurons arranged in 3 dimensions: width, height, depth.')

documents = doc_1 + " " + doc_2 + " " + doc_3

tokens = word_tokenize(documents.lower())

filtered_tokens = [word for word in tokens
                   if word.isalpha() and word not in stop_words]

bigrams = list(ngrams(filtered_tokens, 2))

bigram_freq = Counter(bigrams)

print("Number of unique bi-grams:", len(bigram_freq))
print("\nTop 5 most common bi-grams:")
for bigram, freq in bigram_freq.most_common(5):
    print(bigram, "->", freq)
