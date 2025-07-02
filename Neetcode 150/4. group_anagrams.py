'''
@Link: https://neetcode.io/problems/anagram-groups?list=neetcode150
@difficulty: Medium

Problem Statement:
    Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

Context:
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Solution: Interesting problem. 
    - Take an empty array and a dictionary.
    - Browse through the array and sort each element. 
    - If the sorted element is in the dictionary, append the element to the existing value.
    - If the sorted element is not in the dictionary, create a new key with the sorted element and the value as the element.
    The dictionary will ultimately look like this:
        {
            'aet': ['eat', 'tea', 'ate'],
            'ant': ['tan', 'nat'],
            'abt': ['bat']
        }
    The keys are the sorted elements and the values are the lists of anagrams.
    - Finally, return the values of the dictionary.

'''

from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = list()
        result_dict = dict()
        for element in strs:
            sorted_element = ''.join(sorted(element))
            if sorted_element in result_dict:
                existing_value = result_dict[sorted_element]
                existing_value.append(element)
                result_dict[sorted_element] = existing_value
            else:
                result_dict[sorted_element] = [element] 
        for value in result_dict.values():
            result.append(value)
        return result

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["eat","tea","ate"],["tan","nat"],["bat"]]
print(solution.groupAnagrams([""])) # [[]]
print(solution.groupAnagrams(["a"])) # [["a"]]