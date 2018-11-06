#! /usr/local/bin/python3

hello = 'Hello'
print(hello.capitalize())
print(hello.replace("e", "a"))
print(hello.isalpha())
print(hello.isdigit())

print("foo, bar, spam,eggs".split(","))

computer = "HAL"
print("{0}, nice to meet you, {1}".format(hello, computer))

print(f"Nice to meet you, {computer}")
