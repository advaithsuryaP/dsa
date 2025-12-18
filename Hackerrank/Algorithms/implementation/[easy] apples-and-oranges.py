'''
Problem: 
Given the start and end points of a house, and the start and end points of a tree, and the number of apples and oranges that fell, 
find the number of apples and oranges that fell on the house. The apple and orange trees are on the same line and the house is on the same line.
Example:
Input:
s = 7
t = 11
a = 5
b = 15
apples = [2, 3, -4]
oranges = [3, -2, -4]
Output:
4 2
'''

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apples_available = sum(1 for d in apples if s <= a + d <= t)
    oranges_available = sum(1 for d in oranges if s <= b + d <= t)

    print(apples_available)
    print(oranges_available)

countApplesAndOranges(7, 11, 5, 15, [2, 3, -4], [3, -2, -4]) # 4 2

'''
Solution: 
This problem is straightforward. Calculate the distances the apples and oranges fell and 
check if they are within the house range. But this tests the ability to be pythonic. 

Efficient way to do this is to use list comprehensions and max out on the pythonic nature of the language.
The sum function encapsulates on the comprehension and returns the number of apples and oranges that fell on the house.
'''