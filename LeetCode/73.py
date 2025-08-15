#  leetcode 73 

matrix = [
    [7,5,-3,2],
    [4,20,0,9],
    [19,-0,65,1],
    [99,27,81,3]
]

def setZeros(matrix):
    rows= len(matrix)
    cols = len(matrix[0])
    
    
    rowtrack = [ 0 for _ in range(rows)]
    colstrack = [ 0 for _ in range (cols)]
    
    for i in range(0,rows):
        for j in range(0,cols):
            if matrix[i][j] == 0:
                rowtrack[i] = -1
                colstrack[j] = -1
    
    for i in range(0,rows):
        for j in range(0,cols):
            if rowtrack[i]== -1 or colstrack[j]==-1:
                matrix[i][j] = 0
                
    return matrix

k = setZeros(matrix)
print(matrix)