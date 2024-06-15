class Solution:
    def __init__(self):
        self.st = set()
        self.ar = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["*", "0", "*"]
        ]
    
    def solve(self, i, j, n, track, temp, dp):
        if self.ar[i][j] == "*":
            return 0
        if track == n:
            if temp not in self.st:
                self.st.add(temp)
                return 1
            return 0
        if dp[track][i][j] != -1:
            return dp[track][i][j]
        
        left = right = up = down = 0
        curr = self.solve(i, j, n, track + 1, temp + self.ar[i][j], dp)
        
        if j - 1 >= 0:
            left = self.solve(i, j - 1, n, track + 1, temp + self.ar[i][j - 1], dp)
        if j + 1 < 3:
            right = self.solve(i, j + 1, n, track + 1, temp + self.ar[i][j + 1], dp)
        if i - 1 >= 0:
            up = self.solve(i - 1, j, n, track + 1, temp + self.ar[i - 1][j], dp)
        if i + 1 < 4:
            down = self.solve(i + 1, j, n, track + 1, temp + self.ar[i + 1][j], dp)
        
        ans = curr + left + right + up + down
        dp[track][i][j] = ans
        return ans
    
    def getCount(self, n):
        dp = [[[-1 for _ in range(3)] for _ in range(4)] for _ in range(n + 1)]
        count = 0
        for i in range(4):
            for j in range(3):
                count += self.solve(i, j, n, 1, self.ar[i][j], dp)
        return count
