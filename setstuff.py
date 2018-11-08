#! /usr/bin/env python3
"""Experiments with python sets, which
are unordered collections of unique
immutable objects. The set is mutable,
the objects aren't.

The collections implement 'protocols', which are
like interfaces, and classes implementing protocols
must support the operations of those protocols.

Collections implement:
    container
    sized
    iterable

Most of the collections are also sequences (however,
set and dict aren't sequences).

Other protcols:
  sequence (str, list, range, tuple, bytes)
  mutable sequence (list)
  mutable set (set)
  mutable mapping (dict)
  
"""


def print_set(s):
    print("-- Some info on this set: ")
    print(type(s))
    print("length: ", len(s))
    if s:
        for item in s:
            print(item)
    else:
        print("it's empty")


def literal_set():
    print("--- literal set")
    s = {1, 3, 5, 7, 9, 1, 1, 1, 3}
    print_set(s)


def empty_set():
    print("--- empty set")
    s = {}
    print_set(s)

    print("oops, that didn't work (see above), it thinks it's a dict, so use set() constructor")
    s = set()
    print_set(s)


def iterable_to_set(iterable_data):
    print("--- iterable_to_set...duplicates are discarded")
    s = set(iterable_data)
    print_set(s)


def membership_in_set(iterable_data, probe_value):
    print("--- membership in set: probing for", probe_value)
    s = set(iterable_data)
    print(f"{probe_value} in {s}: {probe_value in s}")


def membership_not_in_set(iterable_data, probe_value):
    print("--- membership NOT in set: probing for", probe_value)
    s = set(iterable_data)
    print(f"{probe_value} in {s}: {probe_value not in s}")


def adding_to_set(iterable_data, item_to_add):
    print("--- adding to set", item_to_add)
    s = set(iterable_data)
    s.add(item_to_add)
    print_set(s)


def adding_several_to_set(iterable_data, iterable_collection):
    print("--- adding_several_to_set", iterable_collection)
    s = set(iterable_data)
    s.update(iterable_collection)
    print_set(s)


def removing_from_set(iterable_data, item_to_remove):
    print("--- removing_from_set", item_to_remove)
    s = set(iterable_data)
    try:
        s.remove(item_to_remove)
    except KeyError as err:
        print(f"!! {item_to_remove} does NOT exist in the set: {err}")
    print_set(s)


def discarding_from_set(iterable_data, item_to_remove):
    print("--- discarding_from_set", item_to_remove)
    s = set(iterable_data)
    s.discard(item_to_remove)
    print_set(s)


def set_algebra():
    print("--- set_algebra")
    blue_eyes = {'olivia', 'harry', 'lily', 'jack', 'amelia'}
    blonde_hair = {'harry', 'jack', 'amelia', 'mia', 'joshua'}
    smell_hcn = {'harry', 'amelia'} # hydrogen cyanide
    taste_ptc = {'harry', 'lily', 'amelia', 'lola'} # phenylthiocarbamide
    o_blood = {'mia', 'joshua', 'lily', 'olivia'}
    b_blood = {'amelia', 'jack'}
    a_blood = {'harry'}
    ab_blood = {'joshua', 'lola'}

    print("blue eyes, blonde hair, or both:", blue_eyes.union(blonde_hair))
    print("blue eyes AND blonde hair:", blue_eyes.intersection(blonde_hair))
    print("blue eyes without blonde hair:", blue_eyes.difference(blonde_hair))
    print("blonde hair without blue eyes:", blonde_hair.difference(blue_eyes))
    print("blue eyes OR blonde hair BUT NOT BOTH:", blue_eyes.symmetric_difference(blonde_hair))

    print("can smell HCN with blonde hair: (smell is subset of blonde?)", smell_hcn.issubset(blonde_hair))
    print("can taste PTC can also smell HCN: (PTC  is superset of HCN?)", taste_ptc.issuperset(smell_hcn))

    print("nothing in common at all: (disjoint -- blood type is a or o, never both)", 
        a_blood.isdisjoint(o_blood))




def main():
    literal_set()
    empty_set()

    data = [ 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 7, 9]
    iterable_to_set(data)
    membership_in_set(data, 3)
    membership_not_in_set(data, 13)

    adding_to_set(data, 0)
    adding_to_set(data, 1)

    adding_several_to_set(data, [-1, 0, 1, 10])
    adding_several_to_set(data, set())

    removing_from_set(data, 1)
    removing_from_set(data, 0) # will freak out if it doesn't exist

    discarding_from_set(data, 1)
    discarding_from_set(data, 0) # doesn't care if it exists

    set_algebra()



if __name__ == '__main__':
    # refactored body to a method which could then be tested separately
    main()  # 0 is the module filename
