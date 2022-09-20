#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):#!/usr/bin/python3
2
"""Defines a Rectangle class."""
3
​
4
class Rectangle:
5
    """Rectangle representation."""
6
​
7
     def __init__(self, width=0, height=0):
8
​
9
         """instantiate a new Rec
10
​
11
         Args:
12
          width (int): The width of the new rectangle.
13
          height (int): The height of the new rectangle.
14
​
15
        """
16
        self.width = width
17
        self.height = height
18
​
19
        @property
20
        def width(self):
21
             """Get/set the width of the rectangle."""
22
             return self.__width
23
​
24
        @width.setter
25
        def width(self, value):
26
            if not isinstance(value, int):
27
                raise TypeError("width must be an integer")
28
            if value < 0:
29
                 raise ValueError("width must be >= 0")
30
             self.__width = value
31
​
32
        @property
33
        def height(self):
34
            """Get/set the height of the rectangle."""
35
            return self.__height
36
​
37
        @height.setter
38
        def height(self, value):
39
            if not isinstance(value, int):
40
                raise TypeError("height must be an integer")
41
            if value < 0:
42
                raise ValueError("height must be >= 0")
43
            self.__height = value
44

        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

