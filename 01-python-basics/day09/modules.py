# Create math_utils.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Use in main.py
from math_utils import add, multiply

result = add(3, 5)  # 8
product = multiply(3, 5)  # 15

# Or import entire module
import math_utils
result = math_utils.add(3, 5)