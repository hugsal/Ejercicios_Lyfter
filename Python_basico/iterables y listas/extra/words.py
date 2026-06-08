long_words = []

for i in range(5):
    word = input("Enter a word:")
    if len(word) > 4:
        long_words.append(word)

print(long_words)