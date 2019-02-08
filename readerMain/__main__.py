# this allows python to 'execute' the directory via:
# python3 reader
print('executing __main__.py with name {}'.format(__name__))

# this also shows that the __main__.py can access the package


import sys
import reader

# pass a file name
r = reader.Reader(sys.argv[1])
try:
    print(r.read())
finally:
    r.close()
