'''
@Link: https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150
@difficulty: Medium

Problem Statement:
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the numbers in the array except nums[i].
    You must write an algorithm that runs in O(n) time and without using the division operator.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # SOLUTION 1: GOOD BUT SPACE COMPLEXITY HIGH

        # result: List[int] = list()
        # prefix_product: List[int] = list()
        # postfix_product: List[int] = list()
        # multiplier: int = 1
        # # Compute prefix sum: [1, 2, 6, 24]
        # for num in nums:
        #     multiplier *= num
        #     prefix_product.append(multiplier)
        
        # # Compute postfix sum but by reversing the array: [4, 12, 24, 24]
        # multiplier = 1
        # for num in reversed(nums):
        #     multiplier *= num
        #     postfix_product.append(multiplier)
        
        # # Postfix is reversed, so flip it back
        # postfix_product.reverse()

        # for i in range(len(nums)):
        #     if(i == 0):
        #         result.append(1 * postfix_product[i+1])
        #     elif(i == len(nums)-1):
        #         result.append(prefix_product[i-1] * 1)
        #     else: 
        #         result.append(prefix_product[i-1] * postfix_product[i+1])

        # return result

        # --------------------------------------------------

        # SOLUTION 2
        result: List[int] = list()

        # Prefix pass
        prefix: int = 1
        for num in nums:
            result.append(prefix)
            prefix *= num

        # Postfix pass
        postfix: int = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result


solution = Solution()
print(solution.productExceptSelf([1,2,3,4])) # [24,12,8,6]
# print(solution.productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]


"""
Problem: productExceptSelf(nums)
--------------------------------
Given an array of numbers, for each position i, I need to find the product of all elements 
except nums[i] — but without using division. Example:
    nums = [1, 2, 3, 4]
    output = [24, 12, 8, 6]
because:
    - For 1: 2*3*4 = 24
    - For 2: 1*3*4 = 12
    - For 3: 1*2*4 = 8
    - For 4: 1*2*3 = 6

--------------------------------
First thought (brute force):
--------------------------------
For each element, multiply everything else. That’s O(n²) — too slow.

--------------------------------
Next thought (prefix + postfix arrays):
--------------------------------
If I know:
    prefix[i] = product of all elements *before* i
    postfix[i] = product of all elements *after* i
then:
    result[i] = prefix[i] * postfix[i]
Simple and intuitive. 
But building both prefix[] and postfix[] uses O(n) extra space each.

--------------------------------
The key realization:
--------------------------------
At any index, result[i] only needs two things:
    - product of elements before it  (prefix)
    - product of elements after it   (postfix)
We can build prefix on the fly (left → right),
and then fold in postfix (right → left) using a single running variable.
We don’t need to store both arrays.

--------------------------------
Optimized logic (the “magic” part):
--------------------------------
1. First pass (left → right):
   Store in result[i] the product of all numbers before i.
   Example for [1,2,3,4]:
       result after prefix pass = [1, 1, 2, 6]
   (each index holds the product of everything to its left)

2. Second pass (right → left):
   Keep a variable postfix = 1.
   As we move backward, multiply result[i] by postfix (everything after i),
   then update postfix *= nums[i].
   This merges both prefix and postfix in-place.

--------------------------------
Why the reverse loop is essential:
--------------------------------
When iterating backward, postfix always represents the product of all elements 
to the right of the current index. That’s why:
    for i in range(len(nums)-1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
is the “magic line” — it combines left and right products correctly.

--------------------------------
Result:
--------------------------------
We get the final array in O(n) time and O(1) extra space (ignoring output).
It’s elegant because we reuse the result array as both prefix and final container.
"""
