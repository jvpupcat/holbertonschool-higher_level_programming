# 0x0B Python - Input/Output

<img src="https://eezeeenglishzone.files.wordpress.com/2016/12/input-output-event-logo.jpg">

## Overview

* open() returns a file object, and is most commonly used with two arguments: open(filename, mode). The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. The modes:

```
* 'w' - for writing in file
* 'r' - for reading file; this will be assumed if mode is omitted
* 'r+' - opens the file for both reading and writing
* 'a' - opens the file for appending

* 'b' appended to the mode opens the file in binary mode
```

Normally, files are opened in text mode, meaning read and write strings from and to the file, which are encoded in a specific encoding. If encoding is not specified, the default is platform dependent. In text mode, the default when reading is to convert line endings (\r\n etc.) to '\n'. This type of modification to file data is fine for text files, but will corrupt binary data in JPEG or EXE files. Be carful using binary mode when reading and writing such files.

* Predefined Clean-up Actions - some objects define standard clean-up actions to be undertaken when the object is no longer needed, regardless of whether or not the operation using the object succeeded or failed.

* Files 

## What you should learn from this project

At the end of this project you are expected to be able to explain to anyone, without the help of Google:

```
* How to open a file
* How to write text in a file
* How to read the full content of a file
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after using it
* What is and how to use the with statement
* What is JSON
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string
* How to convert a JSON string to a Python data structure
```

## Requirements for Python scripts
```
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version 1.7.*)
* All your files must be executable
* The length of your files will be tested using wc
```

## Requirements for Python test cases
```
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* All your test files should be text files (extension: .txt)
* All your tests should be executed by using this command: python3 -m doctest ./tests/*
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* We strongly encourage you to work together on test cases, so that you don't miss any edge case
```
