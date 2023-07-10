Python Inheritance

This repository contains Python scripts that demonstrate the concept of inheritance in object-oriented programming. Inheritance is a fundamental concept in Python and other object-oriented programming languages that allows classes to inherit attributes and methods from other classes. It promotes code reuse and helps create hierarchical relationships between classes.

Resources

If you're new to inheritance or want to deepen your understanding, the following resources can be helpful:

Inheritance: Official Python documentation on inheritance.
Multiple inheritance: Learn about multiple inheritance in Python.
Inheritance in Python: A comprehensive guide to inheritance in Python.
Learn to Program 10: Inheritance Magic Methods: A video tutorial explaining inheritance magic methods.
Learning Objectives
By working through the scripts in this repository, you will gain the following knowledge and skills:

Understand why Python programming is awesome.
Differentiate between superclass (base class or parent class) and subclass.
Learn how to list all attributes and methods of a class or instance.
Identify when an instance can have new attributes.
Grasp the concept of inheriting a class from another.
Define a class with multiple base classes.
Recognize the default class that every class inherits from.
Override methods or attributes inherited from the base class.
Understand the attributes and methods available by inheritance to subclasses.
Comprehend the purpose and benefits of inheritance.
Know how and when to use built-in functions like isinstance, issubclass, type, and super.
Requirements

The scripts in this repository should meet the following requirements:

Python Scripts

Use one of the following editors: vi, vim, emacs.
All files should be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
Each file should end with a new line.
The first line of each file should be exactly #!/usr/bin/python3.
Include a README.md file at the root of the project folder.
Adhere to the pycodestyle (version 2.8.*) style guide.
All files must be executable.
The length of each file will be tested using wc.
Python Test Cases
Use one of the following editors: vi, vim, emacs.
Each file should end with a new line.
Place all test files inside a folder named tests.
Test files should be text files with a .txt extension.
Execute all tests using the command: python3 -m doctest ./tests/*.
Include documentation for all modules, classes, and functions.
Document classes using the format: python3 -c 'print(__import__("my_module").MyClass.__doc__)'.
Document functions using the format: python3 -c 'print(__import__("my_module").my_function.__doc__)'.
Ensure that documentation provides meaningful explanations of the purpose and functionality.
Collaborate with others on test cases to cover all possible edge cases.
Repository Structure

The repository structure for this project is as follows:

alx-higher_level_programming/
└── 0x0A-python-inheritance/
    ├── 0-lookup.py
    ├── 1-my_list.py
    ├── 2-is_same_class.py
    ├── 3-is_kind_of_class.py
    ├── 4-inherits_from.py
    ├── 5-base_geometry.py
    ├── 6-base_geometry.py
    ├── 7-base_geometry.py
    ├── 8-rectangle.py
    ├── 9-rectangle.py
    ├── 10-square.py
    ├── 11-square.py
    └── tests/
        ├── 0-lookup.txt
        ├── 1-my_list.txt
        ├── 2-is_same_class.txt
        ├── 3-is_kind_of_class.txt
        ├── 4-inherits_from.txt
        ├── 5-base_geometry.txt
        ├── 6-base_geometry.txt
        ├── 7-base_geometry.txt
        ├── 8-rectangle.txt
        ├── 9-rectangle.txt
        ├── 10-square.txt
        └── 11-square.txt

The repository contains multiple Python scripts, each focusing on a specific aspect of inheritance. 
The tests folder includes test files for each script.

How to Use

To use these scripts, follow these steps:

Clone the repository using the following command:


git clone https://github.com/your_username/alx-higher_level_programming.git
Navigate to the 0x0A-python-inheritance directory

cd alx-higher_level_programming/0x0A-python-inheritance
Execute any Python script that you want to run:


python3 script.py

Run the test cases for a specific script:

python3 -m doctest tests/test_file.txt
