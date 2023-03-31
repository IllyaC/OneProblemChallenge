"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells 
need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
def isValidSudoku(board):
    
    def is_valid_group(items):
        seen = set()
        for item in items:
            if item != '.':
                if item in seen:
                    return False
                else:
                    seen.add(item)
        return True

    def get_box_values(board, row, col):
        box_values = []
        for i in range(3):
            for j in range(3):
                box_values.append(board[row * 3 + i][col * 3 + j])
        return box_values

    # Check rows and columns
    for i in range(9):
        row = []
        col = []
        for j in range(9):
            row.append(board[i][j])
            col.append(board[j][i])

        if not is_valid_group(row) or not is_valid_group(col):
            return False

    # Check boxes
    for i in range(3):
        for j in range(3):
            box_values = get_box_values(board, i, j)
            if not is_valid_group(box_values):
                return False

    return True
   



board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))
            
            