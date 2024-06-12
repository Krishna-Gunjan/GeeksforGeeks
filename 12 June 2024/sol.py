class Solution:
    def countNumberswith4(self, n : int) -> int:
      
        result = 0
        
        for i in range(4, n+1):
            if '4' in str(i):
                result += 1
        
        return result
