'''
Problem: 
Write a function to sort a given integer array nums in-place (and without the built-in sort function), 
where the array contains n integers that are either 0, 1, and 2 and represent the colors red, white, and blue. 
Arrange the objects so that same-colored ones are adjacent, in the order of red, white, and blue (0, 1, 2).

Input: 
nums = [2,1,2,0,1,0,1,0,1]

Output: [0,0,0,1,1,1,1,2,2]

@refer: https://www.hellointerview.com/learn/code/two-pointers/sort-colors
'''
from typing import List
def sort_colors(nums: List[int]) -> List[int]:
    # Approach 1: Which follows a similar pattern to the previous problem with 2 passes. But this can be done with 3 passes with 3 pointers
    # swap_position: int = 0
    # for index in range(len(nums)):
    #     if nums[index] == 0:
    #         nums[index], nums[swap_position] = nums[swap_position], nums[index]
    #         swap_position += 1


    # for index in range(swap_position, len(nums)):
    #     if(nums[index] == 1):
    #         nums[index], nums[swap_position] = nums[swap_position], nums[index]
    #         swap_position += 1

    # return nums

    # Approach 2: This is incorrect, looks like it's correct, but has a bug in the last swap variants. 
    # zero_swap_position: int = 0
    # two_swap_position: int = len(nums) - 1

    # for index in range(len(nums)):
    #     print("--------------------------")
    #     print(f"Index: {index} | Value: {nums[index]} | nums: {nums}")
    #     if nums[index] == 0 and nums[zero_swap_position] != 0:
    #         nums[index], nums[zero_swap_position] = nums[zero_swap_position], nums[index]
    #         print(f"Swapping nums[{index}]({nums[index]}) <-> nums[{zero_swap_position}]({nums[zero_swap_position]}) | Zero Swap Position: {zero_swap_position}({nums[zero_swap_position]}])")
    #         zero_swap_position += 1
            
        
    #     if nums[index] == 2 and index < two_swap_position:
    #         nums[index], nums[two_swap_position] = nums[two_swap_position], nums[index]
    #         print(f"Swapping nums[{index}]({nums[index]}) <-> nums[{two_swap_position}]({nums[two_swap_position]}) | Two Swap Position: {two_swap_position}({nums[two_swap_position]})")
    #         two_swap_position -= 1
    
    # return nums

    low: int = 0
    current: int = 0
    high: int = len(nums) - 1

    while current <= high:
        if nums[current] == 0:
            nums[current], nums[low] = nums[low], nums[current]
            current += 1
            low += 1
        elif nums[current] == 2:
            nums[current], nums[high] = nums[high], nums[current]
            high -= 1
        else: current += 1

    return nums

print(sort_colors([2,1,2,0,1,0,1,0,1])) # [0,0,0,1,1,1,1,2,2]