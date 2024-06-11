
from typing import List

class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        
        tips = [(abs(arr[i] - brr[i]), arr[i], brr[i], i) for i in range(n)]

        tips.sort(reverse=True, key=lambda x: x[0])
        
        total_tips = 0
        A_turn = 0
        B_turn = 0
        
        for diff, a, b, i in tips:
            if (a >= b and A_turn < x) or B_turn >= y:
                total_tips += a
                A_turn += 1
                
            else:
                total_tips += b
                B_turn += 1
        
        return total_tips
