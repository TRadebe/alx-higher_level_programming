# Python Networking Project

This repository contains solutions to tasks related to fetching internet resources, decoding urllib body responses, making HTTP requests, 
and manipulating data from external services using Python.

## Learning Objectives

Upon completion of this project, you should be able to:

- Fetch internet resources with the Python package urllib
- Decode urllib body responses
- Use the Python package requests for making HTTP requests
- Make HTTP GET, POST, PUT, etc. requests
- Fetch JSON resources
- Manipulate data from an external service

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file at the root of the repo, containing a description of the repository
- A README.md file, at the root of the folder of this project, is mandatory
- Code should use the pycodestyle (version 2.8.*)
- All files must be executable
- Length of files will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Use `get` to access dictionary values by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- Documentation should be a real sentence explaining the purpose of the module, class, or method (length will be verified)
- Code should not be executed when imported (by using `if __name__ == "__main__":`)

### Tasks

#### 0. What's my status? #0

Write a Python script that fetches https://alx-intranet.hbtn.io/status using the `urllib` package. The body of the response must be displayed.

Example:

```bash
$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
```

#### 1. Response header value #0

Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the X-Request-Id variable found in the header 
of the response.

Example:

```bash
$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
```

#### 2. POST an email #0

Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, 
and displays the body of the response (decoded in utf-8).

Example:

```bash
$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
```

#### 3. Error code #0

Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response. Manage `urllib.error.HTTPError` 
exceptions and print the HTTP status code if it's greater than or equal to 400.

Example:

```bash
$ ./3-error_code.py http://0.0.0.0:5000
Index
$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
```

#### 4. What's my status? #1

Write a Python script that fetches https://alx-intranet.hbtn.io/status using the `requests` package. The body of the response must be displayed.

Example:

```bash
$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
```

#### 5. Response header value #1

Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the variable X-Request-Id in the response header.

Example:

```bash
$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
```

#### 6. POST an email #1

Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, 
and finally displays the body of the response.

Example:

```bash
$ ./6-post_email.py http://0.0.0.0
