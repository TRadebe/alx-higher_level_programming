Project: Python Input/Output

This project focuses on file input/output operations and JSON serialization/deserialization in Python. 
It includes several tasks that involve reading and writing files, working with JSON data, and implementing class methods for serialization.

Resources

Before starting the tasks, it is recommended to review the following resources:

7.2. Reading and Writing Files
8.7. Predefined Clean-up Actions
Dive Into Python 3: Chapter 11. Files (until "11.4 Binary Files" included)
JSON encoder and decoder
Learn to Program 8: Reading/Writing Files
Automate the Boring Stuff with Python (Chapter 8, pages 180-183 and Chapter 14, pages 326-333)
All about py-file I/O
Learning Objectives
By completing this project, you should be able to explain the following concepts without external help:

General:

The advantages of Python programming
How to open a file in Python
How to write text to a file
How to read the full content of a file
How to read a file line by line
How to move the cursor in a file
How to ensure a file is closed after use
The purpose and usage of the with statement
What JSON is
What serialization means
What deserialization means
How to convert a Python data structure to a JSON string
How to convert a JSON string to a Python data structure

Requirements

Python Scripts
Allowed editors: vi, vim, emacs
All your files should be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
All your files must be executable
The length of your files will be tested using wc
Your code should use the pycodestyle style (version 2.8.*)

Python Test Cases

Allowed editors: vi, vim, emacs
All your test files should end with a new line
All your test files should be inside a folder named tests
All your test files should be text files (extension: .txt)
All your tests should be executed by running the command: python3 -m doctest ./tests/*
All your modules should have a documentation string (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation string (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation string (python3 -c 'print(__import__("my_module").my_function.__doc__)' 
and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
The documentation should not be a simple word, but rather a sentence explaining the purpose of the module, class, or method (the length of the documentation will be verified)
It is strongly encouraged to work together on test cases to cover all possible edge cases
Tasks

Task 0: Read File

Write a function read_file(filename="") that reads a text file (UTF8) and prints its content to stdout. 
The function must use the with statement and should not handle file permission or file not found exceptions. 
It should have the following prototype:

def read_file(filename=""):

Example:

#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")

$ cat my_file_0.txt


A school every software engineer would have dreamt of!

$ ./0-main.py
We offer a truly innovative a
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers.

A school every software engineer would have dreamt of!

Task 1: Write to a File

Write a function write_file(filename="", text="") that writes a string to a text file (UTF8) and returns the number of 
characters written. 
The function must use the with statement and should not handle file permission exceptions. If the file already exists, 
its content should be overwritten. If the file does not exist, it should be created. The function should have the following prototype:

def write_file(filename="", text=""):

Example:


#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)


$ ./1-main.py
29
$ cat my_first_file.txt
This School is so cool!
Task 2: Append to a File
Write a function append_write(filename="", text="") that appends a string at the end of a text file (UTF8) and 
returns the number of characters added. The function must use the with statement and should not handle file permission 
or file not found exceptions. If the file does not exist, it should be created. The function should have the following prototype:

def append_write(filename="", text=""):

Example:


#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)


$ ./2-main.py
29
$ cat file_append.txt

This School is so cool!

#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)


$ ./2-main.py
29
$ cat file_append.txt
This School is so cool!
This School is so cool!
Task 3: To JSON String
Write a function to_json_string(my_obj) that returns the JSON representation of an object (string). 
The function should not handle exceptions if the object cannot be serialized. It should have the following prototype:


def to_json_string(my_obj):
Example:

#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = {
    'id': 12,
    'name': "John",
    'places': ["San Francisco", "Tokyo"],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 
