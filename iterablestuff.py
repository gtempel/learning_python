#! /usr/bin/env python3


def iterable_and_iter(obj):
    iterator = iter(obj)
    print(f"Iterable: {obj}")
    try:
        print(f"{next(iterator)} = next(iterator)")
        print(f"{next(iterator)} = next(iterator)")
        print(f"{next(iterator)} = next(iterator)")
        print(f"{next(iterator)} = next(iterator)")
        print(f"{next(iterator)} = next(iterator)")
    except StopIteration as identifier:
        print("Nothing more to iterate, got the StopIteration exception")
    finally:
        print("Done")


def first_from_series(iterable):
  iterator = iter(iterable)
  try:
    return next(iterator)
  except StopIteration as err:
    raise ValueError("iterable is empty")



def main():
    iterable_and_iter(['Spring', 'Summer', 'Autumn', 'Winter'])
    first_from_series(['A', 'B', 'C'])
    first_from_series(['1'])
    first_from_series([])


if __name__ == '__main__':
    main()
