'''
@Link: https://neetcode.io/problems/string-encode-and-decode?list=neetcode150'
@difficulty: Medium

Problem Statement: Design an algorithm to encode a list of strings into a single string and decode the string back to the original list of strings.

Example 1:
Input: strs = ["lint","code","love","you"]
Output: ["lint","code","love","you"]

'''
from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for word in strs:
            encoded += str(len(word)) + '#' + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = list()
        while len(s):
            index_of_hash = s.index('#')
            length_of_number = len(s[0:index_of_hash])
            length_of_word = int(s[0:index_of_hash])
            offset = length_of_number + 1 # 1 indicates the # itself
            decoded_word = s[offset:length_of_word+offset]
            decoded.append(decoded_word)
            s = s[length_of_word+offset:]
        return decoded


solution = Solution()
encoded = solution.encode(["we","say",":","yes","!@#$%^&*()"])
print(encoded)
decoded = solution.decode(encoded)
print(decoded)