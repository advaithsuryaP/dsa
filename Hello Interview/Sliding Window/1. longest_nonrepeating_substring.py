'''
Problem:
Write a function to return the length of the longest substring in a provided string s where all characters in the substring are distinct.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The longest substring without repeating characters is "abc".

s = "eghghhgg"
Output: 3
Explanation: The longest substring without repeating characters is "egh".
'''

def longest_nonrepeating_substring(s: str) -> int:
    left: int = 0

    result: int = 0

    window_size: int = 0
    unique: set[int] = set()

    for right in range(len(s)):
        while s[right] in unique:
            unique.remove(s[left])
            left += 1
        
        unique.add(s[right])

        window_size = right - left + 1
        result = max(result, window_size)

    return result









print(longest_nonrepeating_substring("abcabcbb")) # 3
# print(longest_nonrepeating_substring("eghghhgg")) # 3 
# print(longest_nonrepeating_substring("aabbcc")) # 2
# print(longest_nonrepeating_substring("substring")) # 8