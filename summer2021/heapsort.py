import heap

def sort(arr):
    h = heap.Heap()
    for el in arr:
        h.add(el)
    
    return [h.pop() for _ in range(len(arr))]
    
print(sort([5, 6,  -1,  3,  7, 1,  2,  -3,  4,  -2,  0,  9,  8]))
print(sort([0]))
print(sort([0,  0,  0,  0,  0,  100]))
print(sort([4,2]))