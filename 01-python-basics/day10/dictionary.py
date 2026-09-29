# Dict
user = {"name": "Manasa", "age": 21}
print(user["name"])  # Manasa

# Set
unique_ids = {1, 2, 3, 2, 1}  # {1, 2, 3} - duplicates removed
if 1 in unique_ids:  # O(1) lookup
    print("Found")