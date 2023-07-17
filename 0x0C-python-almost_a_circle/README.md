Almost a Circle

This repository contains Python scripts that implement a class hierarchy for managing shapes, specifically rectangles and squares. 
The project focuses on various concepts in Python, including class inheritance, exception handling, file I/O, serialization, and unit testing.

Learning Objectives

By completing this project,I have learned:

How to implement unit testing in a large project.
How to serialize and deserialize a class.
How to read and write JSON files.
How to use the *args syntax in Python.
How to use the **kwargs syntax in Python.
How to handle named arguments in a function.

Requirements

Python 3.8.5
pycodestyle 2.8.*

Project Structure

The project contains the following files and directories:

models/: A directory that serves as a Python package for the project.
models/base.py: The base class Base that provides common functionality for other classes.
models/__init__.py: An empty file that makes the models/ directory a Python package.
models/rectangle.py: The class Rectangle that inherits from Base and represents a rectangle shape.
models/square.py: The class Square that inherits from Rectangle and represents a square shape.
tests/: A directory that contains unit tests for the project.
tests/test_models/: A directory that contains test modules for different classes.
tests/test_models/test_base.py: Test cases for the Base class.
tests/test_models/test_rectangle.py: Test cases for the Rectangle class.
tests/test_models/test_square.py: Test cases for the Square class.

Usage

To run the unit tests for the project, use the following command:


python3 -m unittest discover tests

This command will discover and execute all the test modules in the tests/ directory.

Class Hierarchy

The project implements the following class hierarchy:

mathematically

         Base
          |
      Rectangle
          |
        Square

The Base class serves as the base class for other classes and provides common functionality. 
The Rectangle class inherits from Base and represents a rectangle shape. The Square class inherits from Rectangle and represents a square shape.

Class Descriptions

Base Class

The Base class is defined in the models/base.py file. It provides the following functionality:

Private class attribute __nb_objects that represents the number of instances of the class created. It is initialized to 0.
Class constructor def __init__(self, id=None):
If id is not None, assigns the value of id to the public instance attribute id.
If id is None, increments __nb_objects and assigns its new value to the public instance attribute id.

Rectangle Class

The Rectangle class is defined in the models/rectangle.py file. It inherits from the Base class and represents a rectangle shape.
It provides the following functionality:

Private instance attributes: __width, __height, __x, and __y, each with its own public getter and setter methods.
Class constructor def __init__(self, width, height, x=0, y=0, id=None):
Calls the super class constructor with id and assigns id to the public instance attribute.
Assigns width, height, x, and y to the respective private instance attributes.
Method def area(self): Calculates and returns the area of the rectangle.
Method def display(self): Prints the rectangle using the character #. It takes into account the x and y coordinates.
Method def __str__(self): Returns a string representation of the rectangle in the format [Rectangle] (<id>) <x>/<y> - <width>/<height>.
Method def update(self, *args, **kwargs): Updates the attributes of the rectangle based on the arguments passed.
 
The order of the arguments is important.

Method def to_dictionary(self): Returns a dictionary representation of the rectangle with keys id, width, height, x, and y.

Square Class

The Square class is defined in the models/square.py file. It inherits from the Rectangle class and represents a square shape. 
It provides the following functionality:

Class constructor def __init__(self, size, x=0, y=0, id=None):
Calls the super class constructor with id, x, y, size, and assigns the value of size to the width and height attributes.
Method def __str__(self): Returns a string representation of the square in the format `[Square] (<
