'''
Computing mandelbrot sets.
'''

import math


def mandel(real, imag):
    '''
    Compute a point in the mandelbrot set.

    The logarithm of number of iterations needed
    to determine whether a complex point is in the
    mandelbrot set.

    Args:
      real: the real coordinate
      imag: the imaginary coordinate

    Returns:
      An integer in the range 1-255
    '''
    x = 0
    y = 0
    for i in range(1, 257):  # need 256, and remember, range is exclusive on the right
        if x*x + y*y > 4.0:
            break
        xt = real + x*x - y*y
        y = imag + 2.0 * x * y
        x = xt
    return int(math.log(i) * 256 / math.log(256)) - 1


def mandelbrot(size_x, size_y):
    '''
    Generate a mandelbrot set image

    Args:
      size_x: image width
      size_y: image height

    Returns:
      A list of lists of integers in the range 0-255.
    '''
    # nested list comprehensions to generate lists of lists of integers
    return [[mandel((3.5 * x / size_x) - 2.5,
                    (2.0 * y / size_y) - 1.0)
             for x in range(size_x)]
            for y in range(size_y)]
