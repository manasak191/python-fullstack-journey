#125 leetcode
def isPalindrome(s):
    # Filter alphanumeric and convert to lowercase
    filtered = ""
    for char in s:
        if char.isalnum():  # Check if alphanumeric
            filtered += char.lower()
    
    return filtered == filtered[::-1]