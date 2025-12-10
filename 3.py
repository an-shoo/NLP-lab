# Lab 2: Preprocessing (Tokenization, Stopword Removal and Stemming)
import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

reviews = [
    "The product is amazing and works really well!",
    "I am not happy with the service. It was too slow.",
    "Excellent quality and fast delivery. Highly recommended!",
    "The packaging was terrible and the product was damaged."
]

stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

for i, review in enumerate(reviews, start=1):
    print(f"\n=== Review {i} ===")
    print("Original:", review)

    # Tokenization
    tokens = word_tokenize(review)
    print("Tokens:", tokens)

    # Stopword Removal
    filtered_tokens = [w for w in tokens
                       if w.lower() not in stop_words and w.isalpha()]
    print("Without Stopwords:", filtered_tokens)

    # Stemming
    stemmed = [ps.stem(w) for w in filtered_tokens]
    print("Stemmed:", stemmed)
