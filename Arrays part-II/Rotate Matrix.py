def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i] = matrix[i][::-1]

matrix = [[1,2,3],[4,5,6],[7,8,9]] # Output [[7,4,1],[8,5,2],[9,6,3]]
rotate(matrix=matrix)
print(matrix)