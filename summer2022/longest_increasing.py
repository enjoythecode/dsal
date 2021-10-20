# longest increasing subsequence of a list

# O(n^2) is simple with DP and 2 for loops
# O(nlogn) is increasing

# following tutorial for intuition, tried to code it up independently
# https://nmanojarray.blogspot.com/2015/10/longest-monotonically-increasing.html

def find_ceil_index(arr, trgt):
    lo, hi = 0, len(arr) - 1

    # TTTTFFFF
    # where (arr[i] < trgt) ? T : F
    # find latest T

    ans = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < trgt:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return ans

def lis(nums):
    cands = [nums[0]]

    for i, num in enumerate(nums):
        if num < cands[0]:
            cands[0] = num
        elif num > cands[-1]:
            cands.append(num)
        else:
            # find the index of the latest end element smaller than num
            k = find_ceil_index(cands, num)
            cands[k+1] = num
    
    return len(cands)

print(lis([12,13,14,15,16,1,2,3,4,5,6,7,8,9])) # 9
print(lis([2, 5, 3, 7, 11, 8, 10, 13, 6])) # 6
print(lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])) # 6