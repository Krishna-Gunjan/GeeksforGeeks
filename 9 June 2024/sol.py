def zigZag(n : int, arr : list[int]) -> list[int]:
    
    for ind in range(n - 1):
        
        if ind % 2 == 0:
            
            if arr[ind] > arr[ind + 1]:
                arr[ind], arr[ind + 1] = arr[ind + 1], arr[ind]
        
        else:
            
            if arr[ind] < arr[ind + 1]:
                arr[ind], arr[ind + 1] = arr[ind + 1], arr[ind]
                
    return arr
    
def isZigzag(arr: list[int]) -> bool:
    
        f = 1

        for i in range(1, len(arr)):
            
            if f:
                if arr[i - 1] > arr[i]:
                    return False
                    
            else:
                if arr[i - 1] < arr[i]:
                    return False
                    
            f = f ^ 1

        return True

if __name__ == '__main__':
    print(isZigzag(zigZag(n = 7, arr = [4, 3, 7, 8, 6, 2, 1]))) # Returns True
    print(isZigzag(zigZag(n = 5, arr = [4, 7, 3, 8, 2]))) # Returns False
