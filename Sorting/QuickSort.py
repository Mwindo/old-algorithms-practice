# Quicksort
# Plus crappy code to test how long different pivots take

import random
from time import perf_counter


# sort = [1, 5, 6, 71, 9, 176, 3, 8, 0, 4]


def get_array():
    sort = []
    for i in range(0, 200000):
        sort.append(random.randint(0, 500000))
    return sort


sort = get_array()


def pivot_randomized(array):
    index = random.randint(0, len(array) - 1)
    return index


def pivot_first(array):
    return 0


def pivot_last(array):
    return len(array)-1


def pivot_middle(array):
    return int(len(array) / 2)


def pivot_median_of_threes(array):
    f = array[0]
    mi = pivot_middle(array)
    m = array[mi]
    li = pivot_last(array)
    last = array[li]
    if (f > m) != (f > last):
        return 0
    elif (m > f) != (m > last):
        return mi
    return li


def quicksort(array, pivot_func):
    smaller = []
    larger = []
    if len(array) <= 1:
        return array
    pivot_index = pivot_func(array)
    pivot = array[pivot_index]
    pivots = []
    array.pop(pivot_index)
    for i in array:
        if i < pivot:
            smaller.append(i)
        elif i > pivot:
            larger.append(i)
        else:
            pivots.append(i)
    ret = quicksort(smaller, pivot_func)
    ret.extend(pivots)
    ret.extend(quicksort(larger, pivot_func))
    return ret


def test():
    val = quicksort(sort, pivot_median_of_threes)
    for i in val:
        print(i)


def check_sorted(array):
    check = array[0]
    for i in array:
        if i < check:
            return False
        check = i
    return True


def eval_all_once(array):
    pivot_funcs = [pivot_last, pivot_first, pivot_middle, pivot_randomized, pivot_median_of_threes]
    names = ["last: ", "first: ", "middle: ", "random: ", "median: "]
    times = []
    for i in range(0, len(pivot_funcs)):
        p = pivot_funcs[i]
        t1 = perf_counter()
        val = quicksort(array, p)
        # if check_sorted(val) is False:
        #    print("ERROR")
        #    exit(1)
        t2 = perf_counter()
        t_elapsed = t2-t1
        times.append(t_elapsed)
        print(names[i], t_elapsed)
    return times


def eval_all_x_times(x):
    times = [0,0,0,0,0]
    for i in range(0, x):
        sort_this = get_array()
        index = 0
        for j in eval_all_once(sort_this):
            times[index] += j
            index += 1
    for i in range(0, 5):
        print(times[i]/x)


eval_all_x_times(20)


# 0.15853124000000002 with 200000 at 500 -- much faster with pivots as an array;
# slightly faster at 500000 too
# 0.15211415
# 0.157131875
# 0.15862733499999998
# 0.14225800000000016

# original, with ret.append(pivot) rather than ret.extend(pivots)
# 0.3767813199999999 with 200000 at 500000
# 0.38652462500000057
# 0.38690835999999995
# 0.47204398499999983
# 0.3970339350000001

# 0.5506245849999993 with 200000 at 5000
# 0.5638254800000004
# 0.5795241449999997
# 0.6849034999999999
# 0.6086516500000001

# 3.246552810000007 with 200000 at 500
# 3.464538965000004
# 3.653230639999996
# 4.033232155
# 3.7103375899999946
