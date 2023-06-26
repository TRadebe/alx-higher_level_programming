Python Exceptions

This repository contains Python scripts that demonstrate various examples of handling exceptions in Python. 
Each script addresses a specific task and showcases different exception handling techniques.

Task 0: Safe List Printing

Script: 0-safe_print_list.py
Prototype: def safe_print_list(my_list=[], x=0)
This script defines a function safe_print_list that prints a specified number of elements from a list. 
It uses exception handling (try and except) to handle potential errors. The function returns the actual number of elements printed.

Example usage:

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

Task 1: Safe Printing of an Integers List

Script: 1-safe_print_integer.py
Prototype: def safe_print_integer(value)
This script defines a function safe_print_integer that prints an integer using the "{:d}".format() format specifier. 
It handles exceptions using try and except and returns True if the value is an integer and has been correctly printed, otherwise it returns False.

Example usage:


value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

Task 2: Print and Count Integers

Script: 2-safe_print_list_integers.py
Prototype: def safe_print_list_integers(my_list=[], x=0)
This script defines a function safe_print_list_integers that prints the first x elements of a list, considering only the integer values.
It skips non-integer values silently. 
The function uses exception handling to achieve this behavior and returns the real number of integers printed.

Example usage:


my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

Task 3: Integers Division with Debug

Script: 3-safe_print_division.py
Prototype: def safe_print_division(a, b)
This script defines a function safe_print_division that divides two integers and prints the result.
It uses exception handling (try, except, finally) to ensure proper division and print the result preceded by "Inside result:".
The function returns the division result if successful; otherwise, it returns None.

Example usage:

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

Task 4: Divide a List

Script: 4-list_division.py
Prototype: def list_division(my_list_1, my_list_2, list_length)
This script defines a function list_division that divides two lists element by element. It returns a new list of the specified length with the division results. The function handles different types of exceptions, such as division by zero, wrong types, and out of range errors.

Example usage:

my_list_1 = [10, 8, 4]
my_list_2 = [2, 4, 4]
result = list_division(my_list_1, my_list_2, max(len(my_list_1), len(my_list_2)))
print(result)

print("--")

my_list_1 = [10, 8, 4, 4]
my_list_2 = [2, 0, "H", 2, 7]
result = list_division(my_list_1, my_list_2, max(len(my_list_1), len(my_list_2)))
print(result)

Task 5: Raise Exception

Script: 5-raise_exception.py
Prototype: def raise_exception()
This script defines a function raise_exception that raises a type exception. 
It showcases how to raise exceptions without importing any module.

Example usage:


    raise_exception()
except TypeError as te:
    print("Exception raised")

Task 6: Raise a Message

Script: 6-raise_exception_msg.py
Prototype: def raise_exception_msg(message="")
This script defines a function raise_exception_msg that raises a name exception with a provided message. 
It demonstrates raising exceptions with custom messages without importing any module.

Example usage:


    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
Note: Each script should be executed independently for testing purposes.
