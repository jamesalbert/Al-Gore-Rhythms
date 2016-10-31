def merge(a, b):
    to_return = []
    while True:
        if not (a and b):
            to_return += b if not a else a
            break
        to_return.append(min(a[0], b[0]))
        (a if to_return[-1] == a[0] else b).pop(0)
    return to_return

def mergesort(c):
    i = int(len(c)/2)
    d, e = c[:i], c[i:]
    if (len(d) >= 2):
        d = mergesort(d)
    if (len(e) >= 2):
        e = mergesort(e)
    return merge(d, e)

