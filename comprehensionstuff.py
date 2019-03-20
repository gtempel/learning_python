#! /usr/bin/env python3

from math import factorial, sqrt


def length_of_first_n_factorials(n):
    results = [len(str(factorial(x))) for x in range(n)]
    print(f"Length of each of the first {n} factorials: {results}")


def dictionary_comprehension_to_swap_keys_and_values(dictionary_data):
    # ordinarily you iterate over the keys, but we want keys and items
    # so must use the items() method on the dict
    swapped = {value: key for key, value in dictionary_data.items()}
    print(f"Capitals => Countries: {swapped}")


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def find_all_primes_less_than_or_equal_to(n):
    results = [x for x in range(101) if is_prime(x)]
    print(f"Primes <= {n}:", results)


def comprehensions_with_multiple_sequences(sequence_a, sequence_b):
    # read this like nested for loops, where the comprehension is
    # "executed" within the innermost/rightmost for loop
    #
    # the results container is created atomically -- it works or doesn't
    results = [(x,y) for x in sequence_a for y in sequence_b]
    print(f"comprehensions from multiple sequences: ", results)


def comprehensions_with_multiple_if_clauses_and_multiple_sequences(sequence_a, sequence_b):
    # read this like nested for loops, with the if clauses within the
    # respective loop(s)
    # results = [ x / (x - y) for x in sequence_a if x > 50 for y in sequence_b if x-y != 0]
    results = [ x / (x - y) 
        for x in sequence_a 
        if x > 50 
        for y in sequence_b 
        if x-y != 0]
    print(f"comprehensions from multiple if clauses and multiple sequences: ", results)


def nested_comprehensions(sequence_a):
    results = [[ y * 3 for y in range(x)] for x in sequence_a]
    print(f"nested comprehensions: ", results)


def main():
    length_of_first_n_factorials(20)

    country_to_capital = {
        'United Kingdom': 'London',
        'Brazil': 'Brazilia',
        'Morocco': 'Rabat',
        'Sweden': 'Stockholm',
        'USA': 'Washington DC'
    }
    dictionary_comprehension_to_swap_keys_and_values(country_to_capital)

    find_all_primes_less_than_or_equal_to(101)

    comprehensions_with_multiple_sequences(range(3), range(4))
    comprehensions_with_multiple_if_clauses_and_multiple_sequences(range(100), range(100))
    nested_comprehensions(range(10))


if __name__ == '__main__':
    main()
