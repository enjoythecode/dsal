def partition(arr, lo, hi):
    pivot_i = lo
    pivot = arr[lo]

    while lo < hi:

        lo += 1
        while arr[lo] <= pivot:
            lo += 1

        hi -= 1
        while arr[hi] > pivot:
            hi -= 1

        # swap
        if lo < hi:
            arr[lo], arr[hi] = arr[hi], arr[lo]
    
    arr[pivot_i], arr[hi] = arr[hi], arr[pivot_i]
    return hi

def quicksort(arr, lo, hi):
    if lo < hi:
        k = partition(arr, lo, hi)
        quicksort(arr, lo, k)
        quicksort(arr, k+1, hi)

def sort(l):
    arr = l + [float("inf")]
    quicksort(arr, 0, len(l))
    return arr[:-1]


print(sort([5, 6,  -1,  3,  7, 1,  2,  -3,  4,  -2,  0,  9,  8]))
print(sort([0]))
print(sort([0,  0,  0,  0,  0,  100]))