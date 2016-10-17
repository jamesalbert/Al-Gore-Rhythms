def quicksort(a):
    pivot = len(a) - 1
    wall = 0
    left, middle, right = [], [], []
    for e in a[wall:pivot+1]:
        if a[pivot] > e:
            left.append(e)
            wall += 1
        if a[pivot] < e:
            right.append(e)
        if a[pivot] == e:
            middle.append(e)
    if left:
        left = quicksort(left)
    if right:
        right = quicksort(right)
    return left + middle + right


