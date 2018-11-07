#! /usr/bin/env python3
"""Experiments with python strings

Str is a homogeneous immutable sequence of unicode characters
"""
def string_length():
  welsh = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
  print("length of the welsh town name: ", len(welsh))


def string_concat():
  print("--- some string concatenation")
  print("New" + "found" + "land")

  # these can impact performance, as temporaries are created
  s = "New"
  s += "found"
  s += "land"
  print(s)

  print("--- some string joins")
  color_codes = ['#45ff23', '#2321fa', '#1298a3']
  print("color codes: ", color_codes)
  colors = ';'.join(color_codes)
  print("colors: ", colors)

  print("--- fast string joins")
  # fast concatenation of a group of strings:
  highwayman = ''.join(['high', 'way', 'man'])
  print(highwayman)


def string_functions():
  print("--- some string functions")
  hello = 'Hello'
  print(hello.capitalize())
  print(hello.replace("e", "a"))
  print(hello.isalpha())
  print(hello.isdigit())


def string_splitting():
  print("--- some string splitting")
  print("foo, bar, spam,eggs".split(","))


def string_positional_formatting():
  print("--- string_positional_formatting")
  hello = 'Hello'
  computer = "HAL"
  print("{0}, nice to meet you, {1}".format(hello, computer))
  print(f"Nice to meet you, {computer}")


def string_keyword_formatting():
  print("--- string_keyword_formatting")
  hello = 'Hello'
  computer = "HAL"
  print("{0}, nice to meet you, {1}".format(hello, computer))
  print(f"Nice to meet you, {computer}")
  print("My name is {dave}".format(dave="Dave Bowman"))


def string_partitioning():
  # separate a string into the prefix, separator, suffix
  print("--- string partitioning")
  parts = "unforgettable".partition("forget") # returns a tuple
  print(parts)

  departure, separator, arrival = "London:Edinburgh".partition(':')
  print("departure: ", departure)
  print("arrival:   ", arrival)

  # if you don't care about capturing the separator, use the _ variable
  # which is, by convention, used for unused or dummy values
  origin, _, destination = "Seattle-Newark".partition('-')
  print("origin: ", origin)
  print("dest:   ", destination)



def main():
  string_concat()
  string_length()
  string_functions()
  string_splitting()
  string_positional_formatting()
  string_keyword_formatting()
  string_partitioning()


if __name__ == '__main__':
  # refactored body to a method which could then be tested separately
  main()  # 0 is the module filename
