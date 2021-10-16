def quicksort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quicksort(arr,lo,p - 1)
        quicksort(arr,p + 1,hi)

    return arr

def partition(arr, lo, hi):
    pivot = arr[hi]

    i = lo
    for j in range(lo, hi):
        if pivot > arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i += 1
    
    arr[hi] = arr[i]
    arr[i] = pivot
    return i

def sort(arr):
    return quicksort(arr,0, len(arr) - 1)

print(sort([5, 6,  -1,  3,  7, 1,  2,  -3,  4,  -2,  0,  9,  8]))
print(sort([0]))
print(sort([0,  0,  0,  0,  0,  100]))
print(sort([4, 2]))


# time complexity:
# space complexity: