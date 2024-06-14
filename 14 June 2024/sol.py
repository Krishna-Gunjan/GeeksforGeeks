class Solution:
    def armstrongNumber (self, n):
      
        ans = n
        
        for _ in range(3):
            ans -= (n % 10) ** 3
            n //= 10
        
        return "true" if ans == 0 else "false"
