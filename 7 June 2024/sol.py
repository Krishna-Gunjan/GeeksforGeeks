
def maxOccured(n, l, r, maxx):

    # Initialize a hash map to track the occurence
    hashmap = {}

    for i in range(n):

        # Update the Occurences
        hashmap[l[i]] = hashmap.get(l[i], 0) + 1
        hashmap[r[i] + 1] = hashmap.get(r[i] + 1, 0) - 1
    
    current_max = 0
    max_occurred = 0
    current_count = 0
    
    for key in sorted(hashmap.keys()):

        # Calculate the prefix sum
        current_count += hashmap[key]

        if current_count > current_max:
            # Update the max values
            current_max = current_count
            max_occurred = key

    return max_occurred

if '__main__' == __name__:
    print(maxOccured(n = 4, l = [1,4,3,1], r = [15,8,5,4], maxx = 15)) # Returns 4 
    print(maxOccured(n = 5, l = [1,5,9,13,21], r = [15,8,12,20,30], maxx = 30)) # Returns 5