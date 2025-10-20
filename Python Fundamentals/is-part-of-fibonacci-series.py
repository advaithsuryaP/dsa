'''
@Link: Personal Problem
@Difficulty: Easy

Problem Statement: Check if a number is part of the Fibonacci series.
    The Fibonacci series is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.
    For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

Example 1:
Input: 5
Output: True

Example 2:
Input: 10
Output: False
'''

from math import sqrt
class Solution:
    def is_part_of_fibonacci_series(self, number: int) -> bool:
        if(number < 0): return False

        root1: float = sqrt(5*number**2 + 4)
        root2: float = sqrt(5*number**2 - 4)

        if(root1.is_integer() or root2.is_integer()): return True
        return False


solution = Solution()
print(solution.is_part_of_fibonacci_series(5)) # True
print(solution.is_part_of_fibonacci_series(10)) # False

"""
@Link: Personal Problem
@Difficulty: Easy

Problem Statement:
    Check whether a given number is part of the Fibonacci sequence.
    The Fibonacci sequence is defined as:
        F(0) = 0, F(1) = 1
        F(n) = F(n-1) + F(n-2)
    Example: 0, 1, 1, 2, 3, 5, 8, 13, ...

--------------------------------------------------
🧩 Naive Approach:
    - Generate the Fibonacci sequence iteratively until the number
      either appears or the sequence surpasses it.
    - Return True if found, else False.
    ❌ Problem: This becomes inefficient for large inputs since 
      Fibonacci numbers grow exponentially — you might need thousands 
      of iterations for big inputs.

--------------------------------------------------
💡 Key Insight:
    There’s a **mathematical characterization** of Fibonacci numbers.

    A number 'n' is a Fibonacci number if and only if:
        (5 * n² + 4)  OR  (5 * n² – 4)
    is a **perfect square**.

    This comes from Binet’s Formula and properties of the
    golden ratio (φ = (1 + √5) / 2). These relationships describe 
    Fibonacci numbers as the closest integers to:
        F(n) = (φⁿ – (1 – φ)ⁿ) / √5

    When you manipulate that formula algebraically, you find that 
    Fibonacci numbers are the only integers for which
    `5n² ± 4` yields a perfect square. Hence this elegant test.

--------------------------------------------------
⚙️ Optimized Approach:
    1. Compute `5 * n² + 4` and `5 * n² – 4`.
    2. Take square roots of both.
    3. Check if either root is an integer (using .is_integer()).
    4. If yes → 'n' is Fibonacci; else → not.

    We also handle negative numbers up front since Fibonacci
    is defined only for non-negative indices.

--------------------------------------------------
🔍 Line-by-Line "Magic":
    root1 = sqrt(5 * number**2 + 4)
    root2 = sqrt(5 * number**2 - 4)
        → These are the two "perfect-square candidates" derived
          from the Fibonacci property.

    if root1.is_integer() or root2.is_integer():
        → Checks if either candidate yields a whole square root.

--------------------------------------------------
⏱️ Complexity:
    Time:  O(1)
        - Constant-time arithmetic and sqrt operations.
    Space: O(1)
        - No extra memory used.

--------------------------------------------------
🧠 Extra Note (Why +4 and -4?):
    The ±4 ensures coverage of both branches of Binet’s quadratic 
    relationship. Depending on whether the term comes from φⁿ or 
    (1 - φ)ⁿ, the expression can align slightly above or below 
    a perfect square — hence both need checking.

--------------------------------------------------
✅ Example Runs:
    Input: 5  →  True
    Input: 10 →  False
"""
