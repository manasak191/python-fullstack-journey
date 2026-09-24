items = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
grouped = {}

for item in items:
    if item not in grouped:
        grouped[item] = []
    grouped[item].append(item)

for item, group in grouped.items():
    print(f"{item}: {len(group)} times")