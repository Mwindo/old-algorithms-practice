# Selection Sort

import random
from time import perf_counter


def get_array():
    sort = []
    for i in range(0, 20000):
        sort.append(random.randint(0, 50000))
    return sort


def selection_sort_recursive(array, count):
    if count <= 1:
        return array
    cur = 0
    for i in range(1, count):
        if array[i] > array[cur]:
            cur = i
    x = array[cur]
    array[cur] = array[count-1]
    array[count-1] = x
    return selection_sort_recursive(array, count-1)


def find_index_of_max_element(array):
    ret = 0
    for i in range(0, len(array)):
        if array[i] > array[ret]:
            ret = i
    return ret


def find_index_of_min_element(array):
    ret = 0
    for i in range(1, len(array)):
        if array[i] < array[ret]:
            ret = i
    return ret


def selection_sort_alt(array): #slower
    count = len(array)
    for i in range(0, count):
        max_index = find_index_of_max_element(array[:count-i-1])
        if i != max_index:
            x = array[count-i-1]
            array[count-i-1] = array[max_index]
            array[max_index] = x
    return array


def selection_sort(array):
    for i in range(0, len(array)-1):
        mini = i
        for j in range(i+1, len(array)):
            if array[j] < array[mini]:
                mini = j
        if mini != i:
            x = array[i]
            array[i] = array[mini]
            array[mini] = x
    return array


def test():
    array = get_array()
    t1 = perf_counter()
    test1 = selection_sort(array)
    t2 = perf_counter()
    test2 = selection_sort_alt(array)
    t3 = perf_counter()
    test1_elapsed = t2-t1
    test2_elapsed = t3-t2
    print(test1_elapsed, test2_elapsed)
    #for i in selection_sort_alt(array):
    #    print(i)


test()