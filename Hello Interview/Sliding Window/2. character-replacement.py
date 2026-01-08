'''
Problem: 

Write a function to find the length of the longest substring containing the same letter in a given string s, 
after performing at most k operations in which you can choose any character of the string and change it to any other uppercase English letter.

Example:
s = "BBABCCDD"
k = 2

Output: 5
Explanation: Replace the first 'A' and 'C' with 'B' to form "BBBBBCDD". The longest substring with identical letters is "BBBBB", which has a length of 5.
'''

def character_replacement(s: str, k: int) -> int:
    result: int = 0
    
    left: int = 0

    a: list = []
    a
    
    max_frequency: int = 0
    occurrences: dict[str, int] = dict[str, int]()
    
    for right in range(len(s)):
        occurrences[s[right]] = occurrences.get(s[right], 0) + 1
        max_frequency = max(occurrences[s[right]], max_frequency)

        while (right - left + 1) - max_frequency > k:
            occurrences[s[left]] -= 1
            left += 1
        
        result = max(result, right - left + 1)

    return result
        

print(character_replacement("BBABCCDD", 2)) # 5