'''
Problem: 
Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.

Example:
Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 12
Explanation: The contiguous subarray [5, 1, 3] has the maximum sum of 9
'''
from typing import List
def max_subarray_sum_of_size_k(nums: List[int], k: int) -> int:
    result: float = float('-inf')

    left: int = 0

    total: int = 0
    for right in range(len(nums)):
        total += nums[right]

        print(f"Left: {left}, Right: {right}, Total: {total}")
        if right - left + 1 == k:

            result = max(result, total)

            total -= nums[left]
            left += 1
    
    return result
            

print(max_subarray_sum_of_size_k([2, 1, 5, 1, 3, 2], 3)) # 9