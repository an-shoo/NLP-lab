# Lab 7: N-Gram Language Model with Stopword Removal for Next-Word Prediction
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

text = """
Natural Language Processing, or NLP, enables computers to understand human 
language,
human language patterns, and human language meaning. It helps in automating tasks
like translation, translation of languages, sentiment analysis,
and sentiment analysis of texts, as well as chatbots and chatbots interactions.
"""

tokens = word_tokenize(text.lower())

stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens
                   if word.isalpha() and word not in stop_words]
print(f"Filtered Tokens:\n{filtered_tokens}\n")

n = 2
ngrams_list = list(nltk.ngrams(filtered_tokens, n))

ngram_freq = Counter(ngrams_list)
print("N-Gram Frequencies:")
for gram, freq in ngram_freq.items():
    print(f"{gram}: {freq}")

def predict_next_word(context_word):
    candidates = {
        gram[1]: freq
        for gram, freq in ngram_freq.items()
        if gram[0] == context_word
    }
    if not candidates:
        return "No prediction available"
    return max(candidates, key=candidates.get)

context = 'human'
predicted = predict_next_word(context)
print(f"\nGiven the word '{context}', the predicted next word is: '{predicted}'")
