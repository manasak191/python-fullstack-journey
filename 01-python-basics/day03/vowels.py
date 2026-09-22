s=input("enter string:").lower()
count=0
for char in s:
    if char in "aeiou":
        count+=1
print(count)