"""
Given an m x n binary matrix filled with 0's and 1's, 
find the largest square containing only 1's and return its area.
"""
def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]        
    :rtype: int
    """
    if not matrix or not matrix[0]:
        return 0
    row, column = len(matrix), len(matrix[0])
    
    stored_size = [[0]*(column+1) for i in range(row+1)]
    maxSize = 0
    
    print(stored_size)
    for i in range(1, row+1):
        for j in range(1, column+1):
            if(matrix[i-1][j-1]) == "1":
                stored_size[i][j] = min(stored_size[i-1][j], stored_size[i][j-1], stored_size[i-1][j-1]) + 1
                print(stored_size)
                maxSize = max(stored_size[i][j], maxSize)
    return maxSize **2

matrix = [["1", "1"], ["1", "1"]]
print(maximalSquare(matrix))
    
