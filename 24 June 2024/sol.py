class Solution:
    def sumMatrix(self, n, q):

        if q < 0 or q > 2 * n: return 0
            
        s, e = max(1, q - n), min(n, q - 1)
        
        return e - s + 1 if s <= e else 0
