class Solution:
    def padovanSequence(self, n):
        MOD = 10 ** 9 + 7
        
        if n == 0 or n == 1 or n == 2:
            return 1
        
        third_pointer, second_pointer, first_pointer = 1, 1, 1
        
        for i in range(3, n + 1):
            current = (second_pointer + third_pointer) % MOD
            third_pointer = second_pointer
            second_pointer = first_pointer
            first_pointer = current
        
        return first_pointer
