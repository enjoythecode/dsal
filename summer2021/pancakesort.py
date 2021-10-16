def flip(arr, k):
    lo = 0
    hi = k - 1

    while lo < hi:
        tmp = arr[lo]
        arr[lo] = arr[hi]
        arr[hi] = tmp
        lo += 1
        hi -= 1

def sort(arr):
    sorted_from = len(arr)
    while sorted_from > 0:
        max_id = 0
        for i in range(sorted_from):
            if arr[i] > arr[max_id]:
                max_id = i
        
        flip(arr, max_id + 1)
        flip(arr, sorted_from)

        sorted_from -= 1

    return arr
    

print(sort([5, 6,  -1,  3,  7, 1,  2,  -3,  4,  -2,  0,  9,  8]))
print(sort([0]))
print(sort([0,  0,  0,  0,  0,  100]))
print(sort([4,2]))


# time complexity: O(n^2)
# space complexity: O(1)  (extra)