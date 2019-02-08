
def vegetable():
    return 'blomkål'

def animal():
    return 'bjørn'

def mineral():
    return 'stål'

# need: ensure these functions only return ascii characters
#
# we _could_ modify every function and make the return statements
# something like return ascii('blah')
#
# But that means we have to change all the functions, so it doesn't
# scale and isn't maintainable.
#
# Instead, create a decorator and apply that

def escape_unicode(f):
    def wrap(*args, **kwargs):
        # invoke the function, then transform its return arg
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

@escape_unicode
def northern_city():
    return 'Tromsø'


# decorators can be objecs as well...remember, they accept callables and return
# callables.
#
# how about a class that can count how many times a (function) has been called?

class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)

@CallCount
def hello(name):
    print('Hello {}'.format(name))

# we can have instances as decoractors as well
class Trace:
    def __init__(self):
        self.enabled = True
    
    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Trace()
@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

# can also chain the decorators 

@tracer
@escape_unicode
def norwegian_island_maker(name):
    return name + 'øy'


# how about decorating methods in a class?

class IslandMaker:
    def __init__(self, suffix):
        self.suffix = suffix
    
    @tracer
    def make_island(self, name):
        return name + self.suffix
    

# decorators can lose valuable metadata, though
import functools

def noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()
    
    # UGLY UGLY UGLY
    #noop_wrapper.__name__ = f.__name__
    #noop_wrapper.__doc__ = f.__doc__

    return noop_wrapper


# this function has a __name__ attribute
# it also has a __doc__, which is the doc string
# thus, help(hello) names use of these attributes
#
# decorating the hello() method with noop will mask
# those attributes
#
# can fix that by assigning them from the target
# function to the decorator (see above) but that's QUITE ugly
#
# functools.wraps() can handle this, and does all the
# right metadata stuff.
@noop
def hello():
    "print a well known message"
    print('Hello, world!')

