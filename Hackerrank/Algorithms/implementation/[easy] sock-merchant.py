'''
Link: https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true
Difficulty: Easy

Problem:
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.
Example:
Input:
n = 7
ar = [1, 2, 1, 2, 1, 3, 2]
Output:
2
'''

def sockMerchant(n, ar):
    frequency: dict[int, int] = dict()
    result: int = 0
    for val in ar: 
        if frequency.get(val):
            frequency.pop(val)
            result += 1
        else:
            frequency[val] = 1
    return result

print(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2])) # 2   

'''
A very unconventional solution for a very simple problem. The concept of storing the 
frequency of an element and if we have a matching element, that means we have a pair.
In which case, just remove the element in the dictionary and increment the result.

'''