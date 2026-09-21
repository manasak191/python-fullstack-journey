n=int(input("enter number:"))
if n<0:
    print("please enter the valid number.")
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
print(f"factorial of {n} is :{fact}")