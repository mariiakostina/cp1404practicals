"""
Word Occurrences
Estimate: 20 minutes
Actual: 20 minutes
"""

user_text = input("Text: ").lower()
words = user_text.split()

word_to_count = {}
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

sorted_words = list(word_to_count.keys())
sorted_words.sort()
max_length = max(len(word) for word in sorted_words)

for word in sorted_words:
    print(f"{word:{max_length}} : {word_to_count[word]}")


