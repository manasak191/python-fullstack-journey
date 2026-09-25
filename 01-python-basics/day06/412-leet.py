def fizz_buzz(n):
    result=[]
    for i in range(1,n+1):
        if i%3==0:
            result.append("Fizz")
        elif i%5==0:
            result.append("Buzz")
        elif i%15==0:
            result.append("FizzBuzz")
        else:
            result.append(str(i))
    return result

n=int(input("enter number:"))
print(fizz_buzz(n))