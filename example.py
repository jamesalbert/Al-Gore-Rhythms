from random import sample
from lib import mergesort, quicksort, heapsort
from time import clock


for i in range(7):
    index = int('1' + '0' * i)
    gen_start = clock()
    unsorted = sample(range(index), index)
    gen_end = clock()
    print('generating random sample of %s took %s seconds' % (index, gen_end - gen_start))
    sort_start = clock()
    quicksort(unsorted)
    sort_end = clock()
    print('quick-sorting random sample of %s took %s seconds' % (index, sort_end - sort_start))
    sort_start = clock()
    mergesort(unsorted)
    sort_end = clock()
    print('merge-sorting random sample of %s took %s seconds' % (index, sort_end - sort_start))
    # sort_start = clock()
    # heapsort(unsorted)
    # sort_end = clock()
    # print('heap-sorting random sample of %s took %s seconds' % (index, sort_end - sort_start))
