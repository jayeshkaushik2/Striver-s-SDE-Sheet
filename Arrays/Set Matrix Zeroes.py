def setZeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])
    rw = False
    
    for i in range(m):
        for j in range(n):
            if i > 0:
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
            else:
                if matrix[i][j] == 0:
                    rw = True
    
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
                
    if matrix[0][0] == 0:
        for i in range(m):
            matrix[i][0] = 0
            
    if rw:
        for j in range(n):
            matrix[0][j] = 0

matrix = [[1,1,1], [1,0,1], [1,1,1]]
setZeroes(matrix=matrix)
print(matrix)