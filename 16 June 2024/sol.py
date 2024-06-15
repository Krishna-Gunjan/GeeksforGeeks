class Solution:
    def getPrimes(self, n : int) -> List[int]:

        if n < 3:
            return [-1, -1]
            
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False 
    
        x = 2
        while (x * x <= n):
            if (prime[x] == True):
                for i in range(x * x, n + 1, x):
                    prime[i] = False
            x += 1

        
        for a in range(2, n):
            if prime[a]:
                b = n - a
                if b >= 2 and prime[b]:
                    return [a, b]
        
        return [-1, -1]
