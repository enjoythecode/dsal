def _quicksort_internal(arr, lo, hi):
    print(lo, hi)
    if (hi - lo) < 1:
        return None

    pivot = hi
    pivot_val = arr[pivot]
    i = lo
    while i < pivot:
        if arr[i] > pivot_val:
            if i < pivot - 1:
                arr[i], arr[pivot-1], arr[pivot] = arr[pivot-1], arr[pivot], arr[i]
            else:
                arr[i], arr[pivot] = arr[pivot], arr[i]
            pivot -= 1
        else:
            i += 1

    _quicksort_internal(arr, lo, pivot-1)
    _quicksort_internal(arr, pivot+1, hi)

def quicksort(arr):
    _quicksort_internal(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    x = [5, 6,  -1,  3,  7, 1,  2,  -3,  4,  -2,  0,  9,  8]
    quicksort(x)
    print(x)
    print(quicksort([0]))
    print(quicksort([0,  0,  0,  0,  0,  100]))
