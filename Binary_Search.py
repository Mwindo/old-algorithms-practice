def ret_list():
    ret = [1, 2, 15, 30, 111, 300, 679, 1235]
    return ret


def binary_search(l, val):
    high = len(l) - 1
    low = 0
    while low < high:
        mid = int((high + low) / 2)
        if l[mid] < val:
            low = mid+1
        elif l[mid] > val:
            high = mid - 1
        else:
            return mid
    return -1


def binary_search_recursive(l, val, high=-1, low=-1):
    if high == -1:
        high = len(l) - 1
    if low == -1:
        low = 0
    if low > high:
        return -1
    mid = int((high + low) / 2)
    if l[mid] < val:
        low = mid + 1
    elif l[mid] > val:
        high = mid - 1
    else:
        return mid
    return binary_search_recursive(l, val, high, low)


print(binary_search(ret_list(), 300))

print(binary_search_recursive(ret_list(), 300))

