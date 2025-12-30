'''
Problem:
Given an array of integers nums and an integer target, determine if there are two numbers in the array that add up to target.

Example:
Input: nums = [1,3,4,6,8,10,13], target = 13
Output: True (3 + 10 = 13)
Input: nums = [1,3,4,6,8,10,13], target = 6
Output: False
'''

from typing import List
def twoSum(nums: List[int], target) -> bool:
    nums.sort()
    
    i: int = 0
    j: int = len(nums) - 1

    while( i is not j ):
        calculated_sum: int = nums[i] + nums[j]
        if calculated_sum > target:
            j -= 1
        if calculated_sum < target:
            i += 1
        if calculated_sum == target:
            return True
    else: return False
        


print(twoSum([1,3,4,6,8,10,13], 13)) # True
print(twoSum([1,3,4,6,8,10,13], 6)) # False

