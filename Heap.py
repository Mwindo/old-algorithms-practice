# Heap

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