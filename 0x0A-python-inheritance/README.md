# 0x0A Python Inheritance

<img src="https://achievement-images.teamtreehouse.com/badges_python_oop_stage2.png">

## Overview of Inheritance

Inheritance is a powerful feature in object-oriented programming. It enables us to define a class that takes all the functionality from parent class and allows us to add more. It refers to defining a new class with little or no modification to an existing class. The new class is called "derived class" or child. The class from which the child inherits from is called "base class" or parent.

Python has two built-in functions that work with inheritance:
```
- isinstance() to check an instance's type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.

- issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.
```

## What you should learn from this project

At the end of this project you are expected to be able to explain to anyone, without the help of Google:

```
* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* What is a superclass, baseclass or parentclass
* What is a subclass
* How to list all attributes and methods of a class or instance
* When can an instance have new attributes
* How to inherit class from another
* How to define a class with multiple base classes
* What is the default class every class inherit from
* How to override a method or attribute inherited from the base class
* Which attributes or methods are available by heritage to subclasses
* What is the purpose of inheritance
* What are, when and how to use isinstance, issubclass, type and super built-in functions
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
