def frequency(s):
    freq={}
    for char in s:
        if char in freq:
            freq[char] +=1
        else:
            freq[char]=1
    return freq
s="Hello Manasa"
print(frequency(s))