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