#! /usr/local/bin/python

# to run, use this command line in the shell:
# FLASK_APP=app.py flask run

from flask import Flask, render_template, redirect, url_for, request
from student import Student

students = []

app = Flask(__name__)

# this is a function decorator, modifying the students_page() function
@app.route("/", methods=["GET", "POST"])
def students_page():
    if request.method == "POST":
      new_student_id = request.form.get("student-id", "")
      new_student_name = request.form.get("name", "")
      new_student_last_name = request.form.get("last-name", "")

      new_student = Student(name=new_student_name, last_name=new_student_last_name, student_id=new_student_id)
      students.append(new_student)

    return render_template("index.html", students=students)


if __name__ == "__main__":
  app.run(debug=True)
