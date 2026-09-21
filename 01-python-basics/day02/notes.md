# Day 2: Conditions & Loops

## Key Learnings
- **For loops:** Use when iteration count known
- **While loops:** Use when checking condition repeatedly
- **Break:** Exit loop immediately
- **Continue:** Skip to next iteration

## Critical Mistake
Used `=` instead of `==` in while condition! 
```python
while count = 5:  # WRONG: assignment, not comparison
while count == 5: # CORRECT: comparison
```

## Complexity Analysis
- Prime check: O(√n) — only check up to √n
- Factorial: O(n) — multiply n times
- Fibonacci: O(n) — iterate n times
- Reverse number: O(log n) — digits = log₁₀(n)

## Pattern Recognition
- **Number problems** → Use % and // (modulo and integer division)
- **Palindrome check** → Reverse and compare
- **Searching** → Linear search O(n) or two-pointer O(n)