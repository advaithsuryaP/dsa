'''
Problem: 
Given an integer array nums, write a function to rearrange the array by moving all zeros to the end while keeping the order of non-zero elements unchanged. 
Perform this operation in-place without creating a copy of the array.

Input: nums = [2,0,4,0,9]
Output: [2,4,9,0,0]
'''
from typing import List
def move_zeroes(nums: List[int]) -> List[int]:
    if 0 not in nums:
        return nums

    # Approach 1: This works, but O(n^2) due to internal shifts caused by remove
    # left: int = 0
    # right = len(nums) - 1
    # while left < right:
    #     print(f"Left: {left} and Right: {right}")
    #     if nums[left] != 0:
    #         print(f"Value at nums[{left}]: {nums[left]}. So incrementing left + 1")
    #         left += 1
    #     else:
    #         nums.append(0)
    #         nums.remove(nums[left])
    #         print(f"Found 0 at nums[{left}]. Adjusted nums: {nums}")
    #         right -= 1
    # return nums

    # Approach 2: The actual solution
    # slow: int = 0
    # fast: int = 0

    # while fast < len(nums):
    #     if nums[fast] == 0:
    #         fast += 1
    #     else:
    #         nums[fast], nums[slow] = nums[slow], nums[fast]
    #         fast += 1
    #         slow += 1
    # return nums

    # Approach 3: Highly optimized (relying on a for loop to keep things simple), but same concept
    next_non_zero: int = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap
            nums[i], nums[next_non_zero] = nums[next_non_zero], nums[i]
            next_non_zero += 1

    return nums
    

print(move_zeroes([2,0,4,0,9])) # [2,4,9,0,0]


"""
PROBLEM
-------
Move all zeros in the array to the end while preserving the relative order
of non-zero elements. The operation must be done in-place.

Example:
[2, 0, 4, 0, 9] → [2, 4, 9, 0, 0]


NAIVE / FIRST-THOUGHT APPROACH (WORKS BUT NOT OPTIMAL)
-----------------------------------------------------
Idea:
- Iterate through the array
- Whenever a zero is found:
    - Remove it
    - Append it to the end

Why it works:
- Order of non-zero elements is preserved
- Zeros eventually accumulate at the end

Why it is NOT optimal:
- remove() is O(n) because it shifts elements
- append() mutates array length repeatedly
- Worst case (many zeros): O(n²) time

Key lesson:
Passing test cases does NOT imply optimality.
Avoid repeated shifting inside loops.


OPTIMAL APPROACH — SLOW / FAST POINTER (STABLE COMPACTION)
----------------------------------------------------------
Core idea:
"I want to compact all non-zero values to the front, in order."

This is NOT a left-right pointer problem.
It is a slow-fast pointer problem.

Pointer roles:
- fast pointer:
    - Scans every element exactly once
    - Decides whether an element is useful (non-zero)
- slow pointer:
    - Marks the position where the next non-zero should be placed

Invariant:
- All indices < slow contain non-zero values in correct relative order
- All indices >= fast are unexplored
- Zeros naturally get pushed to the right as swaps occur

Algorithm:
1. Initialize slow = 0
2. Loop fast from 0 → end of array
3. If nums[fast] == 0:
       - Ignore it
       - Move fast only
4. If nums[fast] != 0:
       - Swap nums[slow] and nums[fast]
       - Increment both slow and fast

Why this works:
- Each element is visited once → O(n)
- Each swap places a non-zero in its final correct position
- Relative order of non-zero elements is preserved
- No extra space is used

Complexity:
- Time: O(n)
- Space: O(1)

Mental model to remember:
"Scan everything once. Write non-zeros forward as you find them.
Zeros are just the absence of useful data."
"""
