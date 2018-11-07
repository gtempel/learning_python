#! /usr/bin/env python3
"""Experiments with python ranges

range is an arithmetic progression of integers

range is odd because it doesn't accept keyword arguments, 
when there's 1 argument it's really the 2nd, and when there's
two it's the first two
"""

def range_stop_value():
  print("--- range with only a stop value")
  # note that the stop value isn't in the range
  r = range(5)
  print(r)
  return r


def range_start_stop_values():
  print("--- range with both start and stop value")
  # note that the stop value isn't in the range
  r = range(2, 8)
  print(r)
  return r


def range_start_stop_step_values():
  print("--- range with start, stop and interval values")
  # note that the stop value isn't in the range
  r = range(2, 20, 2)
  print(r)
  return r


def range_with_loop(r):
  for i in r:
    print(i)


def range_dont_do_range_iteration_for_lists():
  print("---range_dont_do_range_iteration_for_lists")
  # this is poor form
  s = [0, 1, 4, 6, 13]
  for i in range(len(s)):
    print(s[i])
  
  print("--- do this instead, preferring direct iteration on objects")

  print("-- or use built-in enumerate() method which yields pair tuples (index, value)")
  t = [6, 372, 8862, 148800, 2096886]
  for p in enumerate(t):
    print(p)
  # or use tuple unpacking and get the index and value
  for i, v in enumerate(t):
    print("i = {}, v = {}".format(i, v))


def main():
  range_with_loop(range_stop_value())
  range_with_loop(range_start_stop_values())
  range_with_loop(range_start_stop_step_values())
  range_dont_do_range_iteration_for_lists()


if __name__ == '__main__':
  # refactored body to a method which could then be tested separately
  main()  # 0 is the module filename
