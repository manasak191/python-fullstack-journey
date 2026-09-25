def add(*numbers):      #*args example
    total=0
    for num in numbers:
        total+=num
    return total

print(add(1,2,3,4,5,6))
print(add(8,4))