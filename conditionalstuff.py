#! /usr/local/bin/python3

def main():
  number = 5
  # no curly braces, just colons and indents
  if number == 5:
    print(f"number is {number}")
  else:
    print(f"number IS NOT {number}")

  if number:
    print(f"{number} has a truthy value")
  else:
    print(f"{number} is NOT truthy")

  if number != 5:
    print("f{number} does NOT equal 5")
  
  if not None:
    print("not none!")

  if None:
    print("None should not get here")
  else:
    print("None is always false")

  if number and True:
    print(f"number {number} is truthy, so and True would be truthy")
  
  if number or not None:
    print(f"number {number} OR not None should be truthy")

  # termary if's are a bit different, and useful for list comprehensions
  print("bigger" if number > 4 else "smaller")

if __name__ == '__main__':
  main()
