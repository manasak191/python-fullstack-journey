# Normal function
def add(a, b):
    return a + b

# Lambda equivalent
add = lambda a, b: a + b

# Use in map/filter
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16]

# Sort by second element
data = [(1, 3), (2, 1), (3, 2)]
sorted_data = sorted(data, key=lambda x: x[1])  # [(2,1), (3,2), (1,3)]