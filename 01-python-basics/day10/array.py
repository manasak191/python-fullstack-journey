# List
data = [1, 2.5, "text"]  # Mixed types ✓ Allowed

# Array
import array
data = array.array('i', [1, 2, 3])  # Only integers
data.append("text")  # TypeError ✗

# Array is lighter: each int = 4 bytes
# List has overhead: type info, reference count