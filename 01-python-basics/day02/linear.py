def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found at index i
    return -1  # Not found

# Test
numbers = [10, 20, 30, 40, 50]
print(linear_search(numbers, 30))  # 2
print(linear_search(numbers, 99))  # -1