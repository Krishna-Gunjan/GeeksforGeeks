class Solution:
    
    def threeSumClosest (self, arr, target):
      
        arr.sort()
        n = len(arr)
        
        closest_sum = float('inf')
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                
                if current_sum == target:
                    return current_sum
                    
                diff_curr_tar = abs(current_sum - target)
                diff_cls_tar = abs(closest_sum - target)
                
                if diff_curr_tar < diff_cls_tar:
                    closest_sum = current_sum
                    
                elif diff_curr_tar == diff_cls_tar:
                    closest_sum = max(closest_sum, current_sum)
                
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum
