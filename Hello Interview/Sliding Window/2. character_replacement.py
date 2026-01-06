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
    result: float = float('-inf')

    left: int = 0
    
    occurrences: dict[str, int] = dict[str, int]()

    max_frequency: int = 0
    window_size: int = 0
    for right in range(len(s)):
        print(f"----------- Iterating {s[right]} -----------")
        
        
        occurrences[s[right]] = occurrences.get(s[right], 0) + 1

        while window_size - max_frequency > k:
            # Window is invalid here
            occurrences[s[left]] -= 1
            print(f"Invalid window. Decremented the count of {s[left]} in {occurrences}")
            left += 1
            window_size = right - left + 1
            max_frequency_key: str = max(occurrences, key=occurrences.get)
            max_frequency = occurrences[max_frequency_key]


        max_frequency_key: str = max(occurrences, key=occurrences.get)
        max_frequency = occurrences[max_frequency_key]
        
        window_size = right - left + 1
        result = max(result, window_size)
        
        
        print(f"Window Size: {window_size}, Max Frequency: {max_frequency}, Occurrences: {occurrences} || Result: {result}")



    return result
        

print(character_replacement("BBABCCDD", 2)) # 5