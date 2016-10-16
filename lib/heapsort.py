from math import floor

heapsize = 0
largest = 0

def heapsort(a):
    global heapsize
    a = buildheap(a)
    for i in range(len(a)-1, 1, -1):
        tmp = a[i]
        a[i] = a[0]
        a[0] = tmp
        heapsize -= 1
        a = heapify(a, 1)
    print(a)
    return a

def buildheap(a):
    global heapsize
    heapsize = len(a) - 1
    for i in range(floor(heapsize/2), 0, -1):
        a = heapify(a, i)
    return a

def heapify(a, i):
    global heapsize
    left = 2 * i + 1
    right = 2 * i + 2
    if left <= heapsize and a[left] > a[i]:
        largest = left
    else:
        largest = i
    if right <= heapsize and a[right] > a[largest]:
        largest = right
    if largest != i:
        tmp = a[i]
        a[i] = a[largest]
        a[largest] = tmp
        a = heapify(a, largest)
    return a
