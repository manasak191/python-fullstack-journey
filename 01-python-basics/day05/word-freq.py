#using dictionary

text = input("Enter text: ").lower().split()
freq = {}
for word in text:
    freq[word] = freq.get(word, 0) + 1

for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(f"{word}: {count}")