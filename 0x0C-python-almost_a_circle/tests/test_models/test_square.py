#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for square.py"""
from unittest import TestCase, mock
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import inspect
import pep8


class TestSquare(TestCase):
    """Test cases for Square class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean test files."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")

    def test_instance(self):
        """Test for correct instancing and inheritance of square object."""
        square_1 = Square(10, 12)

        self.assertIsInstance(square_1, Square)
        self.assertIsInstance(square_1, Rectangle)
        self.assertIsInstance(square_1, Base)
        self.assertTrue(issubclass(type(square_1), Base))
        self.assertTrue(issubclass(type(square_1), Rectangle))
        self.assertEqual(type(square_1), Square)
        self.assertTrue(type(square_1) == Square)
        self.assertFalse(type(square_1) == Rectangle)
        self.assertFalse(type(square_1) == Base)

    def test_attributes(self):
        """Test for correct instance attribute assignment"""
        square_1 = Square(20)

        self.assertEqual(square_1.id, 1)
        self.assertEqual(square_1.width, 20)
        self.assertEqual(square_1.height, 20)
        self.assertEqual(square_1.x, 0)
        self.assertEqual(square_1.y, 0)

        square_2 = Square(1, 2, 4, 20)

        self.assertEqual(square_2.id, 20)
        self.assertEqual(square_2.width, 1)
        self.assertEqual(square_2.height, 1)
        self.assertEqual(square_2.x, 2)
        self.assertEqual(square_2.y, 4)

        square_3 = Square(4, 1, 33)

        self.assertEqual(square_3.id, 2)
        self.assertEqual(square_3.width, 4)
        self.assertEqual(square_3.height, 4)
        self.assertEqual(square_3.x, 1)
        self.assertEqual(square_3.y, 33)

    def test_if_private(self):
        """Test direct access to private attributes"""
        square_1 = Square(10, 2, 3)
        self.assertEqual(square_1.x, 2)
        with self.assertRaises(AttributeError):
            square_1.__x

    def test_raise_argument_errors(self):
        """Test for correct argument error output"""
        with self.assertRaises(TypeError) as exc:
            Square()
        self.assertEqual(str(exc.exception),
                         "__init__() missing 1 required positional " +
                         "argument: 'size'")

    def test_raise_type_errors(self):
        """Test for correct type error output"""
        s_type_error = (30.2, "3", None, True)
        x_type_error = (
            (1, 30.2), (1, "3"), (1, None), (1, True)
        )
        y_type_error = (
            (1, 2, 30.2), (1, 2, "3"), (1, 2, None), (1, 2, True)
        )

        for case in s_type_error:
            with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Square(case)
        for case in x_type_error:
            with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Square(case[0], case[1])
        for case in y_type_error:
            with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Square(case[0], case[1], case[2])

    def test_raise_value_errors(self):
        """Test for correct value error output"""
        s_size_error = (0, -2)
        for case in s_size_error:
            with self.assertRaisesRegex(ValueError, "width must be > 0"):
                Square(case)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(4, -1, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(8, 5, -4)

    def test_area(self):
        """Test for correct area calculation"""
        square_1 = Square(10)

        self.assertEqual(square_1.area(), 100)

        with self.assertRaises(TypeError) as exc:
            square_1.area("Hello")
        self.assertEqual(
            "area() takes 1 positional argument but 2 were given",
            str(exc.exception))

    def test_print_no_offset(self):
        """Test for correct square printing without offset"""
        square_1 = Square(5)
        correct_output = "#####\n#####\n#####\n#####\n#####\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            square_1.display()
            self.assertEqual(output.getvalue(), correct_output)

        square_2 = Square(2)
        correct_output = "##\n##\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            square_2.display()
            self.assertEqual(output.getvalue(), correct_output)

    def test_print_with_offset(self):
        """Test for correct square printing with offset"""
        square_1 = Square(4, 3, 2)
        correct_output = "\n\n   ####\n   ####\n   ####\n   ####\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            square_1.display()
            self.assertEqual(output.getvalue(), correct_output)

        square_2 = Square(2, 0, 4)
        correct_output = "\n\n\n\n##\n##\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            square_2.display()
            self.assertEqual(output.getvalue(), correct_output)

        square_2.x = 2
        square_2.y = 0
        correct_output = "  ##\n  ##\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            square_2.display()
            self.assertEqual(output.getvalue(), correct_output)

    def test_str_magic_method(self):
        """Test for correct __str__ output"""
        square_1 = Square(2)
        correct_output = "[Square] (1) 0/0 - 2"
        self.assertEqual(square_1.__str__(), correct_output)

        square_2 = Square(4, 6, 3, 21)
        correct_output = "[Square] (21) 6/3 - 4"
        self.assertEqual(square_2.__str__(), correct_output)

    def test_update_args(self):
        """Test for correct update method with args"""
        square_1 = Square(2, 2, 2, 2)
        correct_output = "[Square] (2) 2/2 - 2"
        self.assertEqual(square_1.__str__(), correct_output)

        square_1.update()
        correct_output = "[Square] (2) 2/2 - 2"
        self.assertEqual(square_1.__str__(), correct_output)

        square_1.update(10)
        correct_output = "[Square] (10) 2/2 - 2"
        self.assertEqual(square_1.__str__(), correct_output)

        square_1.update(10, 4)
        correct_output = "[Square] (10) 2/2 - 4"
        self.assertEqual(square_1.__str__(), correct_output)

        square_1.update(10, 4, 6)
        correct_output = "[Square] (10) 6/2 - 4"
        self.assertEqual(square_1.__str__(), correct_output)

        square_1.update(10, 4, 6, 8)
        correct_output = "[Square] (10) 6/8 - 4"
        self.assertEqual(square_1.__str__(), correct_output)

    def test_update_kwargs(self):
        """Test for correct update method with kwargs"""
        square_2 = Square(2, 2, 2, 2)
        correct_output = "[Square] (2) 2/2 - 2"
        self.assertEqual(square_2.__str__(), correct_output)

        square_2.update(id=10)
        correct_output = "[Square] (10) 2/2 - 2"
        self.assertEqual(square_2.__str__(), correct_output)

        square_2.update(width=4, id=10)
        correct_output = "[Square] (10) 2/2 - 4"
        self.assertEqual(square_2.__str__(), correct_output)

        square_2.update(id=10, x=6, width=4)
        correct_output = "[Square] (10) 6/2 - 4"
        self.assertEqual(square_2.__str__(), correct_output)

        square_2.update(y=8, width=4, x=6)
        correct_output = "[Square] (10) 6/8 - 4"
        self.assertEqual(square_2.__str__(), correct_output)

        square_2.update(1, 2, y=100)
        correct_output = "[Square] (1) 6/8 - 2"
        self.assertEqual(square_2.__str__(), correct_output)

        square_2_pre_update = square_2.__dict__
        square_2.update(fake=30)
        self.assertEqual(square_2.__dict__, square_2_pre_update)

    def test_to_dictionary(self):
        """Test for correct to_dictionary output"""
        square_1 = Square(2)
        square_1_dict = {'id': 1, 'size': 2, 'x': 0, 'y': 0}
        self.assertEqual(square_1.to_dictionary(), square_1_dict)
        self.assertFalse(square_1.to_dictionary() is square_1_dict)
        self.assertIsInstance(square_1_dict, dict)

        square_2 = Square(30, 50, 2)
        square_2_dict = {'id': 2, 'size': 30, 'x': 50, 'y': 2}
        self.assertEqual(square_2.to_dictionary(), square_2_dict)
        self.assertFalse(square_2.to_dictionary() is square_2_dict)
        self.assertIsInstance(square_2_dict, dict)

        square_3 = Square(1, 24, 9, 20)
        square_3_dict = {'id': 20, 'size': 1, 'x': 24, 'y': 9}
        self.assertEqual(square_3.to_dictionary(), square_3_dict)
        self.assertFalse(square_3.to_dictionary() is square_3_dict)
        self.assertIsInstance(square_3_dict, dict)

        square_3.update(**square_2.to_dictionary())
        self.assertEqual(square_2.__dict__, square_3.__dict__)

    def test_from_json_string(self):
        """Test for correct list output of json string"""
        square_1 = Square(1, 24, 9, 20)
        square_1_dict = square_1.to_dictionary()
        json_str = Base.to_json_string([square_1_dict])
        json_str_list = Base.from_json_string(json_str)

        self.assertEqual(json_str_list, [square_1_dict])
        self.assertIsInstance(json_str_list, list)

    def test_to_json_string(self):
        """Test for correct json output of dictionary"""
        square_1 = Square(4, 20, 10, 12)
        square_1_dict = square_1.to_dictionary()
        json_str = Base.to_json_string([square_1_dict])

        self.assertEqual(json_str, str([square_1_dict]).replace("'", "\""))
        self.assertIsInstance(json_str, str)

    def test_create(self):
        """Test for correct instance creation from dictionary"""
        square_1 = Square(4, 1, 50, 4)
        square_1_dict = square_1.to_dictionary()
        square_2 = Square.create(**square_1_dict)

        self.assertEqual(square_1.__str__(), square_2.__str__())
        self.assertEqual(type(square_1), type(square_2))

    def test_json_to_file_None(self):
        """Test for correct output of None list of save_to_file."""
        Square.save_to_file(None)

        with os.popen('ls {}.json'.format(str(Square.__name__))) as ls:
            self.assertEqual(ls.read(), 'Square.json\n')

        with open(Square.__name__ + '.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

    def test_json_to_file_empty(self):
        """Test for correct output of empty list of save_to_file."""
        Square.save_to_file([])

        with os.popen('ls {}.json'.format(str(Square.__name__))) as ls:
            self.assertEqual(ls.read(), 'Square.json\n')

        with open(Square.__name__ + '.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

    def test_json_to_file(self):
        """Test for correct json output to file"""
        sq_1 = Square(1, 2, 5, 3)
        sq_2 = Square(1, 2, 7, 9)
        sq_list = [sq_1, sq_2]
        sq_1_dict = sq_1.to_dictionary()
        sq_2_dict = sq_2.to_dictionary()

        Square.save_to_file(sq_list)

        with os.popen('ls {}.json'.format(type(sq_1).__name__)) as ls:
            self.assertEqual(ls.read(), 'Square.json\n')
        with open(type(sq_1).__name__ + '.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(),
                             Square.to_json_string([sq_1_dict, sq_2_dict]))

    def test_from_json_file(self):
        """Test for correct instance creation from json file"""
        square_1 = Square(1, 2, 5, 3)
        square_2 = Square(1, 2, 7, 9)
        originals = [square_1, square_2]

        Square.save_to_file(originals)

        instances = Square.load_from_file()

        for original, instance in zip(instances, originals):
            self.assertIsInstance(instance, Square)
            self.assertEqual(instance.__str__(), original.__str__())

    def test_to_file_csv_None(self):
        """Test for correct output of None list of save_to_file_csv."""
        Square.save_to_file_csv(None)

        with os.popen('ls {}.csv'.format(str(Square.__name__))) as ls:
            self.assertEqual(ls.read(), 'Square.csv\n')

        with open(str(Square.__name__) + '.csv', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '')

    def test_to_file_csv_empty(self):
        """Test for correct output of empty list of save_to_file_csv."""
        Square.save_to_file_csv([])

        with os.popen('ls {}.csv'.format(str(Square.__name__))) as ls:
            self.assertEqual(ls.read(), 'Square.csv\n')

        with open(str(Square.__name__) + '.csv', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '')

    def test_to_file_csv(self):
        """Test for correct output of save_to_file_csv"""
        square_1 = Square(1, 2, 5, 3)
        square_2 = Square(1, 2, 7, 9)
        square_list = [square_1, square_2]
        square_1_dict = square_1.to_dictionary()
        square_2_dict = square_2.to_dictionary()
        square_dicts = [square_1_dict, square_2_dict]

        Square.save_to_file_csv(square_list)

        with os.popen('ls {}.csv'.format(type(square_1).__name__)) as ls:
            self.assertEqual(ls.read(), 'Square.csv\n')
        square_fields = ["id", "size", "x", "y"]

        orig_str = ",".join(square_fields) + '\n'
        for rec in square_dicts:
            row = ""
            for field in square_fields:
                row += str(rec[field]) + ','
            orig_str += row[:-1] + '\n'

        with open(type(square_1).__name__ + '.csv',
                  'r', encoding='utf-8') as f:
            csv_str = f.read()[:]

        self.assertEqual(csv_str, orig_str)

    def test_from_csv_file(self):
        """Test for correct instance creation from csv file"""
        square_1 = Square(1, 2, 5, 3)
        square_2 = Square(1, 2, 7, 9)
        originals = [square_1, square_2]

        Square.save_to_file_csv(originals)

        instances = Square.load_from_file_csv()

        for original, instance in zip(instances, originals):
            self.assertIsInstance(instance, Square)
            self.assertEqual(instance.__str__(), original.__str__())


class TestSquareDoc(TestCase):
    "Tests documentation and pep8 for Square class"

    @classmethod
    def setUpClass(cls):
        """Sets the whole functions of the class Square to be inspected for
        correct documentation."""
        cls.functions = inspect.getmembers(Square,
                                           inspect.isfunction(Square))

    def test_doc_module(self):
        """Tests for docstring presence in the module and the class."""
        from models import square

        self.assertTrue(len(square.__doc__) > 0)
        self.assertTrue(len(square.Square.__doc__) > 0)

    def test_doc_fun(self):
        """Tests for docstring presence in all functions of class."""
        for fun in self.functions:
            self.assertTrue(len(fun.__doc__) > 0)

    def test_pep8(self):
        """Tests pep8 style compliance of module and test files."""
        p8 = pep8.StyleGuide(quiet=True)

        res = p8.check_files(['models/square.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

        res = p8.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
