'''
Problem: 

Given an array heights where each element represents the height of a vertical line, pick two lines to form a container. Return the maximum area (amount of water) the container can hold.

What is area? Width × height, where width is the distance between walls, and height is the shorter wall (water overflows at the shorter wall).
heights = [3, 4, 1, 2, 2, 4, 1, 3, 2]
Output: 21 # walls at indices 0 and 7 (both height 3): width=7, height=3, area=21

heights = [1, 2, 1]
2  # walls at indices 0 and 2: width=2, height=min(1,1)=1, area=2

@refer: https://www.hellointerview.com/learn/code/two-pointers/container-with-most-water

'''
from typing import List
def max_area(heights: List[int]) -> int:
    result: int = 0

    left: int = 0
    right: int = len(heights) - 1

    while left < right:
        width: int = right - left
        left_height: int = heights[left]
        right_height: int = heights[right]
        height: int = min(left_height, right_height)
        area: int = width * height

        if left_height < right_height:
            print(f"heights[{left}]({left_height}) is less than heights[{right}]({right_height}), increasing left pointer from {left} to {left + 1}")
            left += 1
        else: 
            print(f"heights[{left}]({left_height}) is more than or equal to heights[{right}]({right_height}), decreasing right pointer from {right} to {right - 1}")
            right -= 1

        if area > result:
            result = area
            print(f"Updating result: {result}")

    return result


print(max_area([3, 4, 1, 2, 2, 4, 1, 3, 2])) # 21
print(max_area([1, 2, 1])) # 2