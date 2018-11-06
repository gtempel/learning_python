#! /usr/local/bin/python3

def add_numbers(first_arg, second_arg):
    print(first_arg + second_arg)

def add_numbers_hinted(first_arg: int, second_arg: int) -> int:
    print(first_arg + second_arg)


FIRST = 42.0
SECOND = 5
add_numbers_hinted(FIRST, SECOND)
