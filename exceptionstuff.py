#! /usr/local/bin/python3

def main():
  student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None,
    "metadata": {
      "foo": "bar"
    }
  }

  print(f"Student: {student}")

  # keys that don't exist throw an exception, unless you
  # try to access them via the .get() method:
  print(f"Emmet's college is {student.get('college', 'no colleges here')}")
  
  # generates a KeyError exception
  try:
    college = student["college"]
  except KeyError as err:
    print(f"Error finding the college: {err}")

  # generates a KeyError exception
  print("Now trying out a bunch of exception stuff..........")
  student["last_name"] = "Kowalski"
  try:
    last_name = student["last_name"]
    # numbered_last_name = 3 + last_name
  except KeyError as err:
    print(f"Error finding the college: {err}")
  except TypeError as err:
    print(f"can't add numbers and last_name")
  # except Exception as err:
  #   # this is bad form and will be flagged as a warning
  #   print("Some generic error we don't know about")
  else:
    print("In the else block...always invoked at the end of the try, like a finally")
  finally:
    print("finally")


if __name__ == '__main__':
  main()
