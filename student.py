#! /usr/local/bin/python3

students = []

class Student:
  school_name = "Springfield Elementary"

  # self refers to the instance of the class...you don't pass
  # this in, it comes in automatically
  def __init__(self, name, last_name, student_id=332):
    # self.blah references an instance attribute
    self.name = name
    self.last_name = last_name
    self.student_id = student_id
    students.append(self)

  def __str__(self):
    return "Student " + self.get_name_capitalize()

  def get_name_capitalize(self):
    return self.name.capitalize() + " " + self.last_name.capitalize()

  def get_school_name(self):
    return self.school_name


mark = Student("Mark", "lastname", 987)
print(students)
print(mark)

print(Student.school_name)

