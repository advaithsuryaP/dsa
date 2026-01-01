'''
Problem: 
Write a function to sort a given integer array nums in-place (and without the built-in sort function), 
where the array contains n integers that are either 0, 1, and 2 and represent the colors red, white, and blue. 
Arrange the objects so that same-colored ones are adjacent, in the order of red, white, and blue (0, 1, 2).

Input: 
nums = [2,1,2,0,1,0,1,0,1]

Output: [0,0,0,1,1,1,1,2,2]

@refer: https://www.hellointerview.com/learn/code/two-pointers/sort-colors
'''
from typing import List
def sort_colors(nums: List[int]) -> List[int]:
    # Approach 1: Which follows a similar pattern to the previous problem with 2 passes. But this can be done with 3 passes with 3 pointers
    # swap_position: int = 0
    # for index in range(len(nums)):
    #     if nums[index] == 0:
    #         nums[index], nums[swap_position] = nums[swap_position], nums[index]
    #         swap_position += 1


    # for index in range(swap_position, len(nums)):
    #     if(nums[index] == 1):
    #         nums[index], nums[swap_position] = nums[swap_position], nums[index]
    #         swap_position += 1

    # return nums

    # Approach 2: This is incorrect, looks like it's correct, but has a bug in the last swap variants. 
    # zero_swap_position: int = 0
    # two_swap_position: int = len(nums) - 1

    # for index in range(len(nums)):
    #     print("--------------------------")
    #     print(f"Index: {index} | Value: {nums[index]} | nums: {nums}")
    #     if nums[index] == 0 and nums[zero_swap_position] != 0:
    #         nums[index], nums[zero_swap_position] = nums[zero_swap_position], nums[index]
    #         print(f"Swapping nums[{index}]({nums[index]}) <-> nums[{zero_swap_position}]({nums[zero_swap_position]}) | Zero Swap Position: {zero_swap_position}({nums[zero_swap_position]}])")
    #         zero_swap_position += 1
            
        
    #     if nums[index] == 2 and index < two_swap_position:
    #         nums[index], nums[two_swap_position] = nums[two_swap_position], nums[index]
    #         print(f"Swapping nums[{index}]({nums[index]}) <-> nums[{two_swap_position}]({nums[two_swap_position]}) | Two Swap Position: {two_swap_position}({nums[two_swap_position]})")
    #         two_swap_position -= 1
    
    # return nums

    low: int = 0
    current: int = 0
    high: int = len(nums) - 1

    while current <= high:
        if nums[current] == 0:
            nums[current], nums[low] = nums[low], nums[current]
            current += 1
            low += 1
        elif nums[current] == 2:
            nums[current], nums[high] = nums[high], nums[current]
            high -= 1
        else: current += 1

    return nums

print(sort_colors([2,1,2,0,1,0,1,0,1])) # [0,0,0,1,1,1,1,2,2]

"""
PROBLEM
-------
Sort an array containing only 0s, 1s, and 2s in-place such that:
- All 0s come first
- Then all 1s
- Then all 2s
- No built-in sort
- O(1) extra space

This is the classic "Dutch National Flag" problem.


MY LEARNING JOURNEY
-------------------

I initially approached this problem by reusing a pattern I had just learned:
- Stable compaction using two pointers
- Multiple passes over the array

That approach WORKED and was correct:
1) First pass: move all 0s to the front
2) Second pass: move all 1s after the 0s
3) 2s naturally end up at the end

This solution:
- Is O(n)
- Is in-place
- Is correct

BUT — this problem is not just about correctness.
It is specifically designed to test whether I understand how to maintain
MULTIPLE REGIONS SIMULTANEOUSLY during a SINGLE PASS.


WHY MY FIRST "ONE-PASS" ATTEMPT WAS WRONG
-----------------------------------------

I tried using:
- one pointer for 0s
- one pointer for 2s
- a for-loop scanning pointer

The bug:
- I used a `for` loop
- When swapping a 2 with the end, I blindly advanced the scanning pointer

This is incorrect because:
- When swapping with the right (2-region),
  the value that comes back is UNKNOWN
- Advancing the scanning pointer skips processing that value

This mistake is subtle and very common.
The problem exists to teach exactly this rule.


THE KEY INSIGHT (THIS IS THE CORE LESSON)
-----------------------------------------

There are THREE regions in the array at all times:

    [ 0s | 1s | unknown | 2s ]

We must maintain this invariant while scanning.

This requires THREE pointers with STRICT roles:

- low     → next position where a 0 should go
- current → element currently being examined
- high    → next position where a 2 should go


THE GOLDEN RULE (MEMORIZE THIS)
-------------------------------

Swap-with-left  (0) → advance BOTH pointers
Swap-with-right (2) → advance ONLY the boundary pointer, NOT current

Why?

- After swapping with low:
    the incoming value is already processed → safe to move on

- After swapping with high:
    the incoming value is UNKNOWN → must be re-checked


FINAL CORRECT APPROACH (DUTCH NATIONAL FLAG)
--------------------------------------------

Algorithm:
1) Initialize:
    low = 0
    current = 0
    high = len(nums) - 1

2) While current <= high:
    - If nums[current] == 0:
        swap(nums[current], nums[low])
        current += 1
        low += 1

    - If nums[current] == 1:
        current += 1

    - If nums[current] == 2:
        swap(nums[current], nums[high])
        high -= 1
        (DO NOT increment current)

This guarantees:
- Single pass
- In-place
- O(n) time
- O(1) space
- Correct ordering


WHY THIS PROBLEM MATTERS
------------------------

This problem taught me that:

- "Two pointers" is NOT one pattern
- There are multiple pointer roles:
    * opposing pointers
    * slow-fast pointers
    * boundary + scanning pointers

It also taught me to think in terms of:
- invariants
- regions
- safety of pointer movement

This understanding generalizes to:
- partition problems
- multi-category grouping
- in-place rearrangements


FINAL TAKEAWAY
--------------

If I ever get confused again, remember:

    Swap left → move forward
    Swap right → re-check

That single sentence is the heart of the Dutch National Flag problem.
"""
