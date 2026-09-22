s=input("enter string:")
character={}
for char in s:
    if char in character:
        character[char]+=1
    else:
        character[char]=1
        
print(character)