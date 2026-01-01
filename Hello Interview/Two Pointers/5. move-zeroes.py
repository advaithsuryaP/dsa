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

    left: int = 0
    right = len(nums) - 1
    while left < right:
        print(f"Left: {left} and Right: {right}")
        if nums[left] != 0:
            print(f"Value at nums[{left}]: {nums[left]}. So incrementing left + 1")
            left += 1
        else:
            nums.append(0)
            nums.remove(nums[left])
            print(f"Found 0 at nums[{left}]. Adjusted nums: {nums}")
            right -= 1
    return nums

print(move_zeroes([2,0,4,0,9])) # [2,4,9,0,0]