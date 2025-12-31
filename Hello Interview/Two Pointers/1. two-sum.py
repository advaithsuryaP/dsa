'''
Problem:
Given an array of integers nums and an integer target, determine if there are two numbers in the array that add up to target.

Example:
Input: nums = [1,3,4,6,8,10,13], target = 13
Output: True (3 + 10 = 13)
Input: nums = [1,3,4,6,8,10,13], target = 6
Output: False

@refer: https://www.hellointerview.com/learn/code/two-pointers/overview
'''

from typing import List
def twoSum(nums: List[int], target) -> bool:
    nums.sort()
    
    left: int = 0
    right: int = len(nums) - 1

    while left < right:
        calculated_sum: int = nums[left] + nums[right]
        if calculated_sum == target:
            return True
        
        if calculated_sum < target:
            left += 1
        else:
            right -= 1
    return False
        


print(twoSum([1,3,4,6,8,10,13], 13)) # True
print(twoSum([1,3,4,6,8,10,13], 6)) # False


