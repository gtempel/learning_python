#! /usr/bin/env python3
'''
Generators are quite powerful:

* specify iterable sequences (all generators are iterators)
* are lazy-evaluated (next value is computed on-demand)
* can model infinite sequences (such as streams, active log files, etc)
* are composable into pipelines (for natural stream processing)

Generators are defined as any python function that uses the 'yield'
keyword, temporarily returning a value to the caller AND serving as
an entry point the next time the method is executed.
'''

import sys
from math import sqrt


def wrong_way_to_use_generators():
    print("wrong_way_to_use_generators:----------------")
    # doing this keeps generating a new generator/iterator
    print(next(generator_123()))
    print(next(generator_123()))
    print(next(generator_123()))
    print(next(generator_123()))


def generator_123():
    # actually returns a generator object, which is really an interator
    # each call to this method really creates a new generator function,
    # and each can be advanced separately!
    print("About to yield 1")
    yield 1
    print("About to yield 2")
    yield 2
    print("About to yield 3")
    yield 3
    # implicit return


def use_generator(g):
    print("use_generator:----------------")
    try:
        print(next(g))
        print(next(g))
        print(next(g))
        print(next(g))
    except StopIteration as err:
        print(f"generator is empty: {err}", file=sys.stdout)


def use_generator_in_for_loop(g):
    print("use_generator_in_for_loop------")
    for v in g:
        print(v)


def use_multiple_generators(g1, g2):
    print("use_multiple_generators---------")
    print(f"{next(g1)} = next(g1) # 1st from g1")
    print(f"{next(g1)} = next(g1) # 2nd from g1")
    print(f"{next(g2)} = next(g2) # 1st from g2")
    print(f"{next(g1)} = next(g1) # 3rd from g1")


def first_n_stateful_generator(count, iterable):
    # generators resume execution within the context of the specific generator instance
    # they can maintain state in local variables
    # they can have complex control flow
    # they are lazy evaluation
    counter = 0  # how many elements we've yielded thus far
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def use_first_n_stateful_generator(n, iterable):
    # first n items
    print(f"use_stateful_generator({n}, {iterable})-----------")
    gen = first_n_stateful_generator(n, iterable)
    for index in range(n):
        result = next(gen)
        print(f"{index} item is {result}")


def distinct_generator(iterable):
    '''Return guaranteed unique items, even if the input wasn't
    something like a set.

    Args:
      iterable: the source series

    Yields:
      Unique elements in order from 'iterable'.
    '''
    seen = set()  # this will memoize the things we've seen
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def use_distinct_generator(iterable):
    print("use_distinct_generator-------------")
    # item in (generator operating on the iterable)
    for item in distinct_generator(iterable):
        print(f"encountered {item}")


def pipeline_generators(n, iterable):
    print("pipline_generators-------------")
    # take the first N distinct items from the generator
    # essentially:
    # create a collection of unique items
    # then iterate over the first n of those
    # HOWEVER...
    # what really happens is that an iterator hits an interator hits an iterator,
    # and distinct only ever really examines the first N that's required. This is
    # the lazy evaluation, and is far more efficient than the alternative. Compare
    # this to doing a distinct on the collection, then filtering the first N
    # from that collection.
    for item in first_n_stateful_generator(n, distinct_generator(iterable)):
        print(item)


def generator_comprehension():
    # similar syntax to list comprehensions
    # create generator object
    # concise
    # lazy evaluation
    # syntax is very similar: (exper(item) for item in iterable)  -- note the parens
    # useful for the lazy evalutation of generators with the clarity of comprehensions
    million_squares = (x*x for x in range(1, 1000001))
    # million squares is a generator; nothing has been evaluated or calculated

    # can force evaluation to resolve it, but this would take up a lot of memory,
    # about 40MB
    # list(million_squares)


def big_sum_via_generator_comprehension():
    # let's calculate the sum for the first ten million squares
    # if we generated a list this could be about 400MB of RAM, but
    # by using a generator memory usage is relatively insignificant
    limit = 10000000
    result = sum(x*x for x in range(1, limit+1))
    print(f"sum of the first {limit} squares is {result}")


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def sum_of_primes_less_than_or_equal_to(n):
    result = sum(x for x in range(n + 1) if is_prime(x))
    print(f"sum of the primes <= {n} is {result}")


def any_primes_between(x, y):
  return any(is_prime(x) for x in range(x,y))


def main():
    wrong_way_to_use_generators()

    # what we need to do is actually save the returned generator
    # and use _that_ object via next
    g = generator_123()
    use_generator(g)
    use_generator_in_for_loop(generator_123())
    use_multiple_generators(generator_123(), generator_123())

    use_first_n_stateful_generator(3, [2, 4, 'done', 6, 8, 'too far'])

    use_distinct_generator([1, 3, 3, 5, 5, 5, 7, 9, 9])

    pipeline_generators(3, [1, 3, 3, 5, 5, 5, 7, 9, 9, 11, 13, 15])

    generator_comprehension()
    big_sum_via_generator_comprehension()
    sum_of_primes_less_than_or_equal_to(1000)

    print(f"any_primes_between(1, 10): {any_primes_between(1, 10)}")
    print(f"any_primes_between(123, 200): {any_primes_between(123, 200)}")
    print(f"any_primes_between(1328, 1361): {any_primes_between(1328, 1361)}")




if __name__ == '__main__':
    main()
