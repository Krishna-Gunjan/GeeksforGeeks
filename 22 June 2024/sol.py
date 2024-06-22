class Solution:
    
    def ExtractNumber(self,sentence):

        ans = -1
        
        for num in sentence.split():
            
            if num.isdigit() and '9' not in num:
                if ans == -1: ans = int(num)
                else: ans = max(ans, int(num))
                
        return ans
