'''
@Link: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true
@Difficulty: Easy

Problem:
Given an array of integers and a positive integer k, determine the number of (i,j) pairs where i < j and ar[i] + ar[j] is divisible by k.
Example:
Input:
n = 6
k = 3
ar = [1, 3, 2, 6, 1, 2]
Output:
5
'''

def divisibleSumPairs(n, k, ar):
    seen = dict()
    result: int = 0
    
    for x in ar:
        remainder: int = x%k
        required: int = (k-remainder)%k
        
        result += seen.get(required, 0)
        seen[remainder] = seen.get(remainder, 0) + 1
    
    return result

"""
DIVISIBLE SUM PAIRS — DEEP DRY RUN (with remainders + seen dict)

Problem:
Count pairs (i, j), i < j, such that (ar[i] + ar[j]) % k == 0.

Key trick:
Instead of checking every pair O(n^2), we only track remainders mod k.

If:
  r = x % k
Then we need a previous element with remainder:
  required = (k - r) % k
Because:
  (r + required) % k == 0

Why %k on required?
- Handles remainder = 0 properly:
    r=0 -> required=(k-0)%k = 0
  so 0 pairs with 0.

What 'seen' stores:
seen[rem] = how many elements we've already processed (to the left) with remainder rem.
Since 'seen' only contains earlier elements, i < j is automatically satisfied:
- when we're at current index j, all counts in 'seen' belong to indices < j.

Algorithm per element x:
1) r = x % k
2) required = (k - r) % k
3) Add seen[required] to result because:
   - every earlier element with remainder 'required' forms a valid pair with x
4) Increment seen[r] because x is now available for future elements

---------------------------------------------------------
DRY RUN:
ar = [12, 8, 6, 4, 9, 3]
k = 5

We’ll track:
- current x
- r = x % 5
- required = (5 - r) % 5
- how many matches already in seen[required]
- result after counting
- seen after updating

Initialize:
seen = {}   # no remainders seen yet
result = 0

Index 0: x = 12
r = 12 % 5 = 2
required = (5 - 2) % 5 = 3
seen.get(3, 0) = 0  -> no earlier remainder-3 numbers exist
result += 0  -> result = 0
Update seen[2] += 1
seen = {2: 1}

Interpretation:
We need a previous remainder 3 to pair with remainder 2.
But since this is the first number, no pairs yet.

---------------------------------------------------------

Index 1: x = 8
r = 8 % 5 = 3
required = (5 - 3) % 5 = 2
seen.get(2, 0) = 1  -> we HAVE seen one remainder-2 number (that was 12)
result += 1  -> result = 1
Update seen[3] += 1
seen = {2: 1, 3: 1}

Which pair did we count?
- previous remainder 2: 12
- current remainder 3: 8
12 + 8 = 20, and 20 % 5 == 0, so pair counted.

---------------------------------------------------------

Index 2: x = 6
r = 6 % 5 = 1
required = (5 - 1) % 5 = 4
seen.get(4, 0) = 0  -> no earlier remainder-4 numbers
result += 0  -> result = 1
Update seen[1] += 1
seen = {2: 1, 3: 1, 1: 1}

Interpretation:
A remainder-1 number needs a remainder-4 partner, but none seen so far.

---------------------------------------------------------

Index 3: x = 4
r = 4 % 5 = 4
required = (5 - 4) % 5 = 1
seen.get(1, 0) = 1  -> we HAVE seen one remainder-1 number (that was 6)
result += 1  -> result = 2
Update seen[4] += 1
seen = {2: 1, 3: 1, 1: 1, 4: 1}

Which pair did we count?
6 + 4 = 10, and 10 % 5 == 0.

---------------------------------------------------------

Index 4: x = 9
r = 9 % 5 = 4
required = (5 - 4) % 5 = 1
seen.get(1, 0) = 1  -> still only one remainder-1 number exists (6)
result += 1  -> result = 3
Update seen[4] += 1
seen = {2: 1, 3: 1, 1: 1, 4: 2}

Which pair did we count?
6 + 9 = 15, and 15 % 5 == 0.

Important:
We added +1 again because the SAME remainder-1 element (6) pairs with this new 4-remainder element (9).
Now we have two remainder-4 elements (4 and 9), hence seen[4]=2.

---------------------------------------------------------

Index 5: x = 3
r = 3 % 5 = 3
required = (5 - 3) % 5 = 2
seen.get(2, 0) = 1  -> remainder-2 exists once (12)
result += 1  -> result = 4
Update seen[3] += 1
seen = {2: 1, 3: 2, 1: 1, 4: 2}

Which pair did we count?
12 + 3 = 15, and 15 % 5 == 0.

---------------------------------------------------------

FINAL ANSWER:
result = 4

The 4 valid pairs (by values) are:
(12, 8)  -> 20
(6, 4)   -> 10
(6, 9)   -> 15
(12, 3)  -> 15

All divisible by 5, and indices always satisfy i < j because we only match with earlier elements.
"""

