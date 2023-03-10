#!/usr/bin/python3
"""model `Base`"""
import json
import turtle


class Base:
    """class `Base`"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """from_json_string"""
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """turtle"""
        print(list_rectangles)
        print(list_squares)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open(cls.__name__+".json", "w", encoding="utf-8") as fle:
            lst = []
            if list_objs is None:
                fle.write(cls.to_json_string([]))
            else:
                for obj in list_objs:
                    lst.append(obj.to_dictionary())
                content = cls.to_json_string(lst)
                fle.write(content)

    @classmethod
    def create(cls, **dictionary):
        """create """
        if cls.__name__ == "Square":
            newCls = cls(1, 0, 0)

        if cls.__name__ == "Rectangle":
            newCls = cls(1, 1, 0, 0)

        newCls.update(**dictionary)
        return newCls

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        name = cls.__name__+".json"
        lst = []
        try:
            with open(name, encoding="utf-8") as file:
                data = file.read()
                json_data = cls.from_json_string(data)
                new = [cls.create(**obj) for obj in json_data]
                return new

        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open(cls.__name__+".csv", "w", encoding="utf-8") as fle:
            lst = []
            if list_objs is None:
                fle.write(cls.to_json_string([]))
            else:
                for obj in list_objs:
                    lst.append(obj.to_dictionary())
                content = cls.to_json_string(lst)
                fle.write(content)

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of instances"""
        name = cls.__name__+".csv"
        lst = []
        try:
            with open(name, encoding="utf-8") as file:
                data = file.read()
                json_data = cls.from_json_string(data)
                new = [cls.create(**obj) for obj in json_data]
                return new

        except FileNotFoundError:
            return []

