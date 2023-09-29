# Project Title

Python Network 0 - Shell and Scripting README

## Table of Contents

- [Project Description](#project-description)
- [Requirements](#requirements)
- [Tasks](#tasks)
    - [Task 0: cURL body size](#task-0-curl-body-size)
    - [Task 1: cURL to the end](#task-1-curl-to-the-end)
    - [Task 2: cURL Method](#task-2-curl-method)
    - [Task 3: cURL only methods](#task-3-curl-only-methods)
    - [Task 4: cURL headers](#task-4-curl-headers)
    - [Task 5: cURL POST parameters](#task-5-curl-post-parameters)
    - [Task 6: Find a peak](#task-6-find-a-peak)
    - [Task 7: Only status code](#task-7-only-status-code)
    - [Task 8: cURL a JSON file](#task-8-curl-a-json-file)
    - [Task 9: Catch me if you can!](#task-9-catch-me-if-you-can)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Description

This README provides an overview of the Python Network 0 project, including its requirements and tasks. 
The project involves creating shell and scripting solutions for various network-related tasks using tools like cURL and Python.

## Requirements

General requirements for this project include:

- All scripts will be tested on Ubuntu 20.04 LTS.
- All Bash scripts should be exactly 3 lines long (`wc -l file` should print 3).
- All files should end with a new line.
- All files must be executable.
- The first line of all Bash files should be `#!/bin/bash`.
- All curl commands must have the option `-s` (silent mode).
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5).
- The first line of all Python files should be `#!/usr/bin/python3`.
- Code should use the pycodestyle (version 2.8.*) coding style.
- All modules, classes, and functions should be documented.

## Tasks

### Task 0: cURL body size

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response. 
The size must be displayed in bytes, and you have to use curl.

Example:
```bash
./0-body_size.sh 0.0.0.0:5000
# Output: 10
```

### Task 1: cURL to the end

Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response. 
Display only the body of a 200 status code response, and you have to use curl.

Example:
```bash
./1-body.sh 0.0.0.0:5000/route_1
# Output: Route 2
```

### Task 2: cURL Method

Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response. You have to use curl.

Example:
```bash
./2-delete.sh 0.0.0.0:5000/route_3
# Output: I'm a DELETE request
```

### Task 3: cURL only methods

Write a Bash script that takes in a URL and displays all HTTP methods the server will accept. You have to use curl.

Example:
```bash
./3-methods.sh 0.0.0.0:5000/route_4
# Output: OPTIONS, HEAD, PUT
```

### Task 4: cURL headers

Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. 
A header variable X-School-User-Id must be sent with the value 98, and you have to use curl.

Example:
```bash
./4-header.sh 0.0.0.0:5000/route_5
# Output: Hello School!
```

### Task 5: cURL POST parameters

Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response. 
Two variables, email and subject, must be sent with specified values, and you have to use curl.

Example:
```bash
./5-post_params.sh 0.0.0.0:5000/route_6
# Output:
# POST params:
#     email: test@gmail.com
#     subject: I will always be here for PLD
```

### Task 6: Find a peak

Write a Python function that finds a peak in a list of unsorted integers. The function should have the lowest complexity 
and not use any external modules. The complexity should be documented in a separate file.

Example usage:
```python
print(find_peak([1, 2, 4, 6, 3]))  # Output: 6
```

### Task 7: Only status code

Write a Bash script that sends a request to a URL passed as an argument and displays only the status code of the response. 
You are not allowed to use pipes, redirection, etc., and you have to use curl.

Example:
```bash
./100-status_code.sh 0.0.0.0:5000
# Output: 200
```

### Task 8: cURL a JSON file

Write a Bash script that sends a JSON POST request to a URL passed as the first argument and displays the body of the response. 
The script should send the contents of a file passed as the second argument in the body of the request, and you have to use curl.

Example:
```bash
./101-post_json.sh 0.0.0.0:5000/route_json my_json_0
# Output: Valid JSON
```

### Task 9: Catch me if you can!

Write a Bash script that makes a request to 0.0.0.0:5000/catch_me, causing the server to respond with a message containing "You got me!" in the body of the response. You have to use curl, and you are not allowed to use echo, cat, etc., to display the final result.

Example:
```bash
./102-catch_me.sh
# Output: You got me!
```

## Usage

To use these scripts, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd <repository-directory>
```

3. Run the desired script with the appropriate arguments.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name:
   ```bash
   git checkout -b feature/my-feature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add my feature"
