def mergesort(arr):
    if len(arr) < 2:
        return arr

    mid = (len(arr) + 1) // 2
    #print(arr, arr[:mid], arr[mid:])
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    l = 0
    r = 0

    new_arr = []

    while l < len(left) or r < len(right):
        if l == len(left):
            new_arr.append(right[r])
            r += 1
            continue
        if r == len(right):
            new_arr.append(left[l])
            l += 1
            continue
        if left[l] < right[r]:
            new_arr.append(left[l])
            l += 1
        else:
            new_arr.append(right[r])
            r += 1

    return new_arr


if __name__ == "__main__":
    arr1 = [5, 6,  -1,  3,  7, 1,  2,  -3,  4,  -2,  0,  9,  8]
    arr2 = [0]
    arr3 = [100,  0,  0,  0,  0,  -100]

    print(mergesort(arr1))
    print(mergesort(arr2))
    print(mergesort(arr3))
