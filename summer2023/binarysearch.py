NOT_FOUND_VALUE = -1
def binarysearch_index(arr, target):
    '''
    Simple Binary Search implementation: return the index of target in arr, and
    if not found, return -1.

    arr is assumed to be sorted.
    '''

    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mi = lo + (hi - lo) // 2
        if arr[mi] == target:
            return mi
        if arr[mi] > target:
            hi = mi - 1
        else:
            lo = mi + 1

    # if not found, return null value
    return NOT_FOUND_VALUE

def binarysearch_leq(arr, target):
    '''
    Modified binary search that returns the index of the greatest element in arr
    that is less than or equal to target. Returns -1 if no such elements

    arr is assumed to be sorted.
    '''
    lo, hi = 0, len(arr) - 1

    largest_valid_index = -1
    while lo <= hi:
        mi = lo + (hi - lo) // 2
        if arr[mi] <= target:
            largest_valid_index = mi
            # keep searching to the right regardless...
            lo = mi + 1
        else:
            hi = mi - 1

    return largest_valid_index

if __name__ == "__main__":
    print("Testing simple binary search")
    f = binarysearch_index
    assert f([], 0) == NOT_FOUND_VALUE
    assert f([0,1,2,3,4,5,6,7,8,9,10], 4) == 4
    assert f([1,5,7,10], 8) == NOT_FOUND_VALUE
    assert f([1,2,3,10000000], 3) == 2

    print("Testing upper bound binary search")
    f = binarysearch_leq
    assert f([], 0) == NOT_FOUND_VALUE
    assert f([0,1,2,3,4,5,6,7,8,9,10], -100) == NOT_FOUND_VALUE
    assert f([0,1,2,3,4,5,6,7,8,9,10], 100) == 10
    assert f([1,5,7,10], 3) == 0
    assert f([1,2,3,10000000], 3) == 2
    print("Tests pass")
