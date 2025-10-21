'''
@Link: https://neetcode.io/problems/valid-sudoku?list=neetcode150
@difficulty: Medium

Problem Statement:
    You are given a 9x9 sudoku board. The board is valid if the following rules are met:
    - Each row must contain the digits 1-9 without repetition.
    - Each column must contain the digits 1-9 without repetition.
    - Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    Return True if the board is valid, otherwise return False.

    Note: The board does not need to be full or be solvable to be valid.

Example 1:
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

 Output: True

Example 2:
 [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
 Output: False
'''

from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     # SOLUTION 1: GOOD BUT SPACE COMPLEXITY HIGH
    #     # Check Rows
    #     for row in board:
    #         is_unique = self.is_row_unique(row)
    #         if not is_unique: return False
        
    #     # Check Columns
    #     for column in zip(*board):
    #         is_unique = self.is_row_unique(column)
    #         if not is_unique: return False

    #     # Segregate into squares and check uniqueness
    #     for row in range(0, 9, 3):
    #         for column in range(0, 9, 3):
    #             # List comprehension again for [x for i in ... for j in ...]
    #             '''
    #             Equivalent code for - 
    #             cells = []
    #             for i in range(r, r + 3):
    #                 for j in range(c, c + 3):
    #                     cells.append(board[i][j])
    #             '''
    #             cells = [board[i][j] for i in range(row, row + 3) for j in range(column, column + 3)]
    #             is_unique = self.is_row_unique(cells)
    #             if not is_unique: return False
        
    #     return True

    # def is_row_unique(self, row: List[str]) -> bool:
    #     # Remove the white spaces which are indicated by a "."
    #     # Method 1: Convert to string and replace all dots 
    #     # row_without_whitespace = "".join(row).replace(".", "")
        
    #     # Method 2: keep the format in lists and use list comprehension instead
    #     row_without_whitespace = [x for x in row if x != "."]
    #     return len(row_without_whitespace) == len(set(row_without_whitespace))

    # --------------------------------------------------

    # SOLUTION 2
        columns = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if(board[row][col] == '.'): continue

                if(board[row][col] in rows[row] or board[row][col] in columns[col] or board[row][col] in squares[(row // 3, col // 3)]): return False

                rows[row].add(board[row][col])
                columns[col].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])
        
        # Iterate rows
        for key, value in rows.items():
            print(key, value)
            '''
            0 {'2', '3', '1'}
            1 {'4', '5'}
            2 {'3', '8', '9'}
            3 {'6', '4', '5'}
            4 {'3', '8', '5'}
            5 {'2', '7', '6'}
            6 {'2'}
            7 {'9', '8', '4', '1'}
            8 {'7', '8', '9'}            
            '''
        for key, value in columns.items():
            print(key, value)
            '''
            0 {'5', '7', '4', '1'}
            1 {'2', '9'}
            4 {'8', '2', '3', '6', '1'}
            3 {'8', '4', '5'}
            2 {'8'}
            8 {'8', '4', '3', '6', '9', '5'}
            5 {'3', '9'}
            6 {'2'}
            7 {'7'}
            '''
        for key, value in squares.items():
            print(key, value)
            '''
            (0, 0) {'8', '4', '2', '9', '1'}
            (0, 1) {'3', '5'}
            (0, 2) {'3'}
            (1, 0) {'7', '5'}
            (1, 1) {'2', '3', '6', '8'}
            (1, 2) {'6', '4', '5'}
            (2, 2) {'2', '7', '8', '9'}
            (2, 1) {'9', '8', '4', '1'}
            '''
        return True


solution = Solution()
board1 = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
print(solution.isValidSudoku(board1))
board2 = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
print(solution.isValidSudoku(board2))

'''
============================
✅ PROBLEM SUMMARY
============================

@Link: https://neetcode.io/problems/valid-sudoku?list=neetcode150
@Difficulty: Medium
@Topic: Hashing / Matrix Traversal / Constraints Checking

Problem:
---------
You are given a partially filled 9×9 Sudoku board. Determine if the board configuration 
is *valid* under standard Sudoku rules:
1. Each row contains digits 1–9 at most once.
2. Each column contains digits 1–9 at most once.
3. Each of the nine 3×3 sub-boxes contains digits 1–9 at most once.

Note:
- The board may be incomplete (empty cells represented by '.').
- You don’t need to solve the puzzle, only validate its current state.

Input: 9x9 List[List[str]]
Output: Boolean — True if valid, False otherwise


============================
🧠 NAIVE APPROACH (SOLUTION 1)
============================

Intuition:
-----------
Handle each constraint separately:
1️⃣ Validate each row — ensure no duplicates ignoring '.'
2️⃣ Validate each column — transpose the board using zip(*board)
3️⃣ Validate each 3×3 box — gather 9 elements using two nested loops.

Pseudocode:
-----------
for each row → check unique digits
for each column in zip(*board) → check unique digits
for each sub-box starting at (r, c) in [0,3,6]:
    collect cells from (r:r+3, c:c+3)
    check unique digits

Helper Function:
----------------
def is_row_unique(row):
    filtered = [x for x in row if x != '.']
    return len(filtered) == len(set(filtered))

Complexity:
-----------
- Time: O(81) → O(1) for fixed 9×9 board
- Space: O(1)
- Passes: 3 (rows + columns + boxes)
✅ Very readable but slightly repetitive.

Key Insight:
-------------
All three checks (row, column, box) share the same uniqueness condition.
They only differ by how we *collect* their elements.

============================
⚡ OPTIMAL APPROACH (SOLUTION 2)
============================

Intuition:
-----------
We can merge all three checks into a *single traversal*.

Each cell belongs to:
- one row (index = row)
- one column (index = col)
- one 3×3 box (index = (row // 3, col // 3))

So, during one pass:
- if a number already exists in its row, column, or box → invalid.
- else → mark it as seen in all three.

Data Structures:
----------------
- rows[row]     = set of seen numbers in that row
- columns[col]  = set of seen numbers in that column
- squares[(r // 3, c // 3)] = set of seen numbers in that sub-box

Code Flow:
----------
for row in range(9):
    for col in range(9):
        val = board[row][col]
        if val == '.': continue

        # If number already exists → invalid
        if val in rows[row] or val in columns[col] or val in squares[(row//3, col//3)]:
            return False

        # Otherwise, record number in all three sets
        rows[row].add(val)
        columns[col].add(val)
        squares[(row//3, col//3)].add(val)

return True

Why (row // 3, col // 3)?
-------------------------
- Integer division groups indices into 3-row × 3-column zones:
  (0,0) → top-left box, (0,1) → top-middle, (2,2) → bottom-right.
- This tuple acts as a unique "box identifier".

============================
💡 KEY TAKEAWAYS
============================
- Sudoku validation is about checking **unique membership** under multiple constraints.
- The set data structure is perfect for O(1) lookups and insertions.
- Using `(r // 3, c // 3)` elegantly maps any cell to its sub-box.
- `zip(*board)` transposes a matrix without extra memory unless reused.
- List comprehensions like `[board[i][j] for i ... for j ...]` flatten 3×3 areas neatly.
- Defaultdict(set) simplifies dynamic initialization — no manual checks required.

============================
🧮 COMPLEXITY ANALYSIS
============================
- Time Complexity: O(81) → O(1) constant for 9×9 board
- Space Complexity: O(81) for 3 × 9 sets (rows, cols, boxes)
- Passes: 1 (single traversal)
✅ Clean, optimal, and interview-ready.

============================
📘 PERSONAL INSIGHTS
============================
- Understood the deep equivalence between "3 separate passes" and "1 unified pass".
- Learned to visualize Sudoku constraints as overlapping sets of rules.
- Practiced both clarity-first (multi-pass) and efficiency-first (one-pass) design.
- Internalized that code readability and reasoning come *before* optimization.
- Gained intuition for matrix transformations (`zip`), list comprehensions, 
  and box-index mapping using integer division.

============================
✅ FINAL RESULT
============================
- Both solutions are valid.
- Solution 1 is clear for conceptual understanding.
- Solution 2 is optimal for interviews and production.
'''

