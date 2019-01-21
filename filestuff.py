#! /usr/bin/env python3
'''
Experiments with file operations

Groovy notion: file objects are iterables, so you can use
them in in loops and such as you would with the collections.
'''
import sys
from itertools import count, islice
import math

def write_to_new_file(filename):
    print("write_to_new_file({}):----------------".format(filename))
    # open in write mode, text mode
    f = open(filename, mode='wt', encoding='utf-8')

    # write() will return the number of characters emitted, but
    # that's not necessarily the number of bytes due to
    # encoding, newline differences, etc.
    f.write("What are the roots that clutch, ")
    f.write("what branches grow\n")
    f.write("Out of this stony rubbish? ")
    f.close()


def read_from_file(filename):
    print("read_from_file({}):----------------".format(filename))
    # open in read mode, text mode
    f = open(filename, mode='rt', encoding='utf-8')

    # read with no args will read everything; with an arg will read
    # that many characters
    n = 32
    text = f.read(n)
    print(f"--First read:\n{text}")
    text = f.read()
    print(f"--Remaining:\n{text}")
    f.close()


def seek_in_file(filename):
    print("seek_in_file({}):----------------".format(filename))
    # open in read mode, text mode
    f = open(filename, mode='rt', encoding='utf-8')

    # read with no args will read everything; with an arg will read
    # that many characters
    n = 32
    text = f.read(n)
    print(f"--First read:\n{text}")
    print(f"--seeking to beginning of file, then reading everything")
    f.seek(0)  # will return new position within file
    text = f.read()
    print(f"--Second read:\n{text}")
    f.close()


def read_lines_from_file(filename):
    print("read_lines_from_file({}):----------------".format(filename))
    # open in read mode, text mode
    f = open(filename, mode='rt', encoding='utf-8')
    text = f.readline()
    # note that the file's newline is included on the readline() calls
    print(f"--First line:\n{text}")
    text = f.readline()
    print(f"--Second line:\n{text}")
    # further calls return empty strings
    text = f.readline()
    print(f"--third call to readline:\n{text}")
    f.close()


def read_all_lines_from_file(filename):
    print("read_all_lines_from_file({}):----------------".format(filename))
    # open in read mode, text mode
    f = open(filename, mode='rt', encoding='utf-8')
    text_list = f.readlines()  # returns list of the lines
    # note that the file's newline is included on the readlines() calls
    print(f"--all lines:\n{''.join(text_list)}")
    f.close()


def append_to_file(filename):
    print("append_to_file({}):----------------".format(filename))
    # open in append mode, text mode
    f = open(filename, mode='at', encoding='utf-8')
    # there's no writeline(), but there is a writelines()
    # and you must include newlines if you want them
    f.writelines(
        [
            'Son of man,\n',
            'You cannot say, or guess, ',
            'for you know only,\n',
            'A heap of broken images, ',
            'where the sun beats\n'
        ]
    )
    f.close()


def iterate_file(filename):
    print("iterate_file({}):----------------".format(filename))
    # open in read mode, text mode
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        # print(line) # print adds its own newlines, which doubles the output
        # same method used when actually writing the file
        sys.stdout.write(line)
    f.close()


def generate_recamans_first_sequence():
    '''
    This is a generator...note the "yield" statement

    Recaman's sequence is a recursive sequence, like fibonacci, but
    there's a conditional operation subtracting OR adding.

    The first sequence (A005132) is a sequence of nonnegative integers 
    separated by steps that can be described as 
    “subtract if possible, otherwise add”: 
    a (0) = 0 ; for  n > 0, a (n) = a (n  −  1)  −  n  
    if that number is positive and not already in the sequence, 
    otherwise  a (n) = a (n  −  1) + n , whether or not that number is already in the sequence
    '''
    seen = set()
    a = 0
    for n in count(1):  # a count starting at 1, start iterating
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c


def generate_recamans_second_sequence():
    '''
    This is a generator...note the "yield" statement

    Recaman's sequence is a recursive sequence, like fibonacci, but
    there's a conditional operation subtracting OR adding.

    The second sequence by Recamán (A008336) can be described as 
    “divide if possible, otherwise multiply”:  
    a (1) = 1; a (n) = (a  (n  −  1))  / n  if  n ∣ a (n  −  1) , otherwise  a (n) = (a (n  −  1))  ⋅  n
    '''
    seen = set()
    a = 1
    for n in count(1):  # a count starting at 1, start iterating
        yield a
        seen.add(a)
        c = int(a / n)
        if a%n != 0 or c in seen:
            c = a * n
        a = c

def is_power(a, b):
    while a % b == 0:
        a = a // b
    return a == 1

def generate_recamans_third_sequence():
    '''
    This is a generator...note the "yield" statement

    A possible third sequence: “take root if possible, otherwise take power”.
    a (1) = 2; a (n) = n √  a (n  −  1)  if  a (n  −  1)  is an  n th power, otherwise  a (n) = (a (n  −  1))  n 
    '''
    seen = set()
    a = 2
    for n in count(1):  # a count starting at 1, start iterating
        yield a
        seen.add(a)
        c = a ** (1/n)
        if n == 1:
            continue
        if (not is_power(a,n)) or c in seen:
            c = a ** n
        a = c


def write_recamans_sequence(filename, num, sequence_generator):
    '''
    Write the generated sequence to a file
    '''
    print("write_recamans_sequence({}, {}):----------------".format(filename, num))

    f = open(filename, mode='wt', encoding='utf-8')
    # note that we're writing a collection of lines, but it's not
    # a big array of lines, it's instead an comprehension based
    # upon the collection returned from islice, which itself is
    # operating on not a list but an iterable created by the generator
    # method.
    f.writelines("{0}\n".format(r)
                 for r in islice(sequence_generator, num + 1))
    f.close()


def read_recamans_sequence(filename):
    print("read_recamans_sequence({}):----------------".format(filename))
    series = []
    # we need to be careful that opens are paired with closes...this is
    # one way to do it, ensuring the close always happens
    try:
        f = open(filename, mode='rt', encoding='utf-8')
        # manually, so to speak:
        # for line in f:
        #     a = int(line.strip())
        #     series.append(a)
        # or via list comprehension
        series = [int(line.strip()) for line in f]
    except ValueError as err:
        print(f"Found invalid data in {filename}: {err}")
    finally:
        f.close()  # this often actually writes the data (likely flushes)
    print(f"--series: {series}")
    return series


def read_with_context_manager(filename):
    '''
    You always have to pair-up opens and closes, otherwise resources
    are left dangling, data may not be flushed/written, etc. Using
    'with' blocks tightens things up into a specific context/scope.

    File objects returned by 'open' support context protocol.
    '''
    print("read_with_context_manager({}):----------------".format(filename))
    series = []
    # with automatically hits the 'close' method
    with open(filename, mode='rt', encoding='utf-8') as f:
        series = [int(line.strip()) for line in f]
    print(f"--series: {series}")
    return series


def write_recamans_sequence_with_context_manager(filename, num, sequence_generator):
    '''
    Write the generated sequence to a file
    '''
    print("write_recamans_sequence_with_context_manager({}, {}):----------------".format(filename, num))

    with open(filename, mode='wt', encoding='utf-8') as f:
        # note that we're writing a collection of lines, but it's not
        # a big array of lines, it's instead an comprehension based
        # upon the collection returned from islice, which itself is
        # operating on not a list but an iterable created by the generator
        # method.
        f.writelines("{0}\n".format(r)
                     for r in islice(sequence_generator, num + 1))


def _words_per_line(file_like_object):
    # might be a file,  might not be but simply acts like one
    return [len(line.split()) for line in file_like_object.readlines()]


def words_per_line_from_text(source):
    with open(source, mode='rt', encoding='utf-8') as f:
        wpl = _words_per_line(f)
        print(f"words_per_line_from_text({source}): {wpl}")


def words_per_line_from_url(source):
    from urllib.request import urlopen
    with urlopen(source) as f:
        wpl = _words_per_line(f)
        print(f"words_per_line_from_url({source}): {wpl}")


def main():
    filename = "wasteland.txt"
    write_to_new_file(filename)
    read_from_file(filename)
    seek_in_file(filename)
    read_lines_from_file(filename)
    read_all_lines_from_file(filename)
    append_to_file(filename)
    iterate_file(filename)

    recamans_filename = 'recamans_first.txt'
    recamans_count = 3
    write_recamans_sequence(filename=recamans_filename,
                            num=recamans_count,
                            sequence_generator=generate_recamans_first_sequence())
    read_recamans_sequence(filename=recamans_filename)

    write_recamans_sequence_with_context_manager(filename=recamans_filename,
                                                 num=recamans_count,
                                                 sequence_generator=generate_recamans_first_sequence())
    read_with_context_manager(filename=recamans_filename)

    write_recamans_sequence_with_context_manager(filename='recamans_second.txt',
                                                 num=recamans_count,
                                                 sequence_generator=generate_recamans_second_sequence())

    write_recamans_sequence_with_context_manager(filename='recamans_third.txt',
                                                 num=recamans_count,
                                                 sequence_generator=generate_recamans_third_sequence())

    words_per_line_from_text(filename)
    words_per_line_from_url('http://sixty-north.com/c/t.txt')


if __name__ == '__main__':
    main()
