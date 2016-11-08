
from math import floor


class Heap(object):
    def __init__(self):
        self.heap = []

    def get_child(self, i=0, size=None, left=True):
        c = 2 * i + (1 if left else 2)
        if c < (size if size else len(self)):
            return c
        return None

    def get_parent(self, i):
        if i is 0:
            return None
        else:
            return floor((i - 1) / 2)

    def get_sorted(self):
        tmp = Heap()
        sorted_array = []
        for item in self:
            tmp.insert(item)
        for item in self:
            sorted_array.append(item)
        return sorted_array

    def sort(self):
        self.buildheap()
        heapsize = len(self) - 1
        for i in range(heapsize, -1, -1):
            self[0], self[i] = self[i], self[0]
            self.heapify(0, i)
        return self

    def buildheap(self):
        heapsize = len(self)
        for i in range(heapsize//2, -1, -1):
            self.heapify(i, heapsize)

    def heapify(self, i, heapsize):
        left = self.get_child(i, size=heapsize)
        right = self.get_child(i, size=heapsize, left=False)
        if left is not None and self[left] < self[i]:
            smallest = left
        else:
            smallest = i
        if right is not None and self[right] < self[smallest]:
            smallest = right
        if smallest != i:
            # Swap and tail-recursion
            self[i], self[smallest] = self[smallest], self[i]
            self.heapify(smallest, heapsize)

    def insert(self, item):
        self.heap.append(item)
        self.percolate(len(self) - 1)
        return self

    def swap(self, s, d):
        self[s], self[d] = self[d], self[s]
        return self

    def percolate(self, i):
        p = self.get_parent(i)
        l = self.get_child(i)
        r = self.get_child(i, left=False)
        if i is 0:
            return self
        elif p is not None and self[i] < self[p]:
            s = p
        elif l is not None and self[i] > self[l]:
            s = l
        elif r is not None and self[i] > self[r]:
            s = r
        else:
            return self
        self.swap(i, s)
        self.percolate(p)
        return self

    def delete(self, i):
        self[i] = self[-1]
        del self[-1]
        if i != len(self):
            self.percolate(i)
        return self

    def __len__(self):
        return len(self.heap)

    def __getitem__(self, i):
        print('getting ', i, ' with size ', len(self))
        if i >= len(self):
            raise IndexError('index {0} out of range'.format(i))
        return self.heap[i]

    def __setitem__(self, i, value):
        self.heap[i] = value
        return value

    def __delitem__(self, i):
        del self.heap[i]

    def __str__(self):
        string = [str(self[0])]
        for i in range(len(self)-1):
            l = self.get_child(i)
            r = self.get_child(i, left=False)
            if r is not None:
                string.append(str(self[r]))
            if l is not None:
                string.append(str(self[l]))
        return '[{0}]'.format(', '.join(string))
