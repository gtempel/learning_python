#! /usr/local/bin/python3

students = []

def get_students_titlecase():
  students_titlecase = []
  for student in students:
    students_titlecase.append(student['name'].title())
  return students_titlecase


def print_students_titlecase():
  students_titlecase = get_students_titlecase()
  print(students_titlecase)



def add_student(name, student_id=332):
  student = {"name": name, "student_id": student_id}
  students.append(student)


# def var_args(name, *args):
#   print(name)
#   print(args)
#   print(args[1])


# def var_kwargs(name, **kwargs):
#   print(name)
#   print(kwargs)


# var_args('mark', 'loves python', None, 'hello', 123, True)
# var_kwargs('mark', desc='loves python', feedback=None, greeting='hello', id=123, subscriber=True)


def save_file(student):
  try:
    f = open("students.txt", "a")
    f.write(student + "\n")
    f.close()
  except Exception as err:
    print("Couldn't save file")


def read_file():
  try:
    f = open("students.txt", "r")
    for student in f.readlines():
      add_student(student)
    f.close()
  except Exception as err:
    print("Could not read file")


read_file()
print_students_titlecase()

student_name = input("Enter student name:")
student_id = input("Enter student ID:")
add_student(student_name, student_id)
save_file(student_name)

print_students_titlecase()
