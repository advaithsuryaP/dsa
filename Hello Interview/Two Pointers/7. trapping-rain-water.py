'''
Problem: 
Write a function to calculate the total amount of water trapped between bars on an elevation map, where each bar's width is 1. 
The input is given as an array of n non-negative integers height representing the height of each bar.

Example: 
Input: height = [3, 4, 1, 2, 2, 5, 1, 0, 2]
Output: 10

'''

from typing import List
def trapping_rain_water(height: List[int]) -> int:
    # Approach 1: 1 For Loop, 2 while loops
    # result: int = 0
    # left: int = 0
    # right: int = 0

    # for index in range(len(height)):
    #     print("-----------------------")
    #     print(f"Iteration for height[{index}]: {height[index]}")
    #     if index == 0: continue
        
    #     max_left_height: int = 0 
    #     max_right_height: int = 0
    #     right = index

    #     while left < index:
    #         if height[left] > max_left_height:
    #             max_left_height = height[left]
    #         else:
    #             left += 1
            
    #     if height[index] > max_left_height: continue
        
    #     while right < len(height):
    #         if height[right] > max_right_height:
    #             max_right_height += 1
    #         else: right += 1
        

    #     no_of_water_blocks: int = min(max_left_height, max_right_height) - height[index]
    #     print(f"Adding {no_of_water_blocks} to the result")
    #     result += no_of_water_blocks
    #     left = 0

    # return result


    # Approach 2: 1 For Loop. Either 1 while to compute the max_left or 1 while to compute the max_right
    # result: int = 0
    # right: int = 0
    # print(height)

    # max_left_height: int = 0
    # for index in range(1, len(height) - 1):
    #     print("-----------------------")
    #     print(f"Iteration for height[{index}]: {height[index]}")

    #     max_left_height = max(height[index-1], max_left_height)
    #     print(f"Max Left height: {max_left_height}")
        
    #     if height[index] > max_left_height:
    #         print(f"Current Index cannot hold water as height at the left is less than the current")
    #         continue


    #     right = index + 1
    #     max_right_height: int = height[index]
    #     while right < len(height):
    #         if height[right] > max_right_height:
    #             max_right_height = height[right]
    #         else: right += 1

    #     print(f"Max Right Height: {max_right_height}")
    #     if height[index] > max_right_height:
    #         print(f"Current Index cannot hold water as height at the right is less than q the current")
    #         continue

    #     no_of_water_blocks: int = min(max_left_height, max_right_height) - height[index]
    #     print(f"Adding {no_of_water_blocks} to the result")
    #     result += no_of_water_blocks

    # return result

    # Approach 3: The two-pointer solution
    result: int = 0
    left: int = 0
    right: int = len(height) - 1
    
    max_left_height: int = 0
    max_right_height: int = height[right]

    while left < right:
        if height[left] <= height[right]:
            max_left_height = max(max_left_height, height[left])
            result += max_left_height - height[left]
            left += 1
        else:
            max_right_height = max(max_right_height, height[right])
            result += max_right_height - height[right]
            right -= 1
            
    return result

print(trapping_rain_water([3, 4, 1, 2, 2, 5, 1, 0, 2])) # 10

"""
TRAPPING RAIN WATER — FINAL NOTES TO FUTURE ME
==============================================

This problem took me 2 days. That is NOT a failure.
This problem is hard because it breaks the instinct of
"compute per index".

--------------------------------------------------
THE TRUE DEFINITION (BRUTE FORCE)
--------------------------------------------------
For each index i:
    water[i] = min(max_left_from_i, max_right_from_i) - height[i]

This is correct physics.
But computing max_left and max_right PER index is O(n²).

--------------------------------------------------
WHY THE TWO-POINTER SOLUTION EXISTS
--------------------------------------------------
The key realization is NOT about computing water per index.
It is about deciding WHEN an index’s water level is finalized.

Water is always limited by the SHORTER boundary.

--------------------------------------------------
CRITICAL INVARIANT
--------------------------------------------------
We maintain:
    left pointer
    right pointer
    left_max  = max height seen so far from the left
    right_max = max height seen so far from the right

At every step:
    We process the side whose current height is smaller.

WHY?
Because the smaller side is the bottleneck.
The opposite side is already guaranteed to be tall enough.

--------------------------------------------------
WHAT "PROCESSING A SIDE" MEANS
--------------------------------------------------
Processing a side means:
    - The limiting boundary for that index is finalized
    - We can safely add trapped water
    - We move that pointer inward

We do NOT process indices arbitrarily.
We process boundaries when they become safe.

--------------------------------------------------
THE TWO CASES (THIS IS THE ENTIRE ALGORITHM)
--------------------------------------------------
While left < right:

1) If height[left] <= height[right]:
       left_max = max(left_max, height[left])
       water += left_max - height[left]
       left += 1

   Reason:
       right side is guaranteed >= height[left]
       left_max determines water level

2) Else:
       right_max = max(right_max, height[right])
       water += right_max - height[right]
       right -= 1

   Reason:
       left side is guaranteed >= height[right]
       right_max determines water level

--------------------------------------------------
WHAT I KEPT GETTING WRONG INITIALLY
--------------------------------------------------
- Thinking I must compute BOTH max_left and max_right for each index
- Treating height[right] as the boundary instead of right_max
- Thinking pointer comparison decides IF water exists
  (it only decides WHICH SIDE is safe to process)

--------------------------------------------------
FINAL MENTAL MODEL
--------------------------------------------------
We never guess future heights.
We only process a side when its opposite boundary is guaranteed.

Symmetric formula.
Asymmetric execution.

--------------------------------------------------
WHY THIS IS THE HARDEST TWO-POINTER PROBLEM
--------------------------------------------------
Because it requires trusting an invariant
instead of computing explicit values per index.

Once this clicks, all other two-pointer problems feel easier.
"""
