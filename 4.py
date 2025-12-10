# Lab 4: Plot the most frequently distributed words in text
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
#%matplotlib inline comment out if in jupyter

text = """
Natural Language Processing is a part of Artificial Intelligence.
It deals with the interaction between computers and humans
using natural language.
"""

# Step 1: Tokenize text
tokens = word_tokenize(text.lower())

# Step 2: Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if w.isalpha() and w not in stop_words]

# Step 3: Count word frequencies
word_freq = Counter(filtered_tokens)

# Get the most common words (top 5)
most_common_words = word_freq.most_common(5)
words, freqs = zip(*most_common_words)

print(words)
print(freqs)

# Step 4: Plot bar graph
plt.bar(words, freqs)
plt.title("Most Frequent Words in Text")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()
