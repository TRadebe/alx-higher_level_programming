#!/usr/bin/python3
"""Create a rectangle class."""
from base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
            x (int, optional): The x coordinate of the Rectangle. Defaults to 0.
            y (int, optional): The y coordinate of the Rectangle. Defaults to 0.
            id (int, optional): The ID of the Rectangle object. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter and setter for the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle.

        Args:
            value (int): The width value.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is not greater than 0.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter and setter for the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle.

        Args:
            value (int): The height value.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is not greater than 0.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter and setter for the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the Rectangle.

        Args:
            value (int): The x coordinate value.

        Raises:
            TypeError: If the x coordinate is not an integer.
            ValueError: If the x coordinate is not greater than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter and setter for the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the Rectangle.

        Args:
            value (int): The y coordinate value.

        Raises:
            TypeError: If the y coordinate is not an integer.
            ValueError: If the y coordinate is not greater than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """
        return self.width * self.height

    def display(self):
        """Display the Rectangle using the '#' character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle with the given arguments.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for n, val in kwargs.items():
                if n == "id":
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val
                elif n == "width":
                    self.width = val
                elif n == "height":
                    self.height = val
                elif n == "x":
                    self.x = val
                elif n == "y":
                    self.y = val

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle.

        Returns:
            dict: The dictionary representation of the Rectangle.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return a string representation of the Rectangle.

        Returns:
            str: The string representation of the Rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
