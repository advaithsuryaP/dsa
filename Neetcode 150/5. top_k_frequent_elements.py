'''
@Link: https://neetcode.io/problems/top-k-elements-in-list?list=neetcode150
@difficulty: Medium

Problem Statement:
    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Solution:
    - Use the Counter class from the collections module to count the frequency of each element in the array.
    - Use the most_common method of the Counter class to get the k most common elements.
    - Return the elements as a list.

'''
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_counter = Counter(nums)
        most_common_tuple = frequency_counter.most_common(k)
        result = list()
        for number, frequency in most_common_tuple:
            result.append(number)
        return result