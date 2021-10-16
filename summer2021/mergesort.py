def mergesort(arr):

    if len(arr) < 2:
        return arr

    m = len(arr) // 2
    l = mergesort(arr[:m])
    r = mergesort(arr[m:])
    return merge(l,r)

def merge(arr1, arr2): # given two sorted arrays, merge them into one merged array
    ans = []

    l = 0
    r = 0

    while l < len(arr1) and r < len(arr2):
        if arr1[l] < arr2[r]:
            ans.append(arr1[l])
            l += 1
        else:
            ans.append(arr2[r])
            r += 1

    while l < len(arr1):
        ans.append(arr1[l])
        l += 1
    while r < len(arr2):
        ans.append(arr2[r])
        r += 1

    return ans

def sort(arr):
    return mergesort(arr)

print(sort([5, 6,  -1,  3,  7, 1,  2,  -3,  4,  -2,  0,  9,  8]))
print(sort([0]))
print(sort([0,  0,  0,  0,  0,  100]))
print(sort([4, 2]))


# time complexity:
# space complexity: