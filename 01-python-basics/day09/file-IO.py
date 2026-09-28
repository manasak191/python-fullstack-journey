# Reading file
with open("data.txt", 'r') as f:  # 'r' = read
    content = f.read()  # Read entire file
    lines = f.readlines()  # Read as list of lines

# Writing file
with open("output.txt", 'w') as f:  # 'w' = write (overwrite)
    f.write("Hello World\n")
    f.writelines(["Line 1\n", "Line 2\n"])

# Appending file
with open("log.txt", 'a') as f:  # 'a' = append
    f.write("New entry\n")

# JSON (structured data)
import json
data = {"name": "Manasa", "age": 25}
with open("data.json", 'w') as f:
    json.dump(data, f, indent=2)  # Write JSON
with open("data.json", 'r') as f:
    loaded = json.load(f)  # Read JSON