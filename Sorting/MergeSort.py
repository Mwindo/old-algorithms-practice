# Merge Sort

import random


def get_array():
    sort = []
    for i in range(0, 20000):
        sort.append(random.randint(0, 50000))
    return sort


def merge(left, right):
    retList = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            retList.append(left[0])
            del left[0]
        else:
            retList.append(right[0])
            del right[0]
    for i in left:
        retList.append(i)
    for i in right:
        retList.append(i)
    return retList


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = int(len(array)/2)
    left = array[:mid]
    right = array[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def test():
    array = get_array()
    for i in merge_sort(array):
        print(i)


test()