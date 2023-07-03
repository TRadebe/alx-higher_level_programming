Python - More Classes and Objects

This project focuses on Object-Oriented Programming (OOP) concepts in Python. It includes the implementation 
of a Rectangle class with various functionalities such as calculating area and perimeter, string representation, handling instance deletion, 
and more.

Learning Objectives

Upon completing this project, you will be able to:

Explain the benefits of Python programming
Understand the concept of Object-Oriented Programming (OOP)
Describe the principles of "first-class everything"
Define a class and understand the difference between a class and an object/instance
Work with attributes and distinguish between public, protected, and private attributes
Use the special __init__ method for object initialization
Understand Data Abstraction, Data Encapsulation, and Information Hiding
Define properties and differentiate them from attributes
Implement getters and setters in a Pythonic way
Utilize the __str__ and __repr__ methods for string representation of objects
Differentiate between __str__ and __repr__
Explore class attributes and object attributes
Implement class methods and static methods
Dynamically create arbitrary new attributes for existing instances of a class
Understand attribute lookup in Python and use the getattr function
Requirements
Allowed editors: vi, vim, emacs
All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
Files should end with a new line
The first line of all files should be exactly #!/usr/bin/python3
A README.md file at the root of the project folder is mandatory
Code should follow the PEP 8 style guide (use pycodestyle version 2.8.*)
All files must be executable
The length of files will be tested using wc
Files
The project consists of the following files:

0-rectangle.py: Defines an empty class Rectangle.
1-rectangle.py: Defines a class Rectangle with private instance attributes width and height and their corresponding getter and setter methods.
2-rectangle.py: Extends the Rectangle class with public instance methods area and perimeter.
3-rectangle.py: Enhances the Rectangle class by adding a string representation of the rectangle using the __str__ method.
4-rectangle.py: Extends the Rectangle class to provide a string representation that can be used to recreate a new instance of the class using eval.
5-rectangle.py: Implements instance deletion and displays a farewell message when an instance of the Rectangle class is deleted.
6-rectangle.py: Extends the Rectangle class to keep track of the number of instances created.
7-rectangle.py: Extends the Rectangle class to implement comparison operators for rectangles based on their area.
8-rectangle.py: Extends the Rectangle class to implement a square subclass.
Usage

You can run each file independently to test the implementation of the corresponding class and its functionalities. For example:

Copy code
$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
Credits

This project is part of the higher-level programming curriculum at ALX - Holberton School.
