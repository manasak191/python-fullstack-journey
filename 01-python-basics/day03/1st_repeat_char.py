s=input("enter string:")
result=[]
for char in s:
    if char not in result:
        result.append(char)
    else:
            print(char)
            break