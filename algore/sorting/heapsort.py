

def heaplen(a):
    return len(a) - 1


def leftchild(i):
    return 2 * i + 1


def rightchild(i):
    return 2 * i + 2


def heapsort(a):
    buildheap(a)
    heapsize = heaplen(a)
    for i in range(heapsize, -1, -1):
        a[0], a[i] = a[i], a[0]
        heapsize -= 1
        heapify(a, 0, heapsize)


def buildheap(a):
    heapsize = heaplen(a)
    for i in range(heapsize//2, -1, -1):
        heapify(a, i, heapsize)


def heapify(a, i, heapsize):
    left = leftchild(i)
    right = rightchild(i)
    if left <= heapsize and a[left] > a[i]:
        largest = left
    else:
        largest = i
    if right <= heapsize and a[right] > a[largest]:
        largest = right
    if largest != i:
        # Swap and tail-recursion
        a[i], a[largest] = a[largest], a[i]
        heapify(a, largest, heapsize)
