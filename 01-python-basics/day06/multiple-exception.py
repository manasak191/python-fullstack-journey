try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(a/b)
except ValueError:
    print("enter numbers only")
except ZeroDivisionError:
    print('cannot divide by zero')
    