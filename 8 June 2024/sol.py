def findExtra(n: int, a : list[int], b : list[int]):
    
    left = 0
    right = n - 1
  
    while left < right:
      
        mid = (right + left) // 2
      
        if a[mid] == b[mid]:
            left = mid + 1   
        else:
           right = mid
          
    return left 

if __name__ == '__main__':
    print(findExtra(n = 7, a = [2,4,6,8,9,10,12], b = [2,4,6,8,10,12])) # returns 4
    print(findExtra(n = 6, a = [3,5,7,8,11,13], b = [3,5,7,11,13])) # returns 3
