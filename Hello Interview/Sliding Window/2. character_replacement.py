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
    occurences: dict[str, int] = dict()

    for right in range(len(s)):
        # while s[right] not in occurences and k == 0:
        #     continue

        occurences[s[right]] = occurences.get(s[right], 0) + 1
        print(occurences)
    
    max_occurrence: str = max(occurences, key=occurences.get)
    print(max_occurrence)
    


print(character_replacement("BBABCCDD", 2)) # 5