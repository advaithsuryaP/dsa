'''
@Link: https://neetcode.io/problems/duplicate-integer?list=neetcode150
@difficulty: Easy

Solution:
An array contains duplicates if the length of the array is not equal to the length of the set of the array.
'''

from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

solution = Solution()
print(solution.hasDuplicate([1,2,3,1]))
print(solution.hasDuplicate([1,2,3,4]))
print(solution.hasDuplicate([1,1,1,3,3,4,3,2,4,2]))





