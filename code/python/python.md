# Python

`2021 Jan 05, Jaroslav Langer`

## Contents

- [Tutorials](#tutorials)
- [How to start](#how-to-start)
  - [Installation](#installation)
  - [Run python](#run-python)
- [Basics](#basics)
  - [First things first](#first-things-first)
  - [Comments](#comments)
  - [Printing](#printing)
  - [Variables](#variables)
  - [String](#string)
  - [Accessing Different data](#accessing-different-data)
  - [Bytes](#bytes)
  - [Conditions](#conditions)
  - [Loops](#loops)
  - [Collections](#collections)
  - [Functions](#functions)
  - [Classes and Objects](#classes-and-objects)
  - [Methods for loops](#methods-for-loops)
  - [Math](#math)
  - [Random](#random)
  - [Imports](#imports)
  - [Inputs, outputs](#inputs-outputs)
  - [Files](#files)
  - [os](#os)
  - [Asserting](#asserting)
  - [Json](#json)
  - [Exceptions](#exceptions)
- [Advanced](#advanced)
  - [pdb — The Python Debugger](#pdb--the-python-debugger)
  - [Regex](#regex)
  - [Lambda](#lambda)
  - [Datetime](#datetime)
  - [pickle](#pickle)
  - [argparse](#argparse)
  - [Compress, decompress, checksum](#compress-decompress-checksum)
  - [underscored names in python](#underscored-names-in-python)
  - [Garbage Collector](#garbage-collector)
  - [ctypes](#ctypes)
  - [Python 2 differences](#python-2-differences)

## Tutorials

- [Tutorial place](https://realpython.com/)
- Consider [the Little Book of Python Anti-Patterns](https://docs.quantifiedcode.com/python-anti-patterns/)
- [Tutorials in Czech language (by Jiří Znamenáček)](http://vyuka.ookami.cz/index.python.html)

## How to start

### Installation

#### Venv

```sh
# Activate environment
source .env_name/source/activate
# deactivate
deactivate
```

#### pip

```sh
# Install package
pip3 install package_name
# Show package info
pip3 show package_name
# Update package
pip3 install --upgrade package_name
```

### Run python

#### Terminal

#### Scripts

Python is and excellent language for writing scripts.
- Every linux script should start with shebang.
  - Otherwise, there will be misunderstanding between python 2 and python 3.

```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

Following construct is highly recommend for scripts.

```py
if __name__ == "__main__":
    #This code will be executed only, if the file was called as a script, not imported
```

## Basics

### First things first

Everything in a python is an **object**. String is an object, list is an object. 
So almost anything has some methods already prepare for you. 
With `dir` function you can see all the attributes and methods of the object.

```py 
dir(anything)
```

### Comments

```py
# One-line comment

"""
multiline comment
"""

'''
multiline comment
'''
```

#### Docstrings

Every file, class, function can have doc string (__doc__).
Write docstrings, they are beautiful.

```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: my beautiful code name
Author: my beautiful name, email
Description:
blaaaaaaaaaa
"""

def fu():
    """function docstring"""

class cla:
    """class docstring"""
```

### Printing

Do not use variable printing for code debugging, use debugger instead!
(However to use printing for local simple testing is absolutely great thing.)

```py
variable = "var"
var2 = "2"
var3 = 3

print(variable)
print("---")

# No newline at the end
print(variable, end="")
print("---")

# More variables
print(variable, var2, var3)
print("---")

# Different separator
print(variable, var2, var3, sep=", ")
print("---")

# Personal recommendation for var printing (bit advanced, but good practice)
four = 2*2
my_array = [7,"6","five",four,[0,1,2]]
print('"len(my_array[2])": {}'.format(len(my_array[2])))
```

Output

```out
var
---
var---
var 2 3
---
var, 2, 3
---
"len(my_array[2])": 4
```

### Variables

```py
# Integers
integer = 10
million = 1_000_000 # It is possible to visually separate big numbers with underscores.
# Floats
decimal = 10.0
NaN = float("NaN")  # Special float for not-a-number.
# Strings
string = "my beautiful string"
# Booleans
boolean = True
false = False
# Empty value
no_value = None

# Unassign variables (not often used)
del integer, million, decimal, Nan, string, boolean, false, no_value
```

### String

There is four types how to quote a string
```py
# Two equivalents how write single-line string
'string'
"another string"
# Two equivalents how write multi-line string
'''
multiline string
'''
"""
another multiline string
"""
```

#### Raw string

```py
r'In this string, the \n character will stay as \n. It will not be expanded as newline'
```

#### Format and f string

```py
# Using string.format()
pathToNewFile = '{folder}{file}.{fileType}'.format(
    folder=download_folder, file=xlsName, fileType='xls')

# Curly braces to remain
string = "{{double curly braces will be formatted as one".format()
# escaping does not work
string = "\{ this will raise an ValueError".format()

# f string
pathToNewFile = f'{download_folder}{xlsName}.{"xls"}'

# Format float precision
a = 1/3
print("{:.2f}".format(a)) # 0.33

# Fill with whitespace
a, b, c = 55555, 1, 7777777
print(f"# a: {a: <8} b: {b: <8} c: {c}")
# a: 55555    b: 1        c: 7777777
```

- [Python string format cookbook](https://mkaz.blog/code/python-string-format-cookbook/)

#### String functions

```py
# Check whether string contains substring
"sub" in "substring" # True
# lower - Make string lowercase
"sTrInG StRiNg".lower() # "string"
# upper - Make string uppercase
"sTrInG StRiNg".upper() # "STRING STRING"
# capitalize - First letter uppercase, rest lowercase
"sTrInG StRiNg".capitalize() # "String string"

# slit
"string string2".split()
# join
' '.join(['string', 'string2', 'string3'])
# strip
"          string                ".strip()

# startswith
"string about nothing".startswith('str')    # True
# endswith
"string about nothing".endswith('ing.')   # False
# find
"string about nothing".find('abo')
# rfind
".hidden_file_.txt".rfind('.')

# count
question = "Hi mom, how much coins i need to buy coin keeper for my coin sessions?"
question.count("coin") # 3

# isnumeric - check if every character is unicode numeric
"1234".isnumeric() # True
"1234.2".isnumeric() # False
```

- [is numeric (tutorials point)](https://www.tutorialspoint.com/python/string_isnumeric.htm)

### Accessing Different data

#### type and isinstance

Recognize type of a passed object
```py
var = {1: "2"}

# Check if types are equal
type(var) == type({}) # True

# However based on the PEP recommendation, types should never be compared like that, instead use
isinstance(a, dict) # True
```

#### Equality, Identity and ID

```py
a = [1,2]
b = [1,2]

a == b  # True
a is b  # False
id(a)   # 140242993380096

True == 1   # True
True is 1   # False
id(True)    # 10299104
```

#### len()

priceless method, can be used for number of characters of a string as well as number of elements of an array

#### Slices

Basically anything that can be iterated retrieves a slice when applying operator `[ : ]`

```py
string[first_letter : letter_not_to_be_seen]
array[ : n_th_item]     # Items from index 0 up to n_th_item (not including n_th_item).
array[first_item : ]    # Items from first_item (including it) to the end.
array[first_item : -1]  # All items except the last one.
array[first_item : -5]  # All items from the first_item up to the -5th (not including it).
```

Examples
```py
# Slice DOCTYPE out of html #
text = text[len('<!DOCTYPE html>\n'):]
```

### Bytes

```py
bytes_1 = b"Bytes form this string"
bytes_2 = "Bytes form this string".encode()

string_from_bytes = bytes_1.decode()
```

- [link](https://www.tutorialspoint.com/python/string_decode.htm)

### Conditions

ternary assigning
```
variable = value if (condition) else otherValue
```

### Loops

```py
for x in almostAnything:
    print(x)
```

### Collections

#### Lists

```py
list_1 = ["a", "b"]
list_2 = ["c", "d"]

# Convert string to list of characters
list("All the beautiful strings")

# Append anything (e.g. list_2) to given list (list_1)
list_1.append(list_2)

# Pop (remove, delete) an item from list_1
popped = list_1.pop()        # pop last item
popped = list_1.pop(index)   # pop item at index e.g. index=0

# Extend list_2 with multiple items (from list_1) at once
list_2.extend(list_1)

# Insert item to given index
list_1.insert(1, "this string will fit between index 0 and index 1")

# Sort list (inplace)
l.sort()
# Ascending/descending, preprocess keys by a function (-> sort names from longest)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

def cmp_len(x):
    return len(x)

cars.sort(reverse=True, key=cmp_len)

# Or with lambda (bit advanced)
cars.sort(reverse=True, key=lambda x: len(x))
```

- [list methods (programiz)](https://www.programiz.com/python-programming/methods/list)
- [sort example](https://www.w3schools.com/python/ref_list_sort.asp)

#### Dictionary

```py
my_dict = {"Key": "value", "k": 1, "list": [1,2,3]}
dict_tmp = dict([("another", "key"), ("and_many", "more")])
# Add key-value pair
my_dict["new_key"] = "anything"
# Add all key-values from another dictionary
my_dict.update(dict_tmp)
```

```py
# For loop with dictionaries
for key in myDict:
    print(myDict[key])

for key, value in myDict.items():
    print(key)
    print(value)
```

#### Set

```py
my_set = set()
my_set.add('a') # {'a'}
my_set.add('a') # {'a'}
```

- [set (programiz)](https://www.programiz.com/python-programming/set)

#### Assignment vs. copy vs. deepcopy

Actions in one collection may affect others if were not created wisely.

```py
# Assignment - shallow copy e.i. copy by reference
a = {'first': 1, 'second': [2]}
b = a
b['first'] = 9
a['first']          # 9
b['second'][0] = 9
a['second']         # [9]

# Collections copy - one level deep copy by value
a = {'first': 1, 'second': [2]}
b = a.copy()
b['first'] = 9
a['first']          # 1
b['second'][0] = 9
a['second']         # [9]

# copy.deepcopy() - every nested collestion is copied by value
import copy

a = {'first': 1, 'second': [2]}
b = copy.deepcopy(a)
b['first'] = 9
a['first']          # 1
b['second'][0] = 9
a['second']         # [2]
```

#### Comprehensions

```py
crazy_big = 34526
crazy_fifth = round(crazy_num/5)

# list comprehension
my_list = [x for x in range(crazy_fifth, crazy_big, crazy_fifth)]

# dict comprehension
my_dict = {str(item): item%2354 for item in my_list}

# set comprehension
my_set = {val for val in my_dict.values()}
```

[set comprehension](https://python-reference.readthedocs.io/en/latest/docs/comprehensions/set_comprehension.html)

### Functions

```py
def fu(arg1, arg2=".", *args, **kwargs):
    print(arg1, arg2, *args, **kwargs)

fu("Hello", "world", "!", sep=" ", end="\n")
```

- [Python does not have function overloading](https://www.codementor.io/@arpitbhayani/overload-functions-in-python-13e32ahzqt)
- [*args and **kwargs](https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3)

### Classes and Objects

Because everything in python is an object, it is essential to know, how to create your own objects.

- [OOP (tutorialspoint)](https://www.tutorialspoint.com/python/python_classes_objects.htm)

```py
class Data():
    """Simple Data class for illustration how classes are created in python"""


    def __init__(self, attribute):
        self.attribute = attribute


    def __repr__(self):
        return f"<Data: attribute={attribute}>"


    def __call__(self, param):
        print(f'This is visible once the instance was called ({param})')


    def set_name_from_dict(self, dictionary):
        """Set attribute to the current object that is read from given dictionary."""
        self.attribute = dictionary.get("attribute")


    @classmethod
    def from_dict(cls, dictionary):
        """Creates Data object with attribute read from dictionary."""
        return cls(dictionary.get("attribute"))

```

- [multiple constructors (stackoverflow)](https://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python)
- [repr (programiz)](https://www.programiz.com/python-programming/methods/built-in/repr)

### Methods for loops

```py
# zip
ids = ["34925705", "09548622", "24641309"]
names = ["John","Peter", "Anthony"]
nicknames = ["Joeeyyy", "Pete", "Toeney"]

transformed = [[id, na, ni] for id, na, ni in zip(ids, names, nicknames)]
[['34925705', 'John', 'Joeeyyy'], ['09548622', 'Peter', 'Pete'], ['24641309', 'Anthony', 'Toeney']]

# enumerate
galleries_without_number = ["Great Gallery", "Magnificent Gallery", "The Gallery"]
id_gallery_dict = {-n: v for n,v in enumerate(galleries_without_number, start=1)}
```

### Math

```py
# Round(float, precision)
round(1.242345, 3)

# Multiple comparisons one line
20 > 13 > 10 # True
(20 > 13) > 10 # False

# Maximum
max(1, 34, 15, 32, 54, 23)      # 34
# Minimum
min([1, 34, 15, 32, 54, 23])    # 1

from math import ceil, floor
ceil(2.1) == floor(3.9) # True
```

- [Round function (w3school)](https://www.w3schools.com/python/ref_func_round.asp)
- [Multiple comparison python 2.3 doc, still valid)](https://docs.python.org/2.3/ref/comparisons.html)

#### Statistics

```py
from statistics import mean, median, mode
values = [1, 34, 4, 32, 54, 23, 34]

mean(values)    # 26
median(values)  # 32
mode(values)    # 34
```

### Random

```py
from random import uniform, randrange, choice, sample

# Random float from range (0,10)
f = uniform(0, 10)

# Random integer from range
i = randrange(0, 101, 1)

# Random item of list
item = choice(["Alice", "Bob", "Chuck"])

# List sample of k elements
samples = sample(["Alice", "Bob", "Chuck"], 2)
```

- [Random library (python documentation)](https://docs.python.org/3/library/random.html)

### Imports
```py
from xy import xyz as x
```

### Inputs, outputs

#### Input arguments

```py
import sys
```
first argument is name of a script with the path you run it
```
print ("the script has the name: {}".format(sys.argv[0]))
```
number of arguments
```
print ("Number of arguments: {}".format(len(sys.argv[0])))
```

#### Standard input

```py
import sys

for line in sys.stdin: # From standard input
    print(line) # to standard output
```

### Files

```py
with open(PATH_TO_FILE, mode='r') as f:
    line = f.readline()
```
multiple files
```py
with open("file_1.txt", mode="r") as f_in, open("file_2.txt", mode="w") as f_out:
    f_out.write(f_in.readline())
```

[source](https://www.w3schools.com/python/python_file_write.asp)

#### Modes

- x: create file, error if already exists
- r: 
- rb: 
- r+: 
- w: rewrite existing, create if does not exist
- wb: 
- w+: 
- wb+:
- a: append to existing, create if does not exist
- ab: 
- a+: 
- ab+:

[source](https://stackabuse.com/file-handling-in-python/)

#### Text files

```py
# Write xls from response.text to file #
pathToNewFile = '{folder}{file}'.format(folder=download_folder, file=xlsName)
# print('pathToNewFile', pathToNewFile)
with open(pathToNewFile, mode='tx') as newFile:
    newFile.write(response.text)
```

#### Binary files

```py
with open('image.png', mode='rb') as f:
    data = f.read(NUMBER_OF_BYTES)
    f.tell()                # tells position
    #Doesn't move the reading head
    #return at least desired number of bytes
    f.peek(NUMBER_OF_BYTES) 
```

[source](http://vyuka.ookami.cz/materialy/python/files/basics.xml)

### os

```py
import os

# Get full (absolute) path (maybe anti-pattern, dunno)
os.path.abspath("./build/knapsack.so")
```

### Asserting
```py
assert(len(tables)==1), f"len(tables) = {len(tables)}"
```

### Json

```py
import json

json_string = json.dumps({1: "yes", 2: "no", 3: "maybe"})
```

### Exceptions

```py
import json

json_string = "my json string"

# This is dangerous, if the string is not loadable, it will raise error
json_dict = json.loads(json_string)
```

Way to handle these is by try-except structures

```py
import json

json_string = "my json string"

try:
    json_dict = json.loads(json_string)
except json.decoder.JSONDecodeError as e:
    print(f'It was not possible to load "json_string" as a dictionary.',
        f'Error: "{e}", json_string: "{json_string}".')
```

- [exceptions (docs)](https://docs.python.org/3/library/exceptions.html)

## Advanced

### pdb — The Python Debugger

```py
import pdb; pdb.set_trace()
```

- [pdb (docs)](https://docs.python.org/3/library/pdb.html)

### Regex

```py
import re

# Using more flags
x = re.findall(r'CAT.+?END','Cat \n eND',flags=re.I | re.DOTALL)
```

#### Match 

Matches from the beginning of the string.

#### fullmatch

the whole pattern must match

[Module re](https://docs.python.org/2/library/re.html)
[Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

#### The special characters

| Pattern | Match group |
| --- | --- |
| `.` | in the default mode, this matches any character except a newline |
| `*` | Causes the resulting RE to match 0 or more repetitions of the preceding character |
| `+` | Causes the resulting RE to match 1 or more repetitions of the preceding character or RE |
| `?` | Causes the resulting RE to match 0 or 1 repetitions of the preceding RE |
| `|` | `A|B`, where A and B can be arbitrary REs, creates a regular expression that will match either A or B|
| `[]` | matches set of character (examples: [ce] match {'c', 'e'}, [c-e], match {'c', 'd', 'e'} [ce+] match {'c', 'd', '+'}, [^c] match anything except 'c')
| `\A` | matches only at the start of the string |
| `\Z` | matches only at the end of the string |
| `\d` | Matches any Unicode decimal digit |
| `\D` | matches any non-digit character; this is equivalent to the class [^0-9] |
| `\s` | Matches Unicode whitespace characters |
| `\S` | Matches any character which is not a whitespace character |
| `\w` | Matches Unicode word characters; this includes most characters that can be part of a word in any language, as well as numbers and the underscore |
| `\W` | Matches any character which is not a word character. This is the opposite of \w |
| `(?=...)` | Matches if ... matches next, but doesn’t consume any of the string |
| `(?!...)` | Matches if ... doesn’t match next |
| `(?<=...)` | Matches if the current position in the string is preceded by a match for ... that ends at the current position |
| `(?<!...)` | Matches if the current position in the string is not preceded by a match for .... |

### Lambda

```py
candidates[DEGREE] = candidates[[DEGREE, DEGREE_TMP]].apply(lambda x:
    np.nan if (pd.isnull(x[0]) & pd.isnull(x[1])) else
        x[0] if pd.isnull(x[1]) else
            x[1] if pd.isnull(x[0]) else x[0]+x[1], axis=1)
```

[More information](https://thispointer.com/python-how-to-use-if-else-elif-in-lambda-functions/)

### Datetime


```py
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
```

[datetime link](https://www.programiz.com/python-programming/datetime/current-time)

```
from datetime import datetime

datetime_str = '09/19/18 13:55:26'

datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

print(type(datetime_object))
print(datetime_object)  # printed in default format
```

[work with datetime](https://www.journaldev.com/23365/python-string-to-datetime-strptime) string to datetime

### pickle

Serialize objects to files and load objects from files.

```py
import pickle

# Have some object
MODELS = (dtc_model, gnb_model, lr_model, svc_model, mlp_model, knn_model)

# Save the object to a file
pickle.dump(MODELS, open(f"models/models_20_5.pkl", "wb"))

# At other time load it from the file
models = pickle.load(open("models/models_20_5.pkl", "rb" ))
```

### argparse

```py
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-t", "--type", choices=[NA, AA], help="reformat nucleic acid or amino acid sequence")
    args = parser.parse_args()
```

### Compress, decompress, checksum

```py
# Compute crc32 checksum
import zlib 
  
string = 'I want this checksum'

# using zlib.crc32() method 
checksum = zlib.crc32(s.encode())
checksum_1 = zlib.crc32(b"Also checksum of this.")

print(checksum, checksum_1) 
```
[python zlib](https://docs.python.org/3/library/zlib.html)

### underscored names in python


- `_single_leading_underscore`: weak "internal use" indicator. E.g. `from M import *` does not import objects whose names start with an underscore.
- `single_trailing_underscore_`: used by convention to avoid conflicts with Python keyword, e.g.
```py
tkinter.Toplevel(master, class_='ClassName')
```
- `__double_leading_underscore`: when naming a class attribute, invokes name mangling (inside `class FooBar`, `__boo` becomes `_FooBar__boo`; see below).

- `__double_leading_and_trailing_underscore__`: "magic" objects or attributes that live in user-controlled namespaces. E.g. `__init__`, `__import__` or `__file__`. Never invent such names; only use them as documented.

#### Dunders (double underscores)

```py
def getStuff(): return [1, "1", None, 4.5, {}];

def uniqueTypes():
    object_list = getStuff()
    return {type(x) for x in object_list}

# How to know if None was in object_list if we do not have it
types = uniqueTypes()
if None.__class__ in types:
    print("Function getStuff is corrupted, returns None while it should not")
```

### Garbage Collector

```py
import gc

gc.collect() # returns number of the number of unreachable objects
```

- [Garbage Collector interface (docs)](https://docs.python.org/3/library/gc.html)

### ctypes

- [top source](https://www.auctoris.co.uk/2017/04/29/calling-c-classes-from-python-with-ctypes/)
- [real python c binding](https://realpython.com/python-bindings-overview/)
- [documentation for c/python types](https://docs.python.org/3.6/library/ctypes.html)
- [source 2](https://medium.com/@stephenscotttucker/interfacing-python-with-c-using-ctypes-classes-and-arrays-42534d562ce7)
- [source 3](https://solarianprogrammer.com/2019/07/18/python-using-c-cpp-libraries-ctypes/)

```cpp
void c_fun(const char * bytes);
```

```py
c_fun("super unicode".encode())
```
[pass unicode as bytes](https://stackoverflow.com/questions/27285405/how-can-ctypes-be-used-to-parse-unicode-strings)

### Python 2 differences

#### Math in python 2 doesn't work well

```
>>> 4**2
16
>>> 16**(1/2)
1
```
---
