def sort(arr):
    lo = 0
    hi = len(arr) - 1
    
    is_sorted = False
    while not is_sorted and lo < hi:
        is_sorted = True
        for i in range(lo, len(arr) - 1):
            if arr[i] > arr[i+1]:
                is_sorted = False
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp 
        
    return arr

print(sort([5, 6,  -1,  3,  7, 1,  2,  -3,  4,  -2,  0,  9,  8]))
print(sort([0]))
print(sort([0,  0,  0,  0,  0,  100]))


# time complexity:
# space complexity: