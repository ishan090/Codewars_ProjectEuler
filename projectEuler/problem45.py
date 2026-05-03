

from math import sqrt


def hexagonal(n):
    """
    returns the nth hexagonal number
    """
    return n * (2 * n - 1)

def triangle(n):
    """
    returns the nth triangular number
    """
    return n * (n + 1) / 2

def pentagonal(n):
    """
    returns the nth pentagonal number
    """
    return n * (3 * n - 1) / 2

def is_triag(n):
    """
    determines if n is triangular
    """
    return sqrt(1 + 4 * 2 * n) % 2 == 1

def is_pent(n):
    """
    determines if n is pentagonal
    """
    return sqrt(1 + 4 * 2 * 3 * n) % 6 == 5

def is_hex(n):
    """
    determines if n is triangular
    """
    return sqrt(1 + 4 * 2 * n) % 4 == 3

def main():
    """
    finds numbers that are triangular, hexangonal and pentagonal
    """
    x = 1
    while True:
        h = hexagonal(x)
        if is_pent(h) and is_triag(h):
            print("FOUND:", h)
        x += 1


if __name__ == "__main__":
    main()

