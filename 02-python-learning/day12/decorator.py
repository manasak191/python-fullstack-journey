def my_decorator(func):
    
    def wrapper():
        print("Something before function call")
        func()
        print("Something after function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")


say_hello()
