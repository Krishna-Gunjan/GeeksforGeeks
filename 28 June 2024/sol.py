class Solution:
    def pattern (self, arr):

        rows = len(arr)
 
        for i in range(rows):
            
            if arr[i] == arr[i][::-1]:
                
                return "{} R".format(i)
                
        for i in range(rows):
            
            if all(arr[j][i] == arr[rows - j - 1][i] for j in range(rows // 2)):
                
                return "{} C".format(i)
                
        return "-1"
                
