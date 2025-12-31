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
def three_sum(nums: List[int]) -> List[int]: 
    result: list[int] = []
    
    nums.sort()

    for index in range(len(nums)):
        k: int = nums[index]

        if index > 0 and k == nums[index - 1]: continue
        
        if k > 0: continue

        target: int = -k 

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
        


print(three_sum([-1, 0, 1, 2, -1, -4])) # [[-1, -1, 2], [-1, 0, 1]]
print(three_sum([-1,0,1,2,-1,-1])) # [[-1,-1,2],[-1,0,1]]

'''
PROBLEM
-------
Given an integer array nums, find all unique triplets (i, j, k) such that:
- i, j, k are distinct indices
- nums[i] + nums[j] + nums[k] == target
- No duplicate triplets in the output


NAIVE APPROACH
--------------
Use three nested loops to try every triplet.
Time: O(n³)
Correct but too slow.


KEY INSIGHT
-----------
3Sum is NOT a three-pointer problem.

Fix one element (k), then reduce the problem to:
    Two Sum on the remaining array with target = (equals - k)

This restores monotonicity and allows pointer elimination.


OPTIMIZED APPROACH
------------------
1. Sort the array.
2. Loop over each index as the fixed element k.
3. Skip duplicate k values.
4. For each k:
   - Use two pointers (left = k+1, right = end).
   - Compare nums[left] + nums[right] to target.
   - Move pointers based on comparison.
5. When a valid triplet is found:
   - Add it once.
   - Move both pointers.
   - Skip duplicate values at left and right.
6. Continue until pointers cross.


WHY DUPLICATE SKIPPING WORKS
----------------------------
Because the array is sorted:
- Duplicate values are adjacent.
- Skipping them at pointer movement prevents duplicate triplets
  from ever being generated.
- No set or post-filtering is needed.


COMPLEXITY
----------
Time:  O(n²)
Space: O(1) extra (excluding output)


MENTAL MODEL
------------
"Fix one value. Solve Two Sum on the rest.
Sorted order lets me discard impossible and duplicate cases safely."

If you ever feel tempted to use a set:
→ you haven’t fully exploited ordering yet.

'''