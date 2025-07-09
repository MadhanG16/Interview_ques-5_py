# Sort texts based on number of occurrences of a word

M = int(input())
word = input().strip().lower()
texts = [input().strip() for _ in range(M)]

def count_word(text):
    return text.lower().split().count(word)

texts.sort(key=count_word)

for line in texts:
    print(line)
