#! /usr/local/bin/python3

def double_function(x):
  return x * 2

# OR

double = lambda x: x * 2

x = 5
print(double_function(x))
print(double(x))
