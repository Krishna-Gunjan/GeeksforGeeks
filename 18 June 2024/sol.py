class Solution:
    def rectanglesInCircle(self,r):

      rectangles = 0
        max_length = 2 * r
        
        for i in range(1, max_length + 1):
            for j in range(1, max_length + 1):
                if i * i + j * j <= 4 * r * r:
                    rectangles += 1
                    
        return rectangles
