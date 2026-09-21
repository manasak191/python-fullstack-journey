def two_sum_sorted(arr, target):
    """Find two numbers that add to target in SORTED array"""
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return []  # Not found

# Test
arr = [2, 3, 5, 7, 11]
print(two_sum_sorted(arr, 10))  # [1, 3] → 3 + 7 = 10