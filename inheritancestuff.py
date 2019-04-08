#! /usr/bin/env python3

class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def sort(self):
        self._items.sort()
    
    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return "SimpleList({!r})".format(self._items)


# this is an extension of the simple list that keeps
# the data sorted at all times
class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()


    def add(self, item):
        super().add(item)
        self.sort()
    
    def __repr__(self):
        return "SortedList({!r})".format(list(self))


class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items:
            self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports integer values.')
    
    def add(self, item):
        self._validate(item)
        super().add(item)
    
    def __repr__(self):
        return "IntList({!r})".format(list(self))


class SortedIntList(IntList, SortedList):
    def __repr__(self):
        return "SortedIntList({!r})".format(list(self))


def create_simple_list():
    my_list = SimpleList([9, 7, 5, 3, 1])
    print(f"create_simple_list() -> {my_list}")


def create_sorted_list():
    my_list = SortedList([9, 7, 5, 3, 1])
    print(f"create_sorted_list() -> {my_list}")

def create_int_list():
    my_list = IntList([9, 7, 5, 3, 1])
    print(f"create_int_list() -> {my_list}")

def create_int_list_with_non_integers():
    list_data = [9, 2, 'one', False]
    try:
        my_list = IntList(list_data)
        print(f"create_int_list_with_non_integers() created -> {my_list}")
    except TypeError as error:
        print(f"create_int_list_with_non_integers() {error}: example list: {list_data}")

def create_sorted_int_list():
    my_list = SortedIntList([10, 8, 6, 4, 2, -2])
    print(f"create_sorted_int_list() -> {my_list}")

def create_sorted_int_list_with_non_integers():
    list_data = [9, 2, 'one', False]
    try:
        my_list = SortedIntList(list_data)
        print(f"create_sorted_int_list_with_non_integers() created -> {my_list}")
    except TypeError as error:
        print(f"create_sorted_int_list_with_non_integers() {error}: example list: {list_data}")



def main():
    create_simple_list()
    create_sorted_list()
    create_int_list_with_non_integers()
    create_sorted_int_list()
    create_sorted_int_list_with_non_integers()


if __name__ == '__main__':
    main()
