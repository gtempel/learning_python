#! /usr/bin/env python3
"""Experiments with python tuple collections, which
are heterogeneous immutable sequences of objects

Objects cannot be added/removed/replaced.
"""


def print_tuple(t):
    print("----- Some info on this tuple ----------")
    print(type(t))
    print("length: ", len(t))
    if t:
        print("first: ", t[0])
        print("each item:")
        for item in t:
            print(item)
    else:
        print("it's empty")


def minmax(items):
    return min(items), max(items)


def tuple_unpacking(sample_data):
    # like ruby, python has tuple unpacking, which breaks the returned
    # tuple up into separate items
    print("--- tuple unpacking")
    lower, upper = minmax(sample_data)
    print('lower: ', lower)
    print('upper: ', upper)


def tuple_swap():
    # tuple unpacking works with nested tuples, but not other structures
    # It also allows for this very pythonesque variable swap:
    print("--- tuple swap")
    a = "foo"
    b = "bar"
    print("a is ", a)
    print("b is ", b)
    b, a = a, b
    print("a is now ", a)
    print("b is now ", b)


def main():
    t = ("Norway", 4.953, 3)
    print_tuple(t)
    s = ('foo', "bar", 123)
    print_tuple(s + t)
    nested = ((1, 2, 3), ('four', 'five', 'six'), ['a', 'b', 'c'])
    print_tuple(nested)
    # can't do (391) for a single item tuple, as python thinks
    # this is just an integer, so need to use the trailing
    # comma separator
    single_tuple = (391,)
    print_tuple(single_tuple)
    # empty tuples are just empty parens
    print_tuple(())
    # parens can be omitted as well, but it might help to have them just so
    # readers know it's a tuple and not a list of some sort
    bare_tuple = 1, 2, 3, 4, 5
    print_tuple(bare_tuple)

    sample_data = [10, 2, 22, -4, 0, 19, -1]

    # tuples can be created from other collections via the tuple() constructor
    print_tuple(tuple(sample_data))
    print_tuple(tuple("Emmet"))

    # tuples are often used to return multiple items from a function--think
    # like the ruby multiple return values!
    min_max = minmax(sample_data)
    print_tuple(min_max)

    tuple_unpacking(sample_data)
    tuple_swap()

    # test for inclusion
    print("--------test for inclusion")
    sample_tuple = tuple(sample_data)
    print("0 in ", sample_tuple, 0 in sample_tuple)

    # test for exclusion
    print("--------test for exclusion")
    print("5 not in ", sample_tuple, 5 in sample_tuple)


if __name__ == '__main__':
    # refactored body to a method which could then be tested separately
    main()  # 0 is the module filename
