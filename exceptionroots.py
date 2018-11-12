#! /usr/bin/env python3


def sqrt(x):
    '''Compute square roots using the method of Heron of Alexandria.
    
    The approach here is EAFP: easier to ask forgiveness than permission, 
    meaning just try to do the work and throw/handle exceptions instead
    of littering the code with preflight if statements and such.

    Args:
      x: The number for which the square root is to be computed.

    Returns:
      The square root of x
    
    Raises:
      ValueError: if x is negative
    '''
    if x < 0:
        raise ValueError("Cannot compute square root of negative number {}".format(x))

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x/guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print("This is never printed")
    except ZeroDivisionError:
        print("Cannot compute square root of a negative number.")
    except ValueError:
        print("sqrt() let us know that it can't deal with negative numbers")
    print("Program execution continues normally here.")


if __name__ == '__main__':
    main()
