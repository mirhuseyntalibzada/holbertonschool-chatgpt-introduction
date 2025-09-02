#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    Parameters
    ----------
    n : int
        The number for which the factorial is to be calculated. 
        Must be a non-negative integer.

    Returns
    -------
    int
        The factorial of the input number `n`.
        Returns 1 if n == 0 (base case).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))

print(f)