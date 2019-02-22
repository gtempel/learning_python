class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)
    
    def __repr__(self):
        return 'Point2D(x={}, y={})'.format(self.x, self.y)

    def __format__(self, format_spec):
        return '[Formatted point: {}, {}, {}]'.format(self.x, self.y, format_spec)


import unittest
from io import StringIO  # Python3
import sys

class Tests(unittest.TestCase):
    def setUp(self):
        self.x = 3
        self.y = 5
        self.point = Point2D(x=self.x, y=self.y)


    def capture_stdout(self):
        self.old_stdout = sys.stdout
        self.captured_stdout = StringIO()
        sys.stdout = self.captured_stdout

    
    def restore_stdout(self):
        sys.stdout = self.old_stdout


    def get_captured_stdout(self):
        return self.captured_stdout.getvalue().strip()


    """Tests for the ``Point2D`` class."""
    def test_print_calls_str(self):
        "Check that print calls str"
        expected = self.point.__str__()
        self.capture_stdout()
        print(self.point)
        actual = self.get_captured_stdout()
        self.restore_stdout()
        self.assertEqual(actual, expected)
  

    def test_repr_gives_details(self):
        "Check that repr provides details"
        expected = self.point.__class__.__name__
        actual = repr(self.point)
        self.assertTrue(actual.startswith(expected))


    def test_built_in_types_call_repr(self):
        expected = self.point.__class__.__name__
        collection = [ self.point ]
        self.capture_stdout()
        print(collection)
        actual = self.get_captured_stdout()
        self.restore_stdout()
        self.assertTrue(actual.find(expected) != -1)


    def test_format_calls_format(self):
        expected = self.point.__format__('')
        actual = '{}'.format(self.point)
        self.assertEqual(actual, expected)


    def test_format_calls_format_with_format_string_options(self):
        expected = self.point.__format__('r')
        actual = '{:r}'.format(self.point)
        self.assertEqual(actual, expected)


    def test_format_calls_repr_with_notr_format(self):
        expected = self.point.__repr__()
        actual = '{!r}'.format(self.point)
        self.assertEqual(actual, expected)
        
    def test_format_calls_repr_with_nots_format(self):
        expected = self.point.__str__()
        actual = '{!s}'.format(self.point)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
