'''
Problem:

Given an input integer array nums, write a function to find all unique triplets [nums[i], nums[j], nums[k]] such that i, j, and k are distinct indices, 
and the sum of nums[i], nums[j], and nums[k] equals zero. Ensure that the resulting list does not contain any duplicate triplets.

Example:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

@refer: https://www.hellointerview.com/learn/code/two-pointers/3-sum

'''

from typing import List
def three_sum(nums: List[int], equals: int) -> List[int]: 
    result: list[int] = []
    
    nums.sort()

    for index in range(len(nums)):
        k: int = nums[index]

        if index > 0 and k == nums[index - 1]: continue
        
        if k > 0: continue

        target: int = equals - k 

        left: int = index + 1 
        right: int = len(nums) - 1


        while left < right:
            left_value: int = nums[left]
            right_value: int = nums[right]
            
            calculated_sum: int = left_value + right_value

            if calculated_sum == target:
                result.append([k, nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]: left += 1
                while left < right and nums[right] == nums[right + 1]: right -= 1
            else:
                if calculated_sum < target:
                    left += 1
                else: right -= 1

    return result
        


print(three_sum([-1, 0, 1, 2, -1, -4], 0)) # [[-1, -1, 2], [-1, 0, 1]]
print(three_sum([-1,0,1,2,-1,-1], 0)) # [[-1,-1,2],[-1,0,1]]

