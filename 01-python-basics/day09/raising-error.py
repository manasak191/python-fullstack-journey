def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age < 18:
        raise ValueError("Must be 18+!")
    return "Valid age"

try:
    validate_age(-5)
except ValueError as e:
    print(f"Error: {e}")