'''
Problem:
Write a function to calculate the maximum number of fruits you can collect from an integer array fruits, where each element represents a type of fruit. 
You can start collecting fruits from any position in the array, but you must stop once you encounter a third distinct type of fruit.
The goal is to find the longest subarray where at most two different types of fruits are collected.
'''

from typing import List
def fruit_basket(fruits: List[int]) -> int:
    result: int = 0
    return


print(fruit_basket([1, 2, 1, 3, 4, 3, 5, 1, 2])) # 3