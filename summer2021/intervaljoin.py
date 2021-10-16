# given a list of unsorted intervals, join all overlapping intervals

def intervaljoin(ints):
    if not len(ints):
        return []


    ints.sort(key = lambda x: x[0])
    ans = [ints[0]]
    for it in ints[1:]:
        if it[0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], it[1])
        else:
            ans.append(it)

    return ans

print(intervaljoin([[1,3], [2,4], [5,7], [6,8]]))