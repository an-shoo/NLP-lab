# Lab 10: Extract Twitter handles and plot top word frequencies
import re
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

text = """
Tech giants are active on Twitter. Follow: https://twitter.com/google,
https://twitter.com/microsoft and https://twitter.com/openai.
To stay updated, visit https://www.github.com or engage in discussion at
https://twitter.com/AI_research_news.
Microsoft collaborates with OpenAI and Google on AI research.
"""

# 1. Extract Twitter Handles
pattern = r'https://twitter\.com/([a-zA-Z0-9_]+)'
twitter_handles = re.findall(pattern, text)
print("Extracted Twitter Handles:")
print(twitter_handles)

# 2. Clean text: remove punctuation and stopwords
cleaned_text = text.translate(str.maketrans("", "", string.punctuation)).lower()
words = cleaned_text.split()

stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word not in stop_words]

# 3. Count the most common words
word_frequency = Counter(filtered_words)
print("\nWord Frequency:")
print(word_frequency)

# 4. Plot the graph
most_common = word_frequency.most_common(10)
words_list, frequency_list = zip(*most_common)

plt.figure(figsize=(10, 5))
plt.bar(words_list, frequency_list)
plt.xticks(rotation=45)
plt.title("Most Frequently Occurring Words (Without Stopwords)")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()
