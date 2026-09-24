s = input("Enter string: ").lower()
freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1

for char in s:
    if freq[char] == 1:
        print(f"First non-repeating: {char}")
        break
else:
    print("No non-repeating character")