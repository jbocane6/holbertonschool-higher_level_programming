#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
import os
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for function max_integer"""

    def test_base_cases(self):
        """Tests for base cases"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([100, 85, -92, 40]), 100)
        self.assertEqual(max_integer([35, 162, -4, 50]), 162)
        self.assertEqual(max_integer([-8, -9, -10, -1, -6]), -1)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([2, 4, 6, 8, 10]), 10)
        self.assertEqual(max_integer([15, 7]), 15)

    def test_doc(self):
        """Tests for doc cases"""
        self.assertTrue(len(max_integer.__doc__) > 0)
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 0)

    def test_style(self):
        """Tests for style cases"""
        fd = os.popen('head -1 5-text_indentation.py')
        self.assertEqual(fd.read(), '#!/usr/bin/python3\n')
        fd.close()

        fd = os.popen('ls tests/6-max_integer_test.py')
        self.assertEqual(fd.read(), 'tests/6-max_integer_test.py\n')
        fd.close()

        fd = os.popen('tail -1 6-max_integer.py | cat -e')
        self.assertEqual(fd.read()[-1], '\n')
        fd.close()

    def test_types(self):
        """Tests for type cases"""
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, 1234)
