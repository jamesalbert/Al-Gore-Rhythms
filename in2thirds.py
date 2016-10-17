from lib import quicksort
from time import clock
from random import sample

index = 100
gen_start = clock()
unsorted = sample(range(index), index)
gen_end = clock()
print('generating random sample of %s took %s seconds' % (index, gen_end - gen_start))
print('sampling %s' % unsorted)
sort_start = clock()
_sorted = quicksort(unsorted)
sort_end = clock()
print('quick-sorting random sample of %s took %s seconds' % (index, sort_end - sort_start))
print('sorted: %s' % _sorted)

for i, e in enumerate(_sorted):
    if len(unsorted) / 6 <= unsorted.index(e) < 5 * len(unsorted) and \
       len(_sorted) / 6 <= i < 5 * len(_sorted):
        print(True)
    print(False)
