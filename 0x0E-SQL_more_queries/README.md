# SQL More Queries Project

This project focuses on improving your SQL skills through a series of tasks that involve creating databases, tables, managing users, 
and writing queries to retrieve and manipulate data.

## Learning Objectives

By the end of this project, i was able to:

- Create MySQL users and manage their privileges.
- Understand and use primary keys and foreign keys.
- Apply constraints such as NOT NULL and UNIQUE.
- Retrieve data from multiple tables using subqueries, JOIN, and UNION.
- Write complex SQL queries to meet specific requirements.

## Requirements

- Operating System: Ubuntu 20.04 LTS
- MySQL Version: 8.0.25
- Allowed Editors: vi, vim, emacs
- All SQL queries should have a descriptive comment just before them.
- File names must be self-explanatory and end with a new line.
- Use uppercase for all SQL keywords (e.g., SELECT, WHERE, JOIN).

## Tasks

### 0. My Privileges!

Write a script to list all privileges of MySQL users `user_0d_1` and `user_0d_2` on your server.

### 1. Root User

Write a script to create a MySQL user `user_0d_1` with all privileges and set the password.

### 2. Read User

Write a script to create a database `hbtn_0d_2` and a user `user_0d_2` with SELECT privilege on the database.

### 3. Always a Name

Write a script to create a table `force_name` with `id` and `name` columns where `name` cannot be null.

### 4. ID Can't be Null

Write a script to create a table `id_not_null` with `id` and `name` columns, and set a default value for `id`.

### 5. Unique ID

Write a script to create a table `unique_id` with `id` and `name` columns, where `id` must be unique.

### 6. States Table

Write a script to create a database `hbtn_0d_usa` and a table `states` with `id` and `name` columns.

### 7. Cities Table

Write a script to create a table `cities` with `id`, `state_id`, and `name` columns, where `state_id` is a foreign key.

### 8. Cities of California

Write a script to list all cities of California without using JOIN.

### 9. Cities by States

Write a script to list all cities along with their corresponding state names.

### 10. Genre ID by Show

Write a script to list all shows with at least one genre linked.

### 11. Genre ID for All Shows

Write a script to list all shows along with their linked genre IDs.

### 12. No Genre

Write a script to list all shows without a linked genre.

### 13. Number of Shows by Genre

Write a script to list genres along with the number of shows linked to each.

### 14. My Genres

Write a script to list all genres of the show "Dexter".

### 15. Only Comedy

Write a script to list all Comedy shows.

### 16. List Shows and Genres

Write a script to list all shows along with their linked genres.

## Usage

To execute the scripts, follow these steps:

1. Install MySQL 8.0 on Ubuntu 20.04 LTS:
   ```bash
   sudo apt update
   sudo apt install mysql-server
