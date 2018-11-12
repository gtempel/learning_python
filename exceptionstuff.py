#! /usr/bin/env python3

import sys


def try_except(student):
    # keys that don't exist throw an exception, unless you
    # try to access them via the .get() method:
    print(f"college is {student.get('college', 'no colleges here')}")

    # generates a KeyError exception
    try:
        college = student["college"]
    except KeyError as err:
        print(f"Error finding the college: {err}")


def try_several_except_else_finally(student):
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


def exception_thrower(student):
    try:
        college = student["college"]
    except TypeError as err:
        print("Should never see this line, the exception")
    else:
        print("Shouldn't see this either, as the try blows out")



def exception_catcher(student):
    try:
        exception_thrower(student)
    except KeyError as err:
        print("exception_catcher caught the thrown inner exception")


def exception_handler_output_to_stdout_instead_of_stderr(student):
    try:
        college = student["college"]
    except KeyError as err:
        print(f"printing to stdout instead of stderr: {err}", file=sys.stdout)


def rethrowing_exception(student):
    try:
        try:
            exception_thrower(student)
        except KeyError as err:
            print("caught exception, now re-raising it")
            raise # unadorned, it re-raises the current exception
    except KeyError as err:
        print("caught the re-thrown exception")


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
    try_except(student)
    try_several_except_else_finally(student)
    exception_catcher(student)
    exception_handler_output_to_stdout_instead_of_stderr(student)
    rethrowing_exception(student)


if __name__ == '__main__':
    main()
