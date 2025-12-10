# Lab 1: Extract data from text files using Python regular expressions
import re

# Step 1: Read the text from file
with open("Lab 1a.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Step 2: Define regex patterns
patterns = {
    "Email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "Phone": r"\b\d{10}\b",
    "URL": r"https?://[^\s]+",
    "Date": r"\b\d{2}/\d{2}/\d{4}\b",
    "IP Address": r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
}

# Step 3: Extract and print matches
for label, pattern in patterns.items():
    matches = re.findall(pattern, text)
    print(f"{label}s found:")
    for match in matches:
        print(" →", match)
    print()
