'''
@Link: https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true
@Difficulty: Hard

Problem:
Given two sets of integers, find the numbers that satisfy the following conditions:
1. The elements of the first array are the factors of the numbers being considered.
2. The elements of the second array are multiples of the numbers being considered.
Example:
Input:
a = [2, 4]
b = [16, 32, 96]
Output:
3
'''

from math import gcd
from functools import reduce
def getTotalX(a, b):
    # Step 1: Compute the LCM of the first array
    L: int = reduce(lcm, a)
    
    # Step 2: Compute the GCD of the second array
    G: int = reduce(gcd, b)
    
    # Step 3: Count multiples of L that divide G
    count: int = 0
    multiple: list[int] = L
    while multiple <= G:
        if G % multiple == 0:
            count += 1
        multiple += L
    return count

def lcm(x, y): 
    return x * y // gcd(x, y)
    
print(getTotalX([2, 4], [16, 32, 96])) # 3


"""
PROBLEM SUMMARY — BETWEEN TWO SETS

We are given two integer arrays:
    a (first array)
    b (second array)

We must count how many integers X satisfy BOTH conditions:

1) Every element in array 'a' is a factor of X
   → X must be divisible by all elements of 'a'
   → X is a MULTIPLE of every a[i]

2) X is a factor of every element in array 'b'
   → Every b[j] must be divisible by X
   → X is a COMMON DIVISOR of array 'b'


MENTAL MODEL (KEY INSIGHT)
------------------------------------------------
The problem is NOT about checking many numbers blindly.
It is about compressing constraints using number theory.

The conditions reduce to:

    a[]  → divides →  X  → divides →  b[]


NUMBER THEORY TOOLS USED
------------------------------------------------
1) LCM (Least Common Multiple)
   - LCM(a) is the SMALLEST number divisible by all elements in 'a'
   - Any valid X must be a MULTIPLE of LCM(a)

2) GCD / HCF (Greatest Common Divisor)
   - GCD(b) is the LARGEST number that divides all elements in 'b'
   - Any valid X must be a FACTOR of GCD(b)

Important identity:
    The set of numbers that divide all elements of b
    is EXACTLY the set of factors of GCD(b).


FINAL REDUCED PROBLEM
------------------------------------------------
Count how many numbers X satisfy:

    X = k * LCM(a)
    AND
    GCD(b) % X == 0

In other words:
    Count multiples of LCM(a) that divide GCD(b)


ALGORITHM STEPS
------------------------------------------------
1) Compute L = LCM of all elements in array 'a'
2) Compute G = GCD of all elements in array 'b'
3) Iterate through multiples of L up to G
4) Count those multiples that divide G exactly


EDGE CASE
------------------------------------------------
If L > G, then no such X exists → return 0


WHY THIS WORKS
------------------------------------------------
- LCM compresses "X must be divisible by all of a" into ONE number
- GCD compresses "X must divide all of b" into ONE number
- Their intersection gives all valid solutions
- No brute force, no wasted checks


TIME COMPLEXITY
------------------------------------------------
- LCM computation: O(len(a) * log M)
- GCD computation: O(len(b) * log M)
- Loop over multiples: O(G / L)

Efficient and safe for large inputs.


PYTHON FUNCTIONS USED
------------------------------------------------
- math.gcd      → computes GCD of two numbers
- functools.reduce → applies gcd/lcm across arrays
- custom lcm function built using gcd


FINAL IMPLEMENTATION
------------------------------------------------
"""
