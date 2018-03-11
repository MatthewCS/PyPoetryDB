# pyPoetryDB

[Check out the online database for yourself!](http://poetrydb.org/index.html)

`pip install pyPoetryDB`

pyPoetryDB is a simple module for Python 3.
This can be used for accessing and storing data from PoetryDB.
It was designed with ease-of-use in mind, making it both useful and easy to use.

Example:

```python
import pyPoetryDB

poem = pyPoetryDB.getPoem(author="Dickinson")
print("Info for \"" + poem.title + "\":\n")
print(str(poem))
```
Will output:

```
Info for "Not at Home to Callers":

author:	Emily Dickinson
title:	Not at Home to Callers
lines:
['Not at Home to Callers', 'Says the Naked Tree --', 'Bonnet due in April --', 'Wishing you Good Day --']
linecount:	4
filetype:	json

```

Check the docs and the testPyPoetry script to learn more.

* **NOTES:**
	+ Docs generated using pydoc
	+ No Python 2 support
