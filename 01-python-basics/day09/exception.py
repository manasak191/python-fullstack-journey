try:
    num = int(input("Enter number: "))  # Might raise ValueError
    result = 10 / num  # Might raise ZeroDivisionError
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:  # Catch-all (not recommended in production)
    print(f"Unexpected error: {e}")
else:
    print(f"Result: {result}")  # Runs only if no exception
finally:
    print("Cleanup code here")  # Always runs (files, connections, etc.)