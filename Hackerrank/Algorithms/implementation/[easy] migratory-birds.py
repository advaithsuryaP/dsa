'''
Problem:
Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. 
If more than 1 type has been spotted that maximum amount, return the smallest of their ids.
Example:
Input:
arr = [1, 1, 2, 2, 3]
Output:
2
Explanation:
The most frequently sighted birds are of type 1 and 2, so we return the smallest of their ids, which is 2.
'''
from collections import Counter
def migratoryBirds(arr):
    # Write your code here
    frequency: dict[int, int] = Counter[int, int](arr)
    result: int = 0
    max_frequency: int = 0
    for key, value in frequency.items():
        if value > max_frequency:
            max_frequency = value
            result = key    
        elif value == max_frequency:
            result = min(result, key)
    
    return result

print(migratoryBirds([1, 1, 2, 2, 3])) # 2

'''
Solution: 
A neat problem introducing the Counter class from the collections module. A very handy module to have in your arsenal.
Check the frequency of each bird type, if its the max, then return.
If we have a tie, then return the smallest of the ids.

All neatly and simply done through basic iteration and conditional checking.
'''