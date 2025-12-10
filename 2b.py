# Lab 6: Extract all numbers in a file and compute their sum
import re

def extract_and_sum(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    # Find all integers
    numbers = re.findall(r'\d+', text)
    numbers = list(map(int, numbers))

    print("Numbers found:", numbers)
    print("Sum of numbers:", sum(numbers))

# Demo file
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("There are 12 apples, 25 mangoes, and 100 bananas in 2025.")

extract_and_sum("sample.txt")
