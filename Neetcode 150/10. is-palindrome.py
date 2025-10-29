'''
Link: https://neetcode.io/problems/is-palindrome?list=neetcode150
@difficulty: Easy

Problem Statement:
    Given a string s, return true if it is a palindrome, otherwise return false.
    A palindrome is a string that reads the same forward and backward. 
    It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:
Input: s = "racecar"
Output: true

Example 2:
Input: s = "hello"
Output: false

Example 3:
Input: s = "A man, a plan, a canal: Panama"
Output: true

Example 4:
Input: s = "Was it a car or a cat I saw?"
Output: true
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Solution 1
        # normalized: list[str] = []
        # for ch in s:
        #     if(ch.isalnum()):
        #         normalized.append(ch.lower())
        # return normalized == normalized[::-1]

        # Solution 2
        normalized = [ch.lower() for ch in s if ch.isalnum()]
        return normalized == normalized[::-1]




solution = Solution()
print(solution.isPalindrome("racecar")) # true
print(solution.isPalindrome("hello")) # false
print(solution.isPalindrome("A man, a plan, a canal: Panama")) # true
print(solution.isPalindrome("Was it a car or a cat I saw?")) # true

'''
@Link: https://neetcode.io/problems/is-palindrome?list=neetcode150
@Difficulty: Easy

🧩 Problem Restatement:
Given a string `s`, return True if it is a palindrome — i.e., it reads the same 
forward and backward — ignoring case and non-alphanumeric characters.

Examples:
    "racecar" → True
    "hello" → False
    "A man, a plan, a canal: Panama" → True
    "Was it a car or a cat I saw?" → True

---

🪜 Naive Approach:
Reverse the string directly and compare → `s == s[::-1]`.
However, that fails when there are spaces, punctuation, or case differences.

---

💡 Key Insight:
We only care about **letters and digits**, and the check must be **case-insensitive**.
So before comparing, we normalize the input:
1. Convert all characters to lowercase.
2. Remove all non-alphanumeric characters.
After normalization, a direct equality check with the reversed version suffices.

---

⚙️ Optimized Approach (O(n) time, O(n) space):
- Build a filtered list of lowercase alphanumeric characters using list comprehension.
- Compare it with its reverse using slicing.

    normalized = [ch.lower() for ch in s if ch.isalnum()]
    return normalized == normalized[::-1]

This leverages Python’s slicing and comprehension for both readability and efficiency.

---

🧠 Intuition Recap:
A palindrome check boils down to symmetry.
By cleaning and lowercasing upfront, we ensure that both sides of the symmetry are comparable.
Slicing (`[::-1]`) in Python gives a reversed copy, making the comparison one clean step.

---

⏱ Complexity Analysis:
- Time:  O(n) → One pass for filtering, one for reversing, one for comparing.
- Space: O(n) → Because we store the normalized list.

---

✅ Example walkthrough:
Input: "A man, a plan, a canal: Panama"
Step 1 → normalized = ['a','m','a','n','a','p','l','a','n','a','c','a','n','a','l','p','a','n','a','m','a']
Step 2 → normalized[::-1] is identical.
Result → True
'''
