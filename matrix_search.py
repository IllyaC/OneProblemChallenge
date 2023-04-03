def search_matrix(matrix, target):
    if not matrix:
        return False

    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1

    while row < m and col >= 0:
        current_value = matrix[row][col]
        if current_value == target:
            return True
        elif current_value > target:
            col -= 1
        else:
            row += 1

    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(search_matrix(matrix, target))