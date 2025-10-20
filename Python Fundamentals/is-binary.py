'''
@Link: Personal Problem
@Difficulty: Easy

Problem Statement: Check if a number is an amstrong number.
    An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
    For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

Example 1:
Input: 153
Output: True

Example 2:
Input: 123
Output: False

Example 3:
Input: 9474
Output: True

'''
class Solution: 
    def is_amstrong_number(self, number: int) -> bool:
        digits = [int(ch) for ch in str(number)]
        length = len(digits)

        total = sum(d ** length for d in digits)
        return total == number

solution = Solution()
print(solution.is_amstrong_number(153))
print(solution.is_amstrong_number(123))
print(solution.is_amstrong_number(9474))
print(solution.is_amstrong_number(5))
print(solution.is_amstrong_number(0))

"""
🧩 Problem: Check if a Number is an Armstrong Number
----------------------------------------------------
An Armstrong (or narcissistic) number is a number that is equal to the sum 
of its own digits each raised to the power of the number of digits.

For example:
153 → 1³ + 5³ + 3³ = 153 → ✅ True
123 → 1³ + 2³ + 3³ = 36 → ❌ False
9474 → 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474 → ✅ True

---

🔍 Naive Approach:
1. Extract digits using modulo (% 10) and integer division (// 10).
2. Keep track of digit count `k`.
3. Compute sum(digit^k) while iterating.
4. Compare result to the original number.

Works fine but requires a few bookkeeping variables.

---

💡 Key Insight:
- Every Armstrong number is *self-descriptive* — its digits and digit count 
  together determine its structure.
- Using string conversion gives both the digits and length directly.
- Since each digit is between 0–9, exponentiation is cheap.

---

⚙️ Optimized Approach:
1. Convert number → string for easy iteration.
       digits = [int(ch) for ch in str(number)]
2. Count digits:
       k = len(digits)
3. Compute:
       total = sum(d ** k for d in digits)
4. Compare:
       return total == number

---

🧠 Why It Works:
Each digit contributes exactly its “weight” raised to the digit-count power.  
Since integer exponentiation is exact in Python, there’s no rounding or 
precision error.

Examples:
---------
153 → [1, 5, 3], len = 3 → 1³ + 5³ + 3³ = 153 → True  
9474 → [9, 4, 7, 4], len = 4 → 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474 → True

---

⏱️ Complexity Analysis:
Time  = O(k)   (k = number of digits)
Space = O(k)   (list of digits)

Both are optimal — can’t do better since every digit must be checked once.

---

🧩 Edge Cases:
✔ Single-digit numbers (0–9) → always True (since d¹ = d)
✔ 0 → True
✔ Large integers → safe, since no float precision issues
✔ Negative numbers → Typically False (definition doesn’t include negatives)

---

💬 Intuitive Takeaway:
This problem teaches **self-descriptive numeric structure** —
how a number’s composition defines its identity.  
It’s a small but elegant way to practice decomposition and mathematical reasoning.
"""


