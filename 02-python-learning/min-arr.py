arr = [10, 5, 25, 8, 15]

minimum = arr[0]

for num in arr:
    if num < minimum:
        minimum = num

print(minimum)