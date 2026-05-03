
from math import floor


def closest(elems, n):
    """
    Given a list of elems, finds the index of the element greater than n
    """

    start = 0
    end = len(elems) - 1

    while start < end:
        mid = floor((start + end) / 2)
        if elems[mid] == n:
            return mid + 1
        elif elems[mid] < n:
            start = mid + 1
        elif elems[mid] > n:
            end = mid

    # print("start and end:", start, end)
    if elems[start] <= n:
        return start + 1
    return start


def inside(elems, n):
    """
    Given a list elems, checks if n is in it using binary search
    """
    
    start = 0
    end = len(elems) - 1

    while start <= end:
        # print("start, end", start, end)
        mid = floor((start + end) / 2)
        if elems[mid] == n:
            return True
        elif elems[mid] < n:
            start = mid + 1
        elif elems[mid] > n:
            end = mid - 1
    
    return False




if __name__ == "__main__":
    print(closest([0, 1, 2, 3], 5))
    # print(([], 6))


