# Functions that locate a prime inside a list of primes using binary search


def index_prime(n, primes_list, verbose = False):
    """
    Given a list of primes, finds the index of the prime number from
    the primes list thats equal to or greater than n using binary search
    """
    # if n is out of bounds, return the last elment
    if n > primes_list[-1]:
        primes_list[-1]
        raise ValueError(n, "was out of bounds")
    if verbose:
        print("n", n, "was within bounds")
    start = 0
    end = len(primes_list)-1
    mid = round((start + end)/2)
    r = 1
    if verbose:
        print("beginning of round", r, ": (start, end, mid) = ", (start, end, mid))
    while start < end:
        val_mid = primes_list[mid]
        if val_mid == n:
            return mid
        elif n < val_mid:
            end = mid - 1
            log = "to_the_left"
        elif n > val_mid:
            start = mid + 1
            log = "to_the_right"
        mid = round((start + end)/2)
        r += 1
        if verbose:
            print("beginning of round", r, ": (start, end, mid) = ", (start, end, mid))
    # If n < values at end:
    if n > primes_list[start]:
        return start + 1
    else:
        return start



