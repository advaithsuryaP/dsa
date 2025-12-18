'''
Problem:
Given the starting position and jump distance of two kangaroos, determine if they will ever land 
on the same position at the same time.
Example:
Input:
x1 = 0
v1 = 3
kangaroo 1 jumps 3 units per jump
x2 = 4
v2 = 2
kangaroo 2 jumps 2 units per jump
Output:
YES
Explanation:
The kangaroos will land on the same position at the same time after 2 jumps.
Kangaroo 1 will land on position 6 after 2 jumps.
Kangaroo 2 will land on position 6 after 2 jumps.
'''

def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
    
    numerator: int = x1 - x2
    denominator: int = v2 - v1
    
    
    if(numerator % denominator == 0):
        if numerator // denominator >= 0:
            return "YES"
    return "NO"

print(kangaroo(0, 3, 4, 2)) # YES
print(kangaroo(0, 2, 5, 3)) # NO

'''
Solution:
This problem is testing the ability to think mathematically and logically.
Solve the equation algebrically to find out if they will land on the same position at the same time.

The equation is: x1 + n*v1 = x2 + n*v2 where n is the number of jumps.
Simplify the equation to: n*(v2 - v1) = x1 - x2
where n = (x1 - x2) / (v2 - v1)

So for every jump, the equation x1-x2 should be divisible by v2-v1 if they are to meet. 
But there is a catch here. The kangaroos could still meet, ie.. the equation would be satisfied 
sometime in the past but we need to check the future. So we need to check if the division is perfect AND positive.

The other edge case is when the kangaroos have the same jump distance. In that case, they will never meet.
'''