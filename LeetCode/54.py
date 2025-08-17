# print the matrix in spiral order 
# Leet Code - 54

matrix = [
    [1,2,3,4,5],
    [16,17,18,19,6],
    [15,24,25,20,7],
    [14,23,22,21,8],
    [13,12,11,10,9]
]

def print_spiral_matrix(matrix):
    result = []
    
    if not matrix or not matrix[0]:
        return []
    
    top , left = 0,0
    bottom , right = len(matrix)-1,len(matrix[0])-1
    
    while top <=bottom and left <= right:
        for i in range(left,right+1):
            result.append(matrix[top][i])
        top+=1
        
        for i in range(top,bottom+1):
            result.append(matrix[i][right])
        right -=1 
        
        if top <= bottom:
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])
            bottom -=1
            
        if left <= right :
            for i in range(bottom,top-1,-1):
                result.append(matrix[i][left])
            left +=1
            
    return result

spiral_matrix = print_spiral_matrix(matrix)
print(spiral_matrix)