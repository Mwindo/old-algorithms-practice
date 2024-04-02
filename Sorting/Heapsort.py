# Heapsort

import random
from time import perf_counter


def get_array():
    sort = []
    for i in range(0, 20000):
        sort.append(random.randint(0, 50000))
    return sort


# how does this work? endindex is just here to make sure we don't go past the end
# what we do: we make sure that the subarray from start[index] to endindex is a heap
# if it is, we return it ("no need to swap!")
# if it is not, we swap the appropriate elements, using the fact that the first child of a parent is parent * 2 + 1
def sift_down(array, start, endindex):
    # really only need endindex on the first iteration since after that child + 1 . . .
    # is guaranteed to be less than endindex
    root = start
    while (root * 2) + 1 <= endindex:
        child = (root * 2) + 1
        swap = root
        if array[swap] < array[child]:
            swap = child
        if child + 1 <= endindex and array[swap] < array[child+1]:
            swap = child + 1
        if swap == root:  # no need to swap!
            return array
        x = array[root]
        array[root] = array[swap]
        array[swap] = x
        root = swap
    return array


# turn an array into a heap
# we start with the last element, get its parent (= last parent), and turn that subarray into a heap
# we continue to do this until we have looped back to the root parent
def heapify(array):
    last = len(array) - 1
    start = int((last-1)/2)  # initialize to last parent
    while start >= 0:
        array = sift_down(array, start, last)
        start -= 1
    return array


def sift_up(array, startindex, endindex):
    child = endindex
    while child > startindex:
        parent = int((child-1)/2)
        if array[parent] < array[child]:
            x = array[parent]
            array[parent] = array[child]
            array[child] = x
            child = parent
        else:
            return array
    return array

def heapify_up(array):
    end = 1  # first child
    while end < len(array):
        sift_up(array, 0, end)
        end += 1
    return array


# turn the array into a heap
# we know that a[0] is the largest element, so we put that at the end
# then we reduce the end by 1, reheapify, and repeat
def heap_sort(array):
    array = heapify(array)
    end = len(array) - 1
    while end > 0:
        x = array[end]
        array[end] = array[0]
        array[0] = x
        end -= 1
        array = sift_down(array, 0, end)
    return array


def heap_sort_up(array):
    array = heapify_up(array)
    end = 1
    while end < len(array)-1:
        x = array[end]
        array[end] = array[0]
        array[0] = x
        end += 1
        array = sift_up(array, 0, end)  # note that this will not work! does not repair damaged heap
    return array


def test():
    array = get_array()
    # array = heapify(array)
    heap_sort(array)
    for i in array:
        print(i)


test()