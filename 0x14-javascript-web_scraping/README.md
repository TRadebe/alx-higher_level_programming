# JavaScript - Web scraping

## Overview

This project consists of a series of JavaScript scripts that perform various tasks related to web scraping and file manipulation. The scripts are designed to meet specific requirements and use the Node.js environment.

## Requirements

### General

- **Editors:** Allowed editors are vi, vim, and emacs.
- **Interpreter:** All files will be interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x).
- **File Endings:** All files should end with a new line.
- **Shebang Line:** The first line of all files should be exactly `#!/usr/bin/node`.
- **README.md:** A README.md file at the root of the project folder is mandatory.
- **Code Style:** Your code should be semistandard compliant, following the rules of Standard with semicolons. Also, adhere to the AirBnB style.
- **File Execution:** All files must be executable.
- **Variable Usage:** Do not use `var`.

### More Info

- **Node.js Installation:**
  ```bash
  $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
  $ sudo apt-get install -y nodejs
  ```
- **Semi-Standard Installation:**
  ```bash
  $ sudo npm install semistandard --global
  ```
- **Request Module Installation:**
  ```bash
  $ sudo npm install request --global
  $ export NODE_PATH=/usr/lib/node_modules
  ```

## Tasks

### 0. Readme

Write a script that reads and prints the content of a file.

```bash
$ ./0-readme.js cisfun
C is super fun!
```

### 1. Write me

Write a script that writes a string to a file.

```bash
$ ./1-writeme.js my_file.txt "Python is cool"
$ cat my_file.txt ; echo ""
Python is cool
```

### 2. Status code

Write a script that displays the status code of a GET request.

```bash
$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
```

### 3. Star wars movie title

Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

```bash
$ ./3-starwars_title.js 1
A New Hope
```

### 4. Star wars Wedge Antilles

Write a script that prints the number of movies where the character “Wedge Antilles” is present.

```bash
$ ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
3
```

### 5. Loripsum

Write a script that gets the contents of a webpage and stores it in a file.

```bash
$ ./5-request_store.js http://loripsum.net/api loripsum
$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit...
```

### 6. How many completed?

Write a script that computes the number of tasks completed by user id.

```bash
$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11, '2': 8, '3': 7, '4': 6, '5': 12, '6': 6, '7': 9, '8': 11, '9': 8, '10': 12 }
```

### 7. Who was playing in this movie?

Write a script that prints all characters of a Star Wars movie.

```bash
$ ./100-starwars_characters.js 3
Darth Vader
R2-D2
Luke Skywalker
...
```

### 8. Right order

Write a script that prints all characters of a Star Wars movie in the same order as the list “characters” in the /films/ response.

```bash
$ ./101-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
...
```

## Repository

GitHub Repository: [alx-higher_level_programming](https://github.com/username/alx-higher_level_programming)

### Directory

- [0x14-javascript-web_scraping](https://github.com/username/alx-higher_level_programming/tree/main/0x14-javascript-web_scraping)

### Files

- [0-readme.js](https://github.com/username/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/0-readme.js)
- [1-writeme.js](https://github.com/username/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/1-writeme.js)
- [2-statuscode.js](https://github.com/username/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/2-statuscode.js)
- [3-starwars_title.js](https://github.com/username/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/3-starwars_title.js)
- [4-starwars_count.js](https://github.com/username/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/4-starwars_count.js)
- [5-request_store.js](https://github.com/username/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/5-request_store.js)
- [6-completed_tasks.js](https://github.com/username/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/6-completed_tasks.js)
- [100-starwars_characters.js](https://github.com/username/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/100-starwars_characters.js)
- [101-starwars_characters.js](https://github.com/username/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/101-starwars_characters.js)
