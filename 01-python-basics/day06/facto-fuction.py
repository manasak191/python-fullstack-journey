def factorial(num):
    if num<0:
        raise ValueError("Factorial not defined for negative")
    result=1
    for i in range(1,num+1):
        result+=i
    return result
def main():
    num=int(input("enter number:"))
    result=factorial(num)
    print(f"{num}!={result}")
if __name__=="__main__":
    main()
          
