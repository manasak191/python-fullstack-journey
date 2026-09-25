def is_prime(n):
    if n<2:
        return False
    for i in range(2,len(n)+1):
        if n%i==0:
            return False
        return True

def main():
    n=int(input("enter number:"))
    if is_prime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")
        
if __name__=="__main__":
    main()