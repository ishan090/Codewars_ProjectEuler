# Uses Euler's method (I think) of finding relatively prime numbers to determine
# if two numbers are relatively prime

# What does it mean for two numbers to be relatively prime?
# -> They must not have factors in common.

# Imports
import random

def euler_rel_prime(a, b):
    """
    Given two number a and b, assumes a is the larger one of the two    
    """
    if a != max(a, b):
       a, b = b, a 
    while a != b and b != 0:
        a, b = b, a % b
    if a != 1:
        return False, a
    return True, True

def test_function(times):
    for i in range(times):
        n1, n2 = random.randint(1, 100), random.randint(1, 100)
        print("Testing Euler on", n1, "and", n2, euler_rel_prime(n1, n2))
    return "Task Completed"

if __name__ == "__main__":
    print(euler_rel_prime(999999, 428570))
    # test_function(10)
