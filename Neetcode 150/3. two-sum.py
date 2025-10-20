'''
@Link: https://neetcode.io/problems/two-integer-sum?list=neetcode150
@difficulty: Easy

Problem Statement:
    Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

Assumption: 
    You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Example 1:
Input: nums = [3,4,5,6], target = 7
Output: [0,1]

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]

Solution: A bit unorthodox but it is efficient and effective.
    - We iterate through the array and for each element, we calculate the required value. Required value is the target minus the current element.
    - We then search for the required value in the rest of the array.
    - If we find the required value, we return the indices of the current element and the required value.
    - If we don't find the required value, we return an empty list.

    But the caveat is that we need to make sure that we don't use the same element twice.
    - So we set the current element to None and then search for the required value in the rest of the array.
    - If we find the required value, we return the indices of the current element and the required value.
'''

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            current = nums[i]
            required = target-current
            
            search_area = nums[0:i]+nums[i+1:]
            if required in search_area:
                new_nums = nums
                new_nums[i] = None
                new_index = new_nums.index(required)
                return [i, new_index]
        return []
