#! /usr/bin/env python3


from math import sqrt
from itertools import chain


def iterable_and_iter(obj):
    iterator = iter(obj)
    print(f"Iterable: {obj}")
    try:
        print(f"{next(iterator)} = next(iterator)")
        print(f"{next(iterator)} = next(iterator)")
        print(f"{next(iterator)} = next(iterator)")
        print(f"{next(iterator)} = next(iterator)")
        print(f"{next(iterator)} = next(iterator)")
    except StopIteration as identifier:
        print("Nothing more to iterate, got the StopIteration exception")
    finally:
        print("Done")


def first_from_series(iterable):
  iterator = iter(iterable)
  try:
    return next(iterator)
  except StopIteration as err:
    raise ValueError("iterable is empty")


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def any_primes_between(x, y):
    return any(is_prime(x) for x in range(x, y))



def examples_using_any():
    print(f"any_primes_between(1, 10): {any_primes_between(1, 10)}")
    print(f"any_primes_between(123, 200): {any_primes_between(123, 200)}")
    print(f"any_primes_between(1328, 1361): {any_primes_between(1328, 1361)}")


def all_are_primes(data):
    return all(is_prime(x) for x in data)


def all_are_proper_nouns(data):
    return all(name == name.title() for name in data)


def examples_using_all():
    all_primes = [3, 5, 7, 11]
    possible_primes = all_primes + [12, 13]
    print(f"all_are_primes({all_primes}):",
          all(is_prime(x) for x in all_primes))
    print(f"all_are_primes({possible_primes}):",
          all(is_prime(x) for x in possible_primes))

    cities = ['London', 'New York', 'Sydney']
    print(f"all_are_proper_nouns({cities}):",
          all_are_proper_nouns(cities))
    cities += ['boston']
    print(f"all_are_proper_nouns({cities}):",
          all_are_proper_nouns(cities))



def using_zip_to_multi_iterate(data1, data2):
    # returns tuples that are elements from each collections,
    # and stops when one of the collections runs out
    for item in zip(data1, data2):
        print(f"using_zip_to_dual_iterate() item: {item}")


def examples_using_zip():
    print("--- same size collections via zip")
    data1 = ['a', 'b', 'c', 'd']
    data2 = [1, 2, 3, 4]
    using_zip_to_multi_iterate(data1, data2)
    print("--- small/large collections via zip")
    using_zip_to_multi_iterate(data1, data2 + [201, 202, 203])
    print("--- large/small collections via zip")
    using_zip_to_multi_iterate(data1 + [101, 102, 103], data2)


def chaining_iterables():
    print("Chaining iterables is a lazy form of append,",
          "providing a form of super-iterator that moves",
          "from one iterable to the next.")
    letters = ['a', 'b', 'c']
    numbers = range(0, 11)
    booleans = {True, False}
    lists = [ ['foo', 'bar'], ['spam', 'eggs'] ]
    values = chain(letters, numbers, booleans, lists)

    for value in values:
        print(value)


def main():
    iterable_and_iter(['Spring', 'Summer', 'Autumn', 'Winter'])
    first_from_series(['A', 'B', 'C'])
    first_from_series(['1'])
    try:
        first_from_series([])
    except Exception as err:
        print("Error when attempting first_from_series([])", err)

    examples_using_any()
    examples_using_all()
    examples_using_zip()

    chaining_iterables()

    

if __name__ == '__main__':
    main()
