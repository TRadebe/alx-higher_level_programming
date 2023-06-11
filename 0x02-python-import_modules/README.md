# 0x02 Python - Import Modules

This directory contains Python programs that demonstrate the usage of importing modules in Python.

## Files

* [0-add.py](./0-add.py): Program that imports the `add` function from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.

* [1-calculation.py](./1-calculation.py): Program that imports functions from the file `calculator_1.py`, performs various mathematical operations,
and prints the results.

* [2-args.py](./2-args.py): Program that prints the number of arguments passed and the list of arguments.

* [3-infinite_add.py](./3-infinite_add.py): Program that prints the result of adding all the arguments passed to it.

* [4-hidden_discovery.py](./4-hidden_discovery.py): Program that prints the names defined in the compiled module `hidden_4.pyc`.

* [5-variable_load.py](./5-variable_load.py): Program that imports the variable `a` from the file `variable_load_5.py` and prints its value.

## Usage

$ ./0-add.py
1 + 2 = 3

$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2

$ ./2-args.py
0 arguments.

$ ./2-args.py Hello
1 argument:
1: Hello

$ ./3-infinite_add.py
0

$ ./3-infinite_add.py 79 10
89

$ ./4-hidden_discovery.py
my_secret_santa
print_hidden
print_school

$ ./5-variable_load.py
98


## Author

Themba Radebe
