# Lab 8: Laplace (Add-One) Smoothing
word_counts = {
    "apple": 3,
    "banana": 2,
    "cherry": 0  # 'cherry' never appeared
}

total_words = sum(word_counts.values())
vocab_size = len(word_counts)

print(f"Vocabulary Size {vocab_size}")

print("Without Laplace Smoothing:")
for word, count in word_counts.items():
    prob = count / total_words
    print(f"P({word}) = {prob:.3f}")

print("\nWith Laplace Smoothing:")
for word, count in word_counts.items():
    prob = (count + 1) / (total_words + vocab_size)
    print(f"P({word}) = {prob:.3f}")
