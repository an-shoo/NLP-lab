# Lab 11: Morphological analysis (lemmatization based on POS)
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

text = ("The cats are running quickly while the dogs were happily "
        "playing in the garden.")

lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

words = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(words)

lemmatized_words = [
    lemmatizer.lemmatize(word, get_wordnet_pos(tag))
    for word, tag in pos_tags
]

print("\nOriginal Text:")
print(text)
print("\nPOS Tags:")
print(pos_tags)
print("\nLemmatized Text (POS-Based):")
print(" ".join(lemmatized_words))
