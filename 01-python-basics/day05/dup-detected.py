nums = list(map(int, input("Enter numbers (comma-separated): ").split(',')))
seen = set()

for num in nums:
    if num in seen:
        print(f"Duplicate found: {num}")
        break
    seen.add(num)
else:
    print("No duplicates")