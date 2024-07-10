from typing import List

class Solution:
    def maxSquare(self, n : int, m : int, mat : List[List[int]]) -> int:

        if not mat:
            return 0
            
        rows = len(mat)
        cols = len(mat[0])
        largest_side = 0
        
        dp = [[0] * m for _ in range(n)]
        
        for i in range(rows):
            dp[i][0] = mat[i][0]
            largest_side = max(largest_side, dp[i][0])
            
        for j in range(cols):
            dp[0][j] = mat[0][j]
            largest_side = max(largest_side, dp[0][j])
        
        for i in range(1, rows):
            for j in range(1, cols):
                if mat[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    largest_side = max(largest_side, dp[i][j])
                else:
                    dp[i][j] = 0
        
        return largest_side
