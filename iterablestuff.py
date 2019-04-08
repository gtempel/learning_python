#! /usr/bin/env python3


from math import sqrt
from itertools import chain
import functools


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
        print(f"Nothing more to iterate, got the StopIteration exception: {identifier}")
    finally:
        print("Done")


def first_from_series(iterable):
  iterator = iter(iterable)
  try:
    return next(iterator)
  except StopIteration as err:
    raise ValueError(f"iterable is empty: {err}")


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


def map_ord(data):
    results = map(ord, data)
    print(f"mapping_ord({data}): {list(results)}")


def map_is_lazy(data):
    class Trace:
        def __init__(self):
            self.enabled = True
   
        def __call__(self, f):
            def wrap(*args, **kwargs):
                if self.enabled:
                    print('Calling {} within map_is_lazy()'.format(f))
                return f(*args, **kwargs)
            return wrap
    
    print(f"map_is_lazy({data}) will now show traces that prove that the mapping is now taking place: ")
    results = map(Trace()(ord), data)
    print(f"{list(results)}")


def map_with_multiple_input_sequences(data1, data2, data3):
    def combine(a, b, c):
        return [a, b, c]

    results = map(combine, data1, data2, data3)
    print(f"map_with_multiple_input_sequences({data1}, {data2}, {data3}): {list(results)}")


def filter_function_returns_items_where_function_returns_true():
    def my_filter(value):
        return not value % 2

    data = range(1, 20)
    results = filter(my_filter, data)
    print(f"filter_function_returns_items_where_function_returns_true() {data} -> {list(results)}")


def filter_lambda_returns_items_where_function_returns_true():
    data = range(1, 20)
    results = filter(lambda x: not x % 2, data)
    print(f"filter_function_returns_items_where_function_returns_true() {data} -> {list(results)}")


def filter_via_none_removes_elements_that_evaluate_to_false():
    data = range(1, 20)
    results = filter(None, [-1, 0, 1, False, True, "a", [], "false", "true", '', 'hello', {}])
    print(f"filter_via_none_removes_elements_that_evaluate_to_false() {data} -> {list(results)}")


def reduce_as_a_summation():
    # interim results passed as first arg, new element as the second
    def my_operation(interim, value):
        print(f"   my_operation({interim}, {value})")
        return interim + value

    # passing an empty sequence will result in a TypeError
    data = range(1, 6)
    results = functools.reduce(my_operation, data)
    print(f"reduce_as_a_summation() {data} -> {results}")


def reduce_with_one_element_never_calls_the_function():
    def my_operation(interim, value):
        print(f"   my_operation({interim}, {value})")
        return interim + value
    
    # passing an empty sequence will result in a TypeError
    data = [1]
    results = functools.reduce(my_operation, data)
    print(f"reduce_with_one_element_never_calls_the_function() {data} -> {results}")


def reduce_with_optional_initial_starting_value():
    def my_operation(interim, value):
        print(f"   my_operation({interim}, {value})")
        return interim + value
    
    # passing an empty sequence will result in a TypeError
    data = range(2,11, 2)
    initial_value = 10
    results = functools.reduce(my_operation, data, initial_value)
    print(f"reduce_with_optional_initial_starting_value() {data} -> {results}")


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

    map_ord('the quick brown fox')
    map_is_lazy('the quick brown fox')
    map_with_multiple_input_sequences(['red', 'orange', 'yellow'],
        [1, 2, 3],
        ['emmet', 'bitsy', 'spike']
        )

    filter_function_returns_items_where_function_returns_true()
    filter_lambda_returns_items_where_function_returns_true()
    filter_via_none_removes_elements_that_evaluate_to_false()

    reduce_as_a_summation()
    reduce_with_optional_initial_starting_value()


if __name__ == '__main__':
    main()
