# Having to do with triangular numbers

# Imports
from math import sqrt

def gen_nums(n):
    """
    Generates the first n triangular numbers   
    """
    x = 1
    while x <= n:
        yield x*(x+1)/2


def n_th(n):
    return n*(n+1)/2


def check_triangular(n):
    """ 
    Checks if a number n is triangular. Returns true if true,
    else false    
    """
    num = (-1 + sqrt(1 + 8*n)) / 2
    val = (-1 + sqrt(1 + 8*n)) % 2
    return val == 0, num


if __name__ == "__main__":
    print(n_th(3898125))
    print(check_triangular(45))

