# Day 3: Strings + LeetCode

## Key Insights
- Strings are immutable; indexing is O(1)
- Slicing creates new string (O(n) time)
- Frequency counting is foundation for hashing
- Two-pointer is common string technique

## LeetCode 125 (Valid Palindrome)
**Approach:** Two pointers, skip non-alphanumeric
**Complexity:** O(n) time, O(1) space
**Key:** Use `isalnum()` to filter on-the-fly

## LeetCode 242 (Valid Anagram)
**Approach:** Frequency count (one hash map)
**Complexity:** O(n) time, O(26) ≈ O(1) space (only 26 letters)
**Key:** Anagram = same characters with same frequencies

## Common Mistakes
1. Forget strings are immutable—can't modify in-place
2. Off-by-one in slicing: [start:end] excludes end
3. Confuse `in` operator (checks substring) with indexing