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
            left += 1
        else: 
            right -= 1

        if area > result:
            result = area

        # result = max(result, area) The above if condition can also be summarized like this

    return result


print(max_area([3, 4, 1, 2, 2, 4, 1, 3, 2])) # 21
print(max_area([1, 2, 1])) # 2

'''
PROBLEM
-------
Given an array of heights where each value represents a vertical wall,
choose two walls that can hold the maximum amount of water.

Water held = width × height
- width = distance between the two indices
- height = min(height[left], height[right]) because water overflows at the shorter wall

Goal: return the maximum possible area.


NAIVE APPROACH
--------------
Brute force:
- Try every possible pair (i, j)
- Compute area = (j - i) * min(h[i], h[j])
- Track the maximum

Time complexity: O(n²)
Space complexity: O(1)

This works, but is too slow for large inputs.


KEY INSIGHT
-----------
The width is largest when we start with the farthest two walls.
Since width can only decrease as pointers move inward,
the only way to increase area is to find a taller wall.

Critical observation:
- The area is always limited by the shorter wall.
- If we keep the shorter wall and reduce width, the area can never improve.
- Therefore, once a wall is identified as the shorter wall, it can be discarded safely.


OPTIMIZED TWO-POINTER APPROACH
------------------------------
1. Place two pointers:
   - left at index 0
   - right at index n - 1

2. Compute the area formed by these two walls.

3. Move the pointer pointing to the shorter wall:
   - Because this is the ONLY move that might increase height.
   - Moving the taller wall cannot improve area (width shrinks, height stays capped).

4. If heights are equal:
   - Move either pointer (both choices are safe).
   - No lookahead or peeking is needed.

5. Repeat until left < right.

This guarantees:
- Every discarded configuration is provably worse
- Each pointer moves at most n times


WHY THIS WORKS (THE "MAGIC")
---------------------------
If heights[left] <= heights[right]:
- Any future container using left as a wall will have:
  - Smaller width
  - Height ≤ heights[left]
- So none can beat the current area
→ Safe to move left

Same logic applies symmetrically for the right pointer.

The algorithm works by ELIMINATION, not prediction.


EDGE CASES
----------
- Equal heights → move either pointer
- Very small arrays (length < 2) → area is 0
- Heights can vary arbitrarily; sorting must NOT be used (indices matter)


COMPLEXITY
----------
Time:  O(n)  — each pointer moves once
Space: O(1)  — constant extra space


MENTAL MODEL TO REMEMBER
------------------------
"Start wide. Sacrifice width only when you can potentially gain height.
Always discard the shorter wall — it can never help you again."

'''