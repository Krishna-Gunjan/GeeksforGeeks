def max_sum(a: list[int] ,n: int):

    # Calculate the sum of all elements in array
    original_sum = sum(a)
    
    # Calculate the sum of all elements in array times their index
    default_sum_without_rotation = sum(i * a[i] for i in range(n))
    
    
    max_sum = default_sum_without_rotation
    
    current_sum = default_sum_without_rotation
    
    for k in range(1, n):
       
        # Calculate the sum after rotating the array around the kth index
        current_sum = current_sum + original_sum - n * a[n-k]
        
        # Update the maximum sum
        max_sum = max(max_sum, current_sum)
    
    return max_sum

if '__main__' == __name__:
    print(max_sum([8, 3, 1, 2], 4)) # returns 29
    print(max_sum([1, 2, 3], 3)) # returns 8