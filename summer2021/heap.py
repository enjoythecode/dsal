# Binary Min Heap

class Heap:
    def __init__(self):
        self.arr = []
    
    def add(self, el):
        self.arr.append(el)
        this = len(self.arr) - 1
        par = (this - 1) // 2
        while par >= 0 and self.arr[par] > self.arr[this]:
            self.arr[par], self.arr[this] = self.arr[this], self.arr[par]
            this = par
            par = (this - 1) // 2

    def get_min(self):
        return self.arr[0]

    def pop(self):
        return self.delete(0)
    
    def delete(self, ind):
        self.arr[len(self.arr) - 1], self.arr[ind] = self.arr[ind], self.arr[len(self.arr) - 1]
        x = self.arr.pop()
        self.heapify(ind)
        return x

    def heapify(self, ind):
        l = ind * 2 + 1
        r = ind * 2 + 2
        smallest = ind

        if l < len(self.arr) and self.arr[l] < self.arr[smallest]:
            smallest = l
        if r < len(self.arr) and self.arr[r] < self.arr[smallest]:
            smallest = r

        if not smallest == ind:
            self.arr[smallest], self.arr[ind] = self.arr[ind], self.arr[smallest]
            self.heapify(smallest)

    def __str__(self):
        return str(self.arr)

bhm = Heap()
bhm.add(6)
bhm.add(1)
bhm.add(7)
bhm.add(5)
bhm.add(8)
bhm.add(4)
bhm.add(3)
bhm.add(2)
bhm.add(0)
print(bhm)
while bhm.arr:
    print(bhm.pop())