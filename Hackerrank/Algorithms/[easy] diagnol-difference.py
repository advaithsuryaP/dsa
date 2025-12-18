'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix is shown below:

1 2 3
4 5 6
9 8 9 

The left-to-right diagonal = 1 + 5 + 9 = 15. 
The right-to-left diagonal = 3 + 5 + 9 = 17. 
Their absolute difference is |15 - 17| = 2.

'''
from typing import List
def diagonalDifference(arr: List[List[int]]) -> int:
    left_to_right_diagonal: int = 0
    right_to_left_diagonal: int = 0

    for i in range(len(arr)):
        left_to_right_diagonal += arr[i][i]
        right_to_left_diagonal += arr[i][len(arr)-i-1]
    
    return abs(left_to_right_diagonal - right_to_left_diagonal)

print(diagonalDifference([[1,2,3],[4,5,6],[9,8,9]]))  

'''
Solution:
    The trick to this question lies in knowing how to access the elements of the diagonal.
    
    When you iterate the 2-D array, the index of the left-right diagonal is the same as the index of the element.
    Ex:  arr = [[1,2,3],[4,5,6],[9,8,9]]
         when i = 0, the index of the left-right diagonal is 0, so the element is arr[0][0] = 1
         when i = 1, the index of the left-right diagonal is 1, so the element is arr[1][1] = 5
         when i = 2, the index of the left-right diagonal is 2, so the element is arr[2][2] = 9
    So, the left-right diagonal is arr[i][i]
    
    The index of the right-left diagonal is the length of the array minus the index of the element minus 1.
    Ex:  arr = [[1,2,3],[4,5,6],[9,8,9]]
         when i = 0, the index of the right-left diagonal is 2, so the element is arr[0][2] = 3
         when i = 1, the index of the right-left diagonal is 1, so the element is arr[1][1] = 5
         when i = 2, the index of the right-left diagonal is 0, so the element is arr[2][0] = 9
    So, the right-left diagonal is arr[i][len(arr)-i-1]

    With this knowledge, the accessing of the diagnol elements is O(n) time complexity.
'''
