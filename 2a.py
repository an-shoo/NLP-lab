# Lab 5: Split string into words and separators using regex
import re

text = "I like apples, bananas and mangoes, grapes too"

tokens = re.split(r'([, ])', text)
print(tokens)

words = [t for t in tokens if t.strip() and t not in [',', ' ']]
separators = [t for t in tokens if t in [',', ' ']]

print("Original text:", text)
print("Words:", words)
print("Separators:", separators)
