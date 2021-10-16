def sort(arr):
    
    # i botched this when done based on an explanation

    sorted_until = 1

    while sorted_until < len(arr): # there are still unsorted elements
        marker = arr[sorted_until]
        new_pos = sorted_until - 1

        while arr[new_pos] > marker and new_pos >= 0:
            arr[new_pos + 1] = arr[new_pos]
            new_pos -= 1

        arr[new_pos + 1] = marker

        sorted_until += 1
        
    return arr

print(sort([5, 6,  -1,  3,  7, 1,  2,  -3,  4,  -2,  0,  9,  8]))
print(sort([0]))
print(sort([0,  0,  0,  0,  0,  100]))
print(sort([4, 2]))


# time complexity:
# space complexity: