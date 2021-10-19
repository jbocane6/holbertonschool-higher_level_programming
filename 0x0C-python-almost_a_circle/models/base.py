#!/usr/bin/python3
"""This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)."""
import json
import csv


class Base():
    """Base of all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instance class Base and assign the value in id,
        Args:
            id (int): id of object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Creates a JSON string representation of a dictionary.
        Args:
            list_dictionaries: List of dictionaries.
        Return:
            dict: new dictionary.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs: List of instances who inherits of Base.
        """
        str_json = []
        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is not None:
                str_json = [obj.to_dictionary() for obj in list_objs]
                str_json = cls.to_json_string(str_json)
            f.write(str(str_json))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        Args:
            json_string: String representing a list of dictionaries.
        Return:
            List: List of the JSON string representation json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        Args:
            dictionary (**dictionary): Double pointer to a dictionary.
        Return:
            Object: Instance of Base with all attributes already set.
        """
        new = cls(1, 1) if cls.__name__ == 'Rectangle' else cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances.
        Return:
            List: List of instances of Base.
        """
        list_instances = []
        try:
            with open(cls.__name__ + ".json", "r") as f:
                new_dict = cls.from_json_string(f.read())

            for i in new_dict:
                list_instances.append(cls.create(**i))
            return list_instances
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV:.
        Args:
            list_objs (list): List of objects.
        """
        args_rectangle = ["id", "width", "height", "x", "y"]
        args_square = ["id", "size", "x", "y"]

        with open(cls.__name__ + ".csv", "w", newline='') as f:
            if list_objs is not None and len(list_objs) != 0:
                if cls.__name__ == "Rectangle":
                    new = csv.DictWriter(f, fieldnames=args_rectangle)
                else:
                    new = csv.DictWriter(f, fieldnames=args_square)
                csv_rows = [obj.to_dictionary() for obj in list_objs]
                new.writeheader()
                new.writerows(csv_rows)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV:.
        Returns:
            list: List of instances of Base.
        """
        try:
            with open(cls.__name__ + ".csv", "r", newline='') as f:
                new = csv.DictReader(f)
                dict_base = []
                for row in new:
                    row = dict([i, int(value)] for i, value in row.items())
                    dict_base.append(row)

            instance_ls = []
            for instance in dict_base:
                instance_ls.append(cls.create(**instance))
            return instance_ls
        except IOError:
            return []
