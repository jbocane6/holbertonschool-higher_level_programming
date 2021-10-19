#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for rectangle.py"""
from unittest import TestCase, mock
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
import os
import inspect
import pep8


class TestRectangle(TestCase):
    """Test cases for Rectangle class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean test files."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")

    def test_instance(self):
        """Test for correct instancing and inheritance of rectangle object."""
        rectangle_1 = Rectangle(10, 12)

        self.assertIsInstance(rectangle_1, Rectangle)
        self.assertIsInstance(rectangle_1, Base)
        self.assertTrue(issubclass(type(rectangle_1), Base))
        self.assertTrue(issubclass(type(rectangle_1), Rectangle))
        self.assertTrue(type(rectangle_1) == Rectangle)
        self.assertFalse(type(rectangle_1) == Base)

    def test_attributes(self):
        """Test for correct instance attribute assignment"""
        rectangle_1 = Rectangle(20, 40)

        self.assertEqual(rectangle_1.id, 1)
        self.assertEqual(rectangle_1.width, 20)
        self.assertEqual(rectangle_1.height, 40)
        self.assertEqual(rectangle_1.x, 0)
        self.assertEqual(rectangle_1.y, 0)

        rectangle_2 = Rectangle(1, 20, 2, 4, 20)

        self.assertEqual(rectangle_2.id, 20)
        self.assertEqual(rectangle_2.width, 1)
        self.assertEqual(rectangle_2.height, 20)
        self.assertEqual(rectangle_2.x, 2)
        self.assertEqual(rectangle_2.y, 4)

        rectangle_3 = Rectangle(4, 1, 33, 4)

        self.assertEqual(rectangle_3.id, 2)
        self.assertEqual(rectangle_3.width, 4)
        self.assertEqual(rectangle_3.height, 1)
        self.assertEqual(rectangle_3.x, 33)
        self.assertEqual(rectangle_3.y, 4)

    def test_if_private(self):
        """Test direct access to private attributes"""
        rectangle_1 = Rectangle(10, 2, 3, 6)
        self.assertEqual(rectangle_1.x, 3)
        with self.assertRaises(AttributeError):
            rectangle_1.__x

    def test_raise_argument_errors(self):
        """Test for correct argument error output"""
        with self.assertRaises(TypeError) as exc:
            Rectangle(1)
        self.assertEqual(str(exc.exception),
                         "__init__() missing 1 required positional argument:" +
                         " 'height'")

        with self.assertRaises(TypeError) as exc:
            Rectangle()
        self.assertEqual(str(exc.exception),
                         "__init__() missing 2 required positional " +
                         "arguments: 'width' and 'height'")

    def test_raise_type_errors(self):
        """Test for correct type error output"""
        w_type_error = (
            (30.2, 1), ("3", 1), (None, 1), (True, 1)
        )
        h_type_error = (
            (1, 30.2), (1, "3"), (1, None), (1, True)
        )
        x_type_error = (
            (1, 2, 30.2), (1, 2, "3"), (1, 2, None), (1, 2, True)
        )
        y_type_error = (
            (1, 2, 3, 30.2), (1, 2, 3, "3"), (1, 2, 3, None), (1, 2, 3, True)
        )

        for case in w_type_error:
            with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle(case[0], case[1])
        for case in h_type_error:
            with self.assertRaisesRegex(TypeError,
                                        "height must be an integer"):
                Rectangle(case[0], case[1])
        for case in x_type_error:
            with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(case[0], case[1], case[2])
        for case in y_type_error:
            with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(case[0], case[1], case[2], case[3])

    def test_raise_value_errors(self):
        """Test for correct value error output"""
        w_val_error = (
            (0, 2), (-2, 2)
        )
        h_val_error = (
            (2, 0), (2, -2)
        )

        for case in w_val_error:
            with self.assertRaisesRegex(ValueError, "width must be > 0"):
                Rectangle(case[0], case[1])
        for case in h_val_error:
            with self.assertRaisesRegex(ValueError, "height must be > 0"):
                Rectangle(case[0], case[1])
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(4, 2, -1, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(8, 10, 5, -4)

    def test_area(self):
        """Test for correct area calculation"""
        rectangle_1 = Rectangle(10, 40)

        self.assertEqual(rectangle_1.area(), 400)

        with self.assertRaises(TypeError) as exc:
            rectangle_1.area("Hello")
        self.assertEqual(
            "area() takes 1 positional argument but 2 were given",
            str(exc.exception))

    def test_print_no_offset(self):
        """Test for correct rectangle printing without offset"""
        rectangle_1 = Rectangle(5, 4)
        correct_output = "#####\n#####\n#####\n#####\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            rectangle_1.display()
            self.assertEqual(output.getvalue(), correct_output)

        rectangle_2 = Rectangle(2, 6)
        correct_output = "##\n##\n##\n##\n##\n##\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            rectangle_2.display()
            self.assertEqual(output.getvalue(), correct_output)

    def test_print_with_offset(self):
        """Test for correct rectangle printing with offset"""
        rectangle_1 = Rectangle(5, 4, 3, 2)
        correct_output = "\n\n   #####\n   #####\n   #####\n   #####\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            rectangle_1.display()
            self.assertEqual(output.getvalue(), correct_output)

        rectangle_2 = Rectangle(2, 6, 0, 4)
        correct_output = "\n\n\n\n##\n##\n##\n##\n##\n##\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            rectangle_2.display()
            self.assertEqual(output.getvalue(), correct_output)

        rectangle_2.x = 2
        rectangle_2.y = 0
        correct_output = "  ##\n  ##\n  ##\n  ##\n  ##\n  ##\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            rectangle_2.display()
            self.assertEqual(output.getvalue(), correct_output)

    def test_str_magic_method(self):
        """Test for correct __str__ output"""
        rectangle_1 = Rectangle(1, 2)
        correct_output = "[Rectangle] (1) 0/0 - 1/2"
        self.assertEqual(rectangle_1.__str__(), correct_output)
        rectangle_2 = Rectangle(4, 6, 2)
        correct_output = "[Rectangle] (2) 2/0 - 4/6"
        self.assertEqual(rectangle_2.__str__(), correct_output)

        rectangle_3 = Rectangle(15, 1, 4, 1)
        correct_output = "[Rectangle] (3) 4/1 - 15/1"
        self.assertEqual(rectangle_3.__str__(), correct_output)

        rectangle_4 = Rectangle(4, 6, 2, 3, 21)
        correct_output = "[Rectangle] (21) 2/3 - 4/6"
        self.assertEqual(rectangle_4.__str__(), correct_output)

    def test_update_args(self):
        """Test for correct update method with args"""
        rectangle_1 = Rectangle(2, 2, 2, 2, 2)
        correct_output = "[Rectangle] (2) 2/2 - 2/2"
        self.assertEqual(rectangle_1.__str__(), correct_output)

        rectangle_1.update()
        correct_output = "[Rectangle] (2) 2/2 - 2/2"
        self.assertEqual(rectangle_1.__str__(), correct_output)

        rectangle_1.update(10)
        correct_output = "[Rectangle] (10) 2/2 - 2/2"
        self.assertEqual(rectangle_1.__str__(), correct_output)

        rectangle_1.update(10, 4)
        correct_output = "[Rectangle] (10) 2/2 - 4/2"
        self.assertEqual(rectangle_1.__str__(), correct_output)

        rectangle_1.update(10, 4, 6)
        correct_output = "[Rectangle] (10) 2/2 - 4/6"
        self.assertEqual(rectangle_1.__str__(), correct_output)

        rectangle_1.update(10, 4, 6, 8)
        correct_output = "[Rectangle] (10) 8/2 - 4/6"
        self.assertEqual(rectangle_1.__str__(), correct_output)

        rectangle_1.update(10, 4, 6, 8, 12)
        correct_output = "[Rectangle] (10) 8/12 - 4/6"
        self.assertEqual(rectangle_1.__str__(), correct_output)

    def test_update_kwargs(self):
        """Test for correct update method with kwargs"""
        rectangle_2 = Rectangle(2, 2, 2, 2, 2)
        correct_output = "[Rectangle] (2) 2/2 - 2/2"
        self.assertEqual(rectangle_2.__str__(), correct_output)

        rectangle_2.update(id=10)
        correct_output = "[Rectangle] (10) 2/2 - 2/2"
        self.assertEqual(rectangle_2.__str__(), correct_output)

        rectangle_2.update(width=4, id=10)
        correct_output = "[Rectangle] (10) 2/2 - 4/2"
        self.assertEqual(rectangle_2.__str__(), correct_output)

        rectangle_2.update(id=10, height=6, width=4)
        correct_output = "[Rectangle] (10) 2/2 - 4/6"
        self.assertEqual(rectangle_2.__str__(), correct_output)

        rectangle_2.update(x=8, width=4, height=6)
        correct_output = "[Rectangle] (10) 8/2 - 4/6"
        self.assertEqual(rectangle_2.__str__(), correct_output)

        rectangle_2.update(y=12, id=10, x=8, height=6, width=4)
        correct_output = "[Rectangle] (10) 8/12 - 4/6"
        self.assertEqual(rectangle_2.__str__(), correct_output)

        rectangle_2.update(12, 200, y=8, x=15)
        correct_output = "[Rectangle] (12) 8/12 - 200/6"
        self.assertEqual(rectangle_2.__str__(), correct_output)

        rectangle_2_pre_update = rectangle_2.__dict__
        rectangle_2.update(fake=30)
        self.assertEqual(rectangle_2.__dict__, rectangle_2_pre_update)

    def test_to_dictionary(self):
        """Test for correct to_dictionary output"""
        rectangle_1 = Rectangle(2, 20)
        rectangle_1_dict = {'id': 1, 'width': 2, 'height': 20, 'x': 0, 'y': 0}
        self.assertEqual(rectangle_1.to_dictionary(), rectangle_1_dict)
        self.assertFalse(rectangle_1.to_dictionary() is rectangle_1_dict)
        self.assertIsInstance(rectangle_1_dict, dict)

        rectangle_2 = Rectangle(30, 1, 50, 2)
        rectangle_2_dict = {'id': 2, 'width': 30, 'height': 1, 'x': 50, 'y': 2}
        self.assertEqual(rectangle_2.to_dictionary(), rectangle_2_dict)
        self.assertFalse(rectangle_2.to_dictionary() is rectangle_2_dict)
        self.assertIsInstance(rectangle_2_dict, dict)

        rectangle_3 = Rectangle(1, 2, 24, 9, 20)
        rectangle_3_dict = {'id': 20, 'width': 1, 'height': 2, 'x': 24, 'y': 9}
        self.assertEqual(rectangle_3.to_dictionary(), rectangle_3_dict)
        self.assertEqual(rectangle_3.to_dictionary() is rectangle_3_dict,
                         False)
        self.assertIsInstance(rectangle_3_dict, dict)

        rectangle_3.update(**rectangle_2.to_dictionary())
        self.assertEqual(rectangle_2.__dict__, rectangle_3.__dict__)

    def test_to_json_string(self):
        """Test for correct json output of dictionary"""
        rectangle_1 = Rectangle(4, 20, 10, 12, 30)
        rectangle_1_dict = rectangle_1.to_dictionary()
        json_str = Base.to_json_string([rectangle_1_dict])

        self.assertEqual(json_str, str([rectangle_1_dict]).replace("'", "\""))
        self.assertIsInstance(json_str, str)

    def test_from_json_string(self):
        """Test for correct list output of json string"""
        rectangle_1 = Rectangle(4, 20, 10, 12, 30)
        rectangle_1_dict = rectangle_1.to_dictionary()
        json_str = Base.to_json_string([rectangle_1_dict])
        json_str_list = Base.from_json_string(json_str)

        self.assertEqual(json_str_list, [rectangle_1_dict])
        self.assertIsInstance(json_str_list, list)

    def test_create(self):
        """Test for correct instance creation from dictionary"""
        rectangle_1 = Rectangle(2, 4, 5, 1, 9)
        rectangle_1_dict = rectangle_1.to_dictionary()
        rectangle_2 = Rectangle.create(**rectangle_1_dict)

        self.assertEqual(rectangle_1.__str__(), rectangle_2.__str__())
        self.assertEqual(type(rectangle_1), type(rectangle_2))

    def test_json_to_file_None(self):
        """Test for correct output of None list of save_to_file."""
        Rectangle.save_to_file(None)

        with os.popen('ls {}.json'.format(str(Rectangle.__name__))) as ls:
            self.assertEqual(ls.read(), 'Rectangle.json\n')

        with open(Rectangle.__name__ + '.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

    def test_json_to_file_empty(self):
        """Test for correct output of empty list of save_to_file."""
        Rectangle.save_to_file([])

        with os.popen('ls {}.json'.format(str(Rectangle.__name__))) as ls:
            self.assertEqual(ls.read(), 'Rectangle.json\n')

        with open(Rectangle.__name__ + '.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

    def test_json_to_file(self):
        """Test for correct json output to file"""
        rc_1 = Rectangle(1, 9, 20, 30, 4)
        rc_2 = Rectangle(2, 5, 10, 2, 9)
        rc_list = [rc_1, rc_2]
        rc_1_dict = rc_1.to_dictionary()
        rc_2_dict = rc_2.to_dictionary()

        Rectangle.save_to_file(rc_list)

        with os.popen('ls {}.json'.format(type(rc_1).__name__)) as ls:
            self.assertEqual(ls.read(), 'Rectangle.json\n')
        with open(type(rc_1).__name__ + '.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(),
                             Rectangle.to_json_string([rc_1_dict, rc_2_dict]))

    def test_from_json_file(self):
        """Test for correct instance creation from json file"""
        rec_1 = Rectangle(1, 9, 20, 30, 4)
        rec_2 = Rectangle(2, 5, 10, 2, 9)
        originals = [rec_1, rec_2]

        Rectangle.save_to_file(originals)

        instances = Rectangle.load_from_file()

        for original, instance in zip(instances, originals):
            self.assertIsInstance(instance, Rectangle)
            self.assertEqual(instance.__str__(), original.__str__())

    def test_to_file_csv_None(self):
        """Test for correct output of None list of save_to_file_csv."""
        Rectangle.save_to_file_csv(None)

        with os.popen('ls {}.csv'.format(str(Rectangle.__name__))) as ls:
            self.assertEqual(ls.read(), 'Rectangle.csv\n')

        with open(str(Rectangle.__name__) + '.csv',
                  'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '')

    def test_to_file_csv_empty(self):
        """Test for correct output of empty list of save_to_file_csv."""
        Rectangle.save_to_file_csv([])

        with os.popen('ls {}.csv'.format(str(Rectangle.__name__))) as ls:
            self.assertEqual(ls.read(), 'Rectangle.csv\n')

        with open(str(Rectangle.__name__) + '.csv',
                  'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '')

    def test_to_file_csv(self):
        """Test for correct output of save_to_file_csv"""
        rc_1 = Rectangle(1, 9, 20, 30, 4)
        rc_2 = Rectangle(2, 5, 10, 2, 9)
        rc_list = [rc_1, rc_2]
        rc_1_dict = rc_1.to_dictionary()
        rc_2_dict = rc_2.to_dictionary()
        rc_dicts = [rc_1_dict, rc_2_dict]

        Rectangle.save_to_file_csv(rc_list)

        with os.popen('ls {}.csv'.format(type(rc_1).__name__)) as ls:
            self.assertEqual(ls.read(), 'Rectangle.csv\n')
        rec_fields = ["id", "width", "height", "x", "y"]

        orig_str = ",".join(rec_fields) + '\n'
        for rec in rc_dicts:
            row = ""
            for field in rec_fields:
                row += str(rec[field]) + ','
            orig_str += row[:-1] + '\n'

        with open(type(rc_1).__name__ + '.csv', 'r', encoding='utf-8') as f:
            csv_str = f.read()[:]

        self.assertEqual(csv_str, orig_str)

    def test_from_csv_file(self):
        """Test for correct instance creation from csv file"""
        rec_1 = Rectangle(1, 9, 20, 30, 4)
        rec_2 = Rectangle(2, 5, 10, 2, 9)
        originals = [rec_1, rec_2]

        Rectangle.save_to_file_csv(originals)

        instances = Rectangle.load_from_file_csv()

        for original, instance in zip(instances, originals):
            self.assertIsInstance(instance, Rectangle)
            self.assertEqual(instance.__str__(), original.__str__())


class TestRectangleDoc(TestCase):
    "Tests documentation and pep8 for Rectangle class"

    @classmethod
    def setUpClass(cls):
        """Sets the whole functions of the class Rectangle to be inspected for
        correct documentation."""
        cls.functions = inspect.getmembers(Rectangle,
                                           inspect.isfunction(Rectangle))

    def test_doc_module(self):
        """Tests for docstring presence in the module and the class."""
        from models import rectangle

        self.assertTrue(len(rectangle.__doc__) > 0)
        self.assertTrue(len(rectangle.Rectangle.__doc__) > 0)

    def test_doc_fun(self):
        """Tests for docstring presence in all functions of class."""
        for fun in self.functions:
            self.assertTrue(len(fun.__doc__) > 0)

    def test_pep8(self):
        """Tests pep8 style compliance of module and test files."""
        p8 = pep8.StyleGuide(quiet=False)

        res = p8.check_files(['models/rectangle.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

        res = p8.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
