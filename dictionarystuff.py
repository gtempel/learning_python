#! /usr/local/bin/python3

def main():
  # keys can have dictionaries as values: nested
  student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None,
    "metadata": {
      "foo": "bar"
    }
  }

  print(f"Student: {student}")


  all_students = [
    {"name": "Emmet", "age": 13},
    {"name": "Connor", "age": 19, "college": "HFU"},
    {"name": "Stephen", "age": 17, "college": None}
  ]

  print(f"Students: {all_students}")

  print(f"Last student: {all_students[-1]['name']}")

  print(f"connor's keys: {all_students[1].keys()}")
  print(f"connor's values: {all_students[1].values()}")

  # keys that don't exist throw an exception, unless you
  # try to access them via the .get() method:
  print(f"Emmet's college is {all_students[0].get('college', 'no dog colleges')}")
  
if __name__ == '__main__':
  main()
