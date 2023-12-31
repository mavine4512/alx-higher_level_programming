#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __int__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.
        Args:
            size (int): The size of the new Square.
            x (int): the x coordinate of the new Square.
            y (int): the y coordinate of the new Square.
            id (int): the identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.
        Args:
            *args (int): New attribute values.
                - 1st arg represents id attribute
                - 2nd arg represents size attribute
                - 3rd arg represents x attribute
                - 4th arg represents y attribute
            **kwargs (dict): new key/value pairs of attributes.
        """
        if arg and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of Square."""
        return {
                "id": self.id,
                "size": self.width
                "x": self.x
                "y": self.y
                }

    def __str__(self):
        '''
         Return thr print() and str() representation of Square
        '''
        return "[Square] ({}) {}/{} - {}/{}".format(self.id, self.x self.y,
                                                    self.width)
