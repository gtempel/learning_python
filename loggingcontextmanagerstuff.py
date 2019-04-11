class LoggingContextManager:
    def __enter__(self):
        print('LoggingContextManager.__enter__()')
        return 'You are in a with-block!'
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('LoggingContextManager.__exit__({}, {}, {})'.format(exc_type, exc_val, exc_tb))
        # return something false to propagate the exception, otherwise return something truthy
        return False #True


import contextlib
import sys
@contextlib.contextmanager
def logging_context_manager():
    print('logging_context_manager: enter')
    try:
        yield 'You are in a with-block!'
        print('logging_context_manager: normal exit')
    except Exception:
        # the exceptions aren't propagated, as with above
        print('logging_context_manager: exceptional exit', sys.exc_info())
        # could re-raise the exception here if you want that same behavior
        # raise

# test these via:
# from loggingcontextmanagerstuff import *
# 
# then do one of the following:
#
# with LoggingContextManager() as x:
#      print(x)
#
# or
#
# with logging_context_manager() as x:
#     print(x)
#

# Also remember, context managers can be nested, as with blocks can have
# cascading/nested 'as' clauses:
#
# with cm1() as a, cm2() as b:
#    blah blah
#
# becomes the same as:
#
# with cm1() as a:
#     with cm2() as b:
#         blah blah
#
@contextlib.contextmanager
def nest_test(name):
    print(f'Entering {name}')
    yield
    print(f'Exiting {name}')

# use the above as 
#
# with nest_test('outer') as outer, nest_test('inner') as inner:
#     blah blah
#
