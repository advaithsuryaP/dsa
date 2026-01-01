'''
Problem:
Write a function to count the number of triplets in an integer array nums that could form the sides of a triangle. 
For three sides to form a valid triangle, the sum of any two sides must be greater than the third side. The triplets do not need to be unique.

Example:
Input: nums = [11,4,9,6,15,18]
Output: 10

The valid triplets are:
4, 15, 18
6, 15, 18
9, 15, 18
11, 15, 18
9, 11, 18
6, 11, 15
9, 11, 15
4, 6, 9 

@refer: https://www.hellointerview.com/learn/code/two-pointers/valid-triangle-number

'''
from typing import List
def triangle_numbers(nums: List[int]) -> int:
    result: int = 0

    nums.sort()

    for index in range(len(nums) - 1, 1, -1):
        k: int = nums[index]

        left: int = 0
        right: int = index - 1

        while left < right:
            condition: bool = nums[left] + nums[right] > k

            if condition:
                result += right - left
                right -= 1
            else: left += 1
    
    return result

        

print(triangle_numbers([11,4,9,6,15,18])) # 10

'''
PROBLEM
-------
Given an integer array nums, count the number of triplets that can form
a valid triangle.

Triangle condition:
For sides a ≤ b ≤ c, a + b > c


NAIVE APPROACH
--------------
Try all triplets (i, j, k) and check triangle inequality.
Time: O(n³)
Correct but too slow.


KEY INSIGHT
-----------
After sorting the array:
- Only one condition matters: a + b > c
- The largest side must be fixed
- If the smallest possible pair works, all larger pairs work too

This turns enumeration into counting.


OPTIMIZED APPROACH (Two Pointers)
---------------------------------
1. Sort the array.
2. Fix the largest side k from right to left.
3. Use two pointers on the left subarray:
   - left = 0
   - right = k_index - 1
4. While left < right:
   - If nums[left] + nums[right] > k:
       - All pairs from left..right-1 with this right are valid
       - Add (right - left) to the count
       - Decrement right
   - Else:
       - Increment left


WHY `right - left` WORKS
------------------------
Because the array is sorted:
If nums[left] + nums[right] > k,
then nums[left+1] + nums[right],
nums[left+2] + nums[right], ... also > k.

So we count a whole range at once instead of enumerating.


COMPLEXITY
----------
Time:  O(n²)
Space: O(1) extra


MENTAL MODEL
------------
Fix the largest side.
If the smallest possible pair works,
everything between also works — count them and move inward.
'''