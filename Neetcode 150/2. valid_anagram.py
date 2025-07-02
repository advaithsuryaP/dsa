'''
@Link: https://neetcode.io/problems/valid-anagram?list=neetcode150
@difficulty: Easy

Problem Statement: 
    Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false. 

Context:
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Solution:
    [Solution One]: We need to use a hashmap to count the frequency of each character in both the strings and then check for equality.
    [Solution Two]: Another solution, is to simply sort the strings and then check for equality but this is less efficient as it's nlog(n) time complexity.
'''
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1_counter = Counter(s)
        c2_counter = Counter(t)
        if len(c1_counter) != len(c2_counter):
            return False
        for key, value in c1_counter.items():
            if c2_counter[key] != value:
                return False
        return True

solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))