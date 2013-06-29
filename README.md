Objects Essentials
==================

This session covers all the essentials of Python objects, from the most basic concepts to some advanced features, with real world examples and some exercises. The training contents are:

 * Type, id and value
 * Mutable vs. immutable types
 * New-style vs. old-style classes
 * Objects data model and customisation
 * Inheritance: super, getattr and MRO
 * Instantiation: __new__ and __init__
 * Metaclasses

# Usage

All the course content is written down in Python scripts, designed to be executed with [pydemo](https://github.com/pablito56/pydemo "pydemo GitHub repository").

To execute yourself all the code:

* Create a **virtualenv** (optional):
```
me@my_laptop:~/workspace/objects (master)$ virtualenv ~/venvs/objects_essentials -p python2.7
Running virtualenv with interpreter /usr/bin/python2.7
New python executable in /Users/pev/venvs/objects_essentials/bin/python
Installing setuptools............done.
Installing pip...............done.
me@my_laptop:~/workspace/objects (master)$ source ~/venvs/objects_essentials/bin/activate
```

* Install readline with **easy_install**:
```
(objects_essentials)me@my_laptop:~/workspace/objects (master)$ easy_install readline
Searching for readline
Reading http://pypi.python.org/simple/readline/
Best match: readline 6.2.4.1
Downloading http://pypi.python.org/packages/2.7/r/readline/readline-6.2.4.1-py2.7-macosx-10.7-intel.egg#md5=6ede61046a61219a6d97c44a75853c23
Processing readline-6.2.4.1-py2.7-macosx-10.7-intel.egg
creating /Users/pev/venvs/objects_essentials/lib/python2.7/site-packages/readline-6.2.4.1-py2.7-macosx-10.7-intel.egg
Extracting readline-6.2.4.1-py2.7-macosx-10.7-intel.egg to /Users/pev/venvs/objects_essentials/lib/python2.7/site-packages
Adding readline 6.2.4.1 to easy-install.pth file

Installed /Users/pev/venvs/objects_essentials/lib/python2.7/site-packages/readline-6.2.4.1-py2.7-macosx-10.7-intel.egg
Processing dependencies for readline
Finished processing dependencies for readline
```

* Install the `requirements.txt` with **pip**:

```
(objects_essentials)me@my_laptop:~/workspace/objects (master)$ pip install -r wspace/objects/requirements.txt
Downloading/unpacking git+git://github.com/pablito56/pydemo.git (from -r wspace/objects/requirements.txt (line 3))
  Cloning git://github.com/pablito56/pydemo.git to /var/folders/rv/1ljrf4d94dqbj0qg_3bksqtn3c6f71/T/pip-wHiloB-build
  Running setup.py egg_info for package from git+git://github.com/pablito56/pydemo.git

Downloading/unpacking Pygments==1.6rc1 (from -r wspace/objects/requirements.txt (line 1))
  Downloading Pygments-1.6rc1.tar.gz (1.4MB): 1.4MB downloaded
  Running setup.py egg_info for package Pygments

Downloading/unpacking nose==1.3.0 (from -r wspace/objects/requirements.txt (line 2))
  Downloading nose-1.3.0.tar.gz (404kB): 404kB downloaded
  Running setup.py egg_info for package nose

    no previously-included directories found matching 'doc/.build'
Requirement already satisfied (use --upgrade to upgrade): readline==6.2.4.1 in ./venvs/objects_essentials/lib/python2.7/site-packages/readline-6.2.4.1-py2.7-macosx-10.7-intel.egg (from -r wspace/objects/requirements.txt (line 4))
Installing collected packages: Pygments, nose, pydemo
  Running setup.py install for Pygments

    Installing pygmentize script to /Users/pev/venvs/objects_essentials/bin
  Running setup.py install for nose

    no previously-included directories found matching 'doc/.build'
    Installing nosetests script to /Users/pev/venvs/objects_essentials/bin
    Installing nosetests-2.7 script to /Users/pev/venvs/objects_essentials/bin
  Running setup.py install for pydemo

    Installing pydemo script to /Users/pev/venvs/objects_essentials/bin
Successfully installed Pygments nose pydemo
Cleaning up...
```

* Execute pydemo console (use `-h` to check its arguments):

```shell
me@my_laptop:~/workspace/objects (master)$ pydemo
Loaded 4 files, 238 code blocks
Python 2.7.2 (default, Oct 11 2012, 20:14:37)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(DemoHistoryConsole)
>>>
#-*- coding: utf-8 -*-
###
# MODULE 01: Objects: type, id, value, mutable vs. immutable
###

>>>
# Let's instantiate a string and check its id, type and value
str_inst = 'abcd'
print id(str_inst)
print type(str_inst)
print str_inst

4524942560
<type 'str'>
abcd
>>> str_inst
'abcd'
>>>
```

Alternatively you can open the Python modules with you preferred Python editor and execute code blocks manually.
