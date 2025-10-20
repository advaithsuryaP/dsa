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

"""
🧩 Problem: Encode and Decode Strings
------------------------------------
Design an algorithm to encode a list of strings into a single string and 
decode it back without any loss of information.

Example:
---------
Input:  ["lint", "code", "love", "you"]
Encode: "4#lint4#code4#love3#you"
Decode: ["lint", "code", "love", "you"]

---

Naive Approach:
---------------
Use a simple delimiter like "," to join and split.
    encoded = ",".join(strs)
    decoded = encoded.split(",")
❌ Problem: What if the strings themselves contain commas (",")?
Decoding breaks because we can't tell delimiter vs data apart.

---

Key Insight:
-------------
We need a *self-describing format*.
If each string says how long it is, we can always decode safely —
no matter what characters the string contains.

So, encode each word as:
    "<len>#<word>"
Example: "4#love"

Then just concatenate all such chunks.

---

Optimized Approach:
-------------------
Encoding:
    - For each word, compute len(word)
    - Add "len#word" to the output string
    - O(N) time and space, where N is total number of characters

Decoding:
    - Parse characters left to right.
    - Read up to the next '#', which gives us the length of the next word.
    - Use that length to extract exactly that many characters after '#'.
    - Continue until string is fully consumed.

Example:
---------
Encoded = "4#love3#you"
Iteration:
    - Read "4#", → length = 4
    - Extract next 4 chars → "love"
    - Move pointer to next chunk → "3#you"
    - Repeat → "you"
Output = ["love", "you"]

---

Complexity:
------------
Time  = O(N)  (both encode and decode scan each character once)
Space = O(N)  (output string and list store all data once)

---

💡 Summary:
This problem is a perfect example of *data self-description* —
when a string needs to encode its own structure so it can be losslessly parsed.
It’s simple, elegant, and interview gold because it tests your
understanding of edge cases, not just syntax.
"""
