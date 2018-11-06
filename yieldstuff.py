#! /usr/local/bin/python3

students = []


def read_students(f):
  for line in f:
    yield line


def read_file():
  try:
    f = open("students.txt", "r")
    for student in read_students(f):
      students.append(student)
    f.close()
  except Exception as err:
    print("Could not read file")

read_file()
print(students)