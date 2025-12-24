'''
@Link: https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true
@Difficulty: Easy

Problem:
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
Lily decides to share a contiguous segment of the chocolate bar selected such that:
The length of the segment matches Ron's birth day.
The sum of the integers on the squares is equal to his birth month.
Determine how many ways she can divide the chocolate.
Example:
Input:
s = [2, 2, 1, 3, 2]
d = 4
m = 2
Output: 2
'''

def birthday(s, d, m):
    # SOLUTION 1: NAIVE
    # window_sum: int = sum(s[0:m])
    # result: int = 0
    
    # for i in range(m, len(s)):
    #     if window_sum == d:
    #         result += 1
        
            
    # return result

    # SOLUTION 2: SLIDING WINDOW
    window_sum: int = sum(s[:m])
    result: int = 1 if window_sum == d else 0
    
    for i in range(m, len(s)):
        window_sum += s[i]
        window_sum -= s[i-m]
        if window_sum == d:
            result += 1
        
    return result

print(birthday([2, 2, 1, 3, 2], 4, 2)) # 2

'''
This problem is a wonderful introduction to the concept of sliding window. The first solution is very straightforward and naive. But it is not efficient.
It computes the sum of the window for each iteration. So if window size is m, it takes O(n*m) time complexity, which is not efficient.

Introducing the sliding window technique, which says
new_sum = old_sum  - element_leaving + element_entering, which is O(1) time complexity and ultimately the problem then becomes O(n) time complexity.

So, as per the sliding window technique, 
we first calculate the initial window sum and then start our teration from the m'th index. 
Here, we slide the window by 1 at a time and add the new element to the window (the mth index) and subtract the element that is leaving the window (i-m index)

'''
