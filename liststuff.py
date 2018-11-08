#! /usr/bin/env python3

def main():
  student_names = ["Mark", "Katarina", "Jessica", "Bort", "Frank Grimes"]

  print(f"first student is {student_names[0]}")
  print(f"last student is {student_names[-1]}")
  print(f"number of students is {len(student_names)}")
  print(f"Mark is a student: {'Mark' in student_names}")
  print(f"Emmet is NOT a student: {'Emmet' not in student_names}")
  
  # loops
  for name in student_names:
    print(f"Student name is {name}")

  x = 0
  for index in range(10):
    x += 10
    print(f"x is {x}")

  x = 0
  for index in range(5, 10, 2):
    x += 10
    print(f"x is {x}, index is {index}")
  
  # find mark
  for name in student_names:
    if name is "Mark":
      print(f"Found {name}!")
      break
    print(f"currently testing {name}")

  # totally skip over Bort
  for name in student_names:
    if name is "Bort":
      continue
    print(f"currently testing {name}")

  x = 0
  while x < 10:
    print(f"Count is {x}")
    x += 1

  # can index from the end as well using negative numbers
  # REMEMBER: negative indices are 1-based, not zero-based
  s = "show how to index into sequences".split()
  print(s[-2])
  
  # can use slices by referencing start/stop (stop not included)
  print(s[1:3])

  # first and last elements
  print(s[1:-1])

  # from 3rd to end
  print(s[3:])

  # from start to third
  print(s[:3])

  # full list
  print(s[:])
  # this is also a new list object, with identical contents

  full_slice = s[:] # same as s.copy() or list(s) and are SHALLOW COPIES
  print("full_slice is s", full_slice is s) # different objects
  print("full_slice == s", full_slice == s) # same contents


if __name__ == '__main__':
  main()
