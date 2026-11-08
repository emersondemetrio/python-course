# Module 09: Databases

In module 06 you saved data in JSON files. That works for small amounts of data, but it has limits: to change one item you have to load the whole file, change it, and write the whole file back. To find "all books from before 1970, newest first" you have to write a loop yourself.

A **database** is a program made for storing and finding data. In this module you learn the language databases speak, **SQL**, and how to use it from Python with **SQLite**, a small database that comes built into Python. No installation, no server: the whole database is one file.

This is the module where the final project moves its ceramic pieces from a JSON file into a real database.

## What you will learn

- What tables, rows and columns are
- The five SQL commands you will use almost every day: `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`
- How to filter (`WHERE`) and sort (`ORDER BY`) results
- What a primary key is, and what `NULL` means
- How to run SQL from Python with the `sqlite3` module
- How to pass values safely with `?` placeholders, and why f-strings in SQL are dangerous
- How to organize database code in small functions
- How to move data from a JSON file into a table

## Files, in order

1. [sql-basics.md](sql-basics.md): tables and the SQL language
2. [sqlite.md](sqlite.md): using SQLite from Python

## You are ready for the next module when you can...

- [ ] Explain table, row and column using a spreadsheet as an example
- [ ] Write a `CREATE TABLE` with an `id` primary key and three columns
- [ ] Write a `SELECT` with `WHERE` and `ORDER BY` without looking
- [ ] Explain why `WHERE rating = NULL` finds nothing and what to write instead
- [ ] Insert a row from Python using `?` placeholders, and explain why not to use an f-string
- [ ] Remember to call `commit()` after changing data

**Start here:** [sql-basics.md](sql-basics.md)
