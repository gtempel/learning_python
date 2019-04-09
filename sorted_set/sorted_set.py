# some handy standard abstract base class functionality we can mix-in and get things for
# free, such as the stuff for Sequence protocol
from collections.abc import (Sequence, Set)
from bisect import bisect_left
from itertools import chain


class SortedSet(Sequence, Set):
    def __init__(self, items=None):
        # sorted always returns a list,
        # and if set set() the items then we're certain there are no duplicates
        self._items = sorted(set(items)) if items is not None else []
    
    # container protocol allows membership testing using in and not in
    # via the special method __contains__(item)
    # There's a fallback to iterable protocol, which is reflected in the
    # test failure error messages, where it'll iterate long-hand through
    # the collection
    def __contains__(self, item):
        # obvious, but inefficient
        # return item in self._items
        #
        # refactored this detection from the count() method to here...
        # now this is *also* very similar to what's in the index() method,
        # which means we could dry this up further
        # this returns the index where you'd insert the item to maintain sort order
        # index = bisect_left(self._items, item)
        # return (index != len(self._items)) and (self._items[index] == item)
        try:
            self.index(item)
            return True
        except ValueError:
            return False
    
    # sized protocol
    def __len__(self):
        # simply delegate to the underlying list
        return len(self._items)

    # iterable protocol
    def __iter__(self):
        # or could use a for loop that yields
        # for item in self._items:
        #   yield item
        return iter(self._items)
    
    # sequence protocol: [] for slices, reversed(), index(), count(), +, * operators
    # sequence protocol: reversed has a fallback to __getitem__ and __len__
    def __getitem__(self, index):
        # if called within an index, act like a list
        # if called with a slice, return a sorted set
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    # we don't *need* a count() implementation, but we could provide a much
    # better implementation than the linear search we'll be inheriting. We
    # know that our set is sorted AND that it's a set (only ever 0 or 1 instance of something)
    # so we should be able to search much faster.
    def count(self, item):
        # now, looking at the search, which is index and found, we have a very fast
        # implementation that we can use for the __contains__ method
        # index = bisect_left(self._items, item)
        # found = (index != len(self._items)) and (self._items[index] == item)
        # convert this to a 0 or 1 (remember, we're a set, so it's not there or is there)
        return int(item in self)

    # the inherited index() method is relatively inefficient as well, given that
    # we are a sorted set, so things are in-order AND there's only ever 0 or 1
    def index(self, item):
        # this returns the index where you'd insert the item to maintain sort order
        index = bisect_left(self._items, item)

        # this is now very similar to what is/was in the __contains__ method, which
        # means that we could refactor
        if (index != len(self._items)) and (self._items[index] == item):
            return index
        raise ValueError("{} not found".format(repr(item)))
    

    # for the repr protocol to print nice strings
    # this will help with our debugging as well
    def __repr__(self):
        return "SortedSet({})".format(repr(self._items) if self._items else '')
    
    # equality operator
    def __eq__(self, rhs):
        if not isinstance(rhs, SortedSet):
            # return the error exception, not raising it...
            # this allows perhaps another object to attempt to respond
            return NotImplemented
        return self._items == rhs._items

    def __ne__(self, rhs):
        if not isinstance(rhs, SortedSet):
            # return the error exception, not raising it...
            # this allows perhaps another object to attempt to respond
            return NotImplemented
        return self._items != rhs._items

    def __add__(self, rhs):
        return SortedSet(chain(self._items, rhs._items))
    
    def __mul__(self, rhs):
        # our sorted sets are immutable, so ok to return self
        # instead of a copy
        return self if rhs > 0 else SortedSet()
    
    def __rmul__(self, lhs):
        # order of operands doesn't matter for us, so delegate by flipping/reversing
        return self * lhs

    def issubset(self, iterable):
        return self <= SortedSet(iterable)

    def issuperset(self, iterable):
        return self >= SortedSet(iterable)

    def intersection(self, iterable):
        return self & SortedSet(iterable)

    def union(self, iterable):
        return self | SortedSet(iterable)

    def symmetric_difference(self, iterable):
        return self ^ SortedSet(iterable)

    def difference(self, iterable):
        return self - SortedSet(iterable)
    