def isToeplitz(mat):
  
    rows = len(mat)
    cols = len(mat[0])
    
    for row in range(1, rows):
        for col in range(1, cols):
          
            if mat[row][col] != mat[row - 1][col - 1]:
                return False
              
    return True
