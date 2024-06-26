class Solution:
	def findCoverage(self, matrix):
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        cords = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        coverage = 0
        
        for i in range(rows):
            for j in range(cols):
                
                if matrix[i][j] == 0:
                        
                    for cord in cords:
                        
                        x, y = i + cord[0], j + cord[1]
                        
                        if 0 <= x < rows and 0 <= y < cols:
                            
                            if matrix[x][y] == 1:
                                
                                coverage += 1
                                
        return coverage
