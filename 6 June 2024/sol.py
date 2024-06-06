def max_sum(a: list[int] ,n: int):

    original_sum = sum(a)
    
    default_sum_without_rotation = sum(i * a[i] for i in range(n))
    
    max_sum = default_sum_without_rotation
    
    current_sum = default_sum_without_rotation
    
    for k in range(1, n):
       
        current_sum = current_sum + original_sum - n * a[n-k]
        
        max_sum = max(max_sum, current_sum)
    
    return max_sum

if '__main__' == __name__:
    print(max_sum([8, 3, 1, 2], 4)) # returns 29
    print(max_sum([1, 2, 3], 3)) # returns 8