def sort(arr):
    sorted_until = 0

    while sorted_until < len(arr) - 1:
        minimum = arr[sorted_until]
        swap = sorted_until
        for i in range(sorted_until + 1, len(arr)):
            if arr[i] < minimum:
                swap = i
                minimum = arr[i]
        tmp = arr[swap]
        arr[swap] = arr[sorted_until]
        arr[sorted_until] = tmp

        sorted_until += 1

    return arr

print(sort([5, 6,  -1,  3,  7, 1,  2,  -3,  4,  -2,  0,  9,  8]))
print(sort([0]))
print(sort([0,  0,  0,  0,  0,  100]))


# time complexity: O(n^2)
# space complexity: O(1)  (extra)