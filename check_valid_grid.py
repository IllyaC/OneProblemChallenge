"""
There is a knight on an n x n chessboard. In a valid configuration, 
the knight starts at the top-left cell of the board and visits every cell on the board exactly once.

You are given an n x n integer matrix grid consisting 
of distinct integers from the range [0, n * n - 1] where grid[row][col] 
indicates that the cell (row, col) is the grid[row][col]th cell that the knight visited. 
The moves are 0-indexed.

Return true if grid represents a valid configuration of the knight's movements or false otherwise.

Note that a valid knight move consists of moving two squares vertically 
and one square horizontally, or two squares horizontally and one square vertically. 
The figure below illustrates all the possible eight moves of a knight from some cell.
"""

def checkValidGrid(grid):
    """
    :type grid: List[List[int]]
    :rtype: bool
    """
    n = len(grid)
    positions = {}
    for row in range(n):
        for col in range(n):
            positions[grid[row][col]] = (row, col)
    def is_valid_move(start, end):
        x1, y1 = start
        x2, y2 = end
        dx, dy = abs(x1-x2), abs(y1-y2)
        return(dx == 1 and dy ==2) or (dx == 2 and dy == 1)
    
    step = n * n -1
    while step > 0:
        start = positions[step]
        end = positions[step-1]
        print(start, end)
        if( not is_valid_move(start, end)):
            return False
        step -=1
    return True

"grid = [[0,3,6],[5,8,1],[2,7,4]]"
"grid2 = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]"
grid3 = [[24,11,22,17,4],[21,16,5,12,9],[6,23,10,3,18],[15,20,1,8,13],[0,7,14,19,2]]
"print(checkValidGrid(grid))"
"print(checkValidGrid(grid2))"
print(checkValidGrid(grid3))
        