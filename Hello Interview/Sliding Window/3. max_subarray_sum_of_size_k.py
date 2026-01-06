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
    result = float('-inf')

    left: int = 0

    window_sum: int = 0
    for right in range(len(nums)):
        window_sum += nums[right]

        if (right - left) + 1 == k:
            result = max(result, window_sum)   

            window_sum -= nums[left]
            left += 1

    return result

            



print(max_subarray_sum_of_size_k([2, 1, 5, 1, 3, 2], 3)) # 9