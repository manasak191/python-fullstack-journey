# Day 1: Python Fundamentals

## What I Learned
- Variables store references to objects
- Dynamic typing: variables can change types
- Type conversion: input() returns string; use int()/float()
- Comparison operators return booleans
- String formatting with f-strings

## Key Mistakes Made
1. **Forgot type conversion on input()**
   - `age = input()` returns string "25", not integer 25
   - Fixed: `age = int(input())`

2. **Used `=` instead of `==` in comparisons**
   - `if age = 18:` causes SyntaxError
   - Fixed: `if age == 18:`

3. **Floating-point rounding**
   - `0.1 + 0.2 ≠ 0.3` in Python
   - Fixed: Use f-strings with `.2f` for formatting

## Time Complexity Notes
- **Array traversal:** O(n) where n = array length
- **Min/max:** O(n) must check every element
- **Sum:** O(n) accumulate all values