'''
@Link: https://neetcode.io/problems/longest-consecutive-sequence?list=neetcode150
@difficulty: Medium

Problem Statement:
    Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
    A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
    The elements do not have to be consecutive in the original array.

    You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4]. Therefore, the length is 4.

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7
'''

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result: int = 0
        num_set: set[int] = set(nums)
        for num in nums:
            if(num - 1 not in num_set):
                streak: int = 1
                current: int = num
                while current + 1 in num_set:
                    streak += 1
                    current += 1
                if(streak > result): result = streak
        return result


solution = Solution()
print(solution.longestConsecutive([100,4,200,1,3,2])) # 4
print(solution.longestConsecutive([0,3,2,5,4,6,1,1])) # 7

"""
@Link: https://neetcode.io/problems/longest-consecutive-sequence?list=neetcode150
@difficulty: Medium

─────────────────────────────────────────────────────────────
Problem Statement:
─────────────────────────────────────────────────────────────
Given an unsorted array of integers `nums`, return the length of the longest
consecutive sequence of integers that can be formed.

A consecutive sequence means each number is exactly 1 greater than the previous.
The elements do not have to appear consecutively in the original array.

Example:
    Input:  [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest sequence is [1, 2, 3, 4].

─────────────────────────────────────────────────────────────
1️⃣ Naive Approach:
─────────────────────────────────────────────────────────────
- Sort the array → O(n log n)
- Walk through and count consecutive streaks.
- Works, but violates the O(n) requirement.

─────────────────────────────────────────────────────────────
2️⃣ Key Insight:
─────────────────────────────────────────────────────────────
We don't need sorting — just fast existence checks.

A number can only be the **start** of a sequence if there’s no predecessor:
    i.e., (num - 1) is not in the set.

That means:
- For every number, if `num - 1` not in set → start a new sequence.
- Count forward: (num + 1), (num + 2), … until a gap appears.
- Keep track of the maximum streak length.

This guarantees O(n) time since:
- Each number is inserted and looked up in O(1) via a hash set.
- Each element is visited at most once during the forward walk.

─────────────────────────────────────────────────────────────
3️⃣ Optimized Approach Reasoning:
─────────────────────────────────────────────────────────────
- Convert the list → set for O(1) lookups.
- Initialize `result` = 0.
- Iterate over every number:
    - If (num - 1) not in set → potential start of sequence.
    - Expand sequence forward using a while loop until (num + 1) not in set.
    - Track streak length.
- Update `result` accordingly.

─────────────────────────────────────────────────────────────
4️⃣ Line-by-Line Notes:
─────────────────────────────────────────────────────────────
num_set = set(nums)  
→ Avoid O(n²) list lookups. Set gives O(1) existence checks.

if (num - 1 not in num_set):  
→ This check ensures we only start from the beginning of each chain.

while current + 1 in num_set:  
→ Expands the chain forward only once per element (no rechecking).

─────────────────────────────────────────────────────────────
5️⃣ Complexity Analysis:
─────────────────────────────────────────────────────────────
Time Complexity  : O(n)
    - Each number visited at most twice (start + forward expansion).
Space Complexity : O(n)
    - For the hash set storing all elements.

─────────────────────────────────────────────────────────────
6️⃣ Example Walkthrough:
─────────────────────────────────────────────────────────────
nums = [100, 4, 200, 1, 3, 2]
num_set = {100, 4, 200, 1, 3, 2}

Iteration:
100 → start (no 99) → streak = 1
4   → skip (3 exists)
200 → start (no 199) → streak = 1
1   → start (no 0) → streak = 4 → ✅ longest
3,2 → skipped (have predecessors)

Answer = 4
─────────────────────────────────────────────────────────────
"""
