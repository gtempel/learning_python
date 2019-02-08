'''
Calculate the hypervolume of the hypercube by
multiplying each of the sides

AT a minimum we need one length; the others are optional
and thus in the *lengths vararg
'''
def hypervolume(length, *lengths):
    # get the first side
    v = length

    # multiply each of the sides in turn
    for item in lengths:
        v *= item
    return v

if __name__ == '__main__':
  # refactored body to a method which could then be tested separately
  hypervolume(1,2,3)
