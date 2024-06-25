class Solution:
    def rotateMatrix(self, k, mat):

        k = k % len(mat[0])
        
        for i in range(len(mat)):
            
            mat[i] = mat[i][k:] + mat[i][:k]
            
        return mat
