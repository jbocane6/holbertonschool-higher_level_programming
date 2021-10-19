#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for base.py"""
from unittest import TestCase
from models.base import Base
import os
import inspect
import pep8


class TestBase(TestCase):
    """Test cases for Base class."""

    def setUp(self):
        """Initialization of __nb_objects to 0 before all tests."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean test files."""
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Base.csv"):
            os.remove("Base.csv")

    def test_instance(self):
        """Test for correct instancing of base object."""
        base_1 = Base(20)

        self.assertIsInstance(base_1, Base)

    def test_id(self):
        """Test for correct instance id assignment."""
        base_1 = Base()
        base_2 = Base(91)
        base_3 = Base()
        base_4 = Base(10)
        base_5 = Base(-10)

        self.assertEqual(base_1.id, 1)
        self.assertEqual(base_2.id, 91)
        self.assertEqual(base_3.id, 2)
        self.assertEqual(base_4.id, 10)
        self.assertEqual(base_5.id, -10)

    def test_to_json_empty(self):
        """Test for correct output of empty argument of to_json_string."""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_from_json_empty(self):
        """Test for correct output of empty argument of from_json_string."""
        json_str = Base.from_json_string(None)
        self.assertEqual(json_str, [])

        json_str = Base.from_json_string([])
        self.assertEqual(json_str, [])

    def test_json_to_file_None(self):
        """Test for correct output of None list of save_to_file."""
        Base.save_to_file(None)

        with os.popen('ls {}.json'.format(str(Base.__name__))) as ls:
            self.assertEqual(ls.read(), 'Base.json\n')

        with open(Base.__name__ + '.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

    def test_json_to_file_empty(self):
        """Test for correct output of empty list of save_to_file."""
        Base.save_to_file([])

        with os.popen('ls {}.json'.format(str(Base.__name__))) as ls:
            self.assertEqual(ls.read(), 'Base.json\n')

        with open(Base.__name__ + '.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

    def test_from_json_file(self):
        """Test for correct output from non existent json file."""
        Base.save_to_file(None)

        instances = Base.load_from_file()
        self.assertEqual(instances, [])

    def test_to_file_csv_None(self):
        """Test for correct output of None list of save_to_file_csv."""
        Base.save_to_file_csv(None)

        with os.popen('ls {}.csv'.format(str(Base.__name__))) as ls:
            self.assertEqual(ls.read(), 'Base.csv\n')

        with open(str(Base.__name__) + '.csv', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '')

    def test_to_file_csv_empty(self):
        """Test for correct output of empty list of save_to_file_csv."""
        Base.save_to_file_csv([])

        with os.popen('ls {}.csv'.format(str(Base.__name__))) as ls:
            self.assertEqual(ls.read(), 'Base.csv\n')

        with open(str(Base.__name__) + '.csv', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '')

    def test_from_csv_file(self):
        """Test for correct output from non existent csv file."""
        Base.save_to_file_csv(None)

        instances = Base.load_from_file()
        self.assertEqual(instances, [])


class TestBaseDoc(TestCase):
    "Tests documentation and pep8 for Base class"

    @classmethod
    def setUpClass(cls):
        """Sets the whole functions of the class Base to be inspected for
        correct documentation."""
        cls.functions = inspect.getmembers(Base, inspect.isfunction(Base))

    def test_doc_module(self):
        """Tests for docstring presence in the module and the class."""
        from models import base

        self.assertTrue(len(base.__doc__) > 0)
        self.assertTrue(len(base.Base.__doc__) > 0)

    def test_doc_fun(self):
        """Tests for docstring presence in all functions of class."""
        for fun in self.functions:
            self.assertTrue(len(fun.__doc__) > 0)

    def test_pep8(self):
        """Tests pep8 style compliance of module and test files."""
        p8 = pep8.StyleGuide(quiet=False)

        res = p8.check_files(['models/base.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

        res = p8.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
