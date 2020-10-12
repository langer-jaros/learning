# Python

`2020/03/17, Jaroslav Langer`

## MENU

- [Comments](#comments)
- [First things first](#first-things-first)
- [Printing](#printing)
- [Variables](#variables)
- [Data types](#data-types)
- [Conditions](#conditions)
- [Loops](#loops)
- [Imports](#imports)
- [Inputs, outputs](#inputs,-outputs)
- [Asserting](#asserting)
- [json](#json)

Advanced
- [Regex](#regex)
- [lambda](#lambda)
- [datetime](#datetime)
- [argparse](#argparse)
- [compress, decompress, checksum](#compress,-decompress,-checksum)
- [ctypes](#ctypes)
- [Python 2 differences](#python-2-differences)

## Links

[Tutorial place](https://realpython.com/)

## Comments

```py
# Oneline coment

"""
multiline comment
"""

'''
multiline comment
'''
```

### Docstrings

Every file, class, function can have doc string (__doc__).
Write docstrings, they are beatiful.

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
    "function docstring"

class cla:
    "class docstring"
```

## First things first

### Scripts

Python is and excelent language for writing scripts. Every script on linux should start with. Otherwise, there will be misunderstanding between python2 and 3 guys.
```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```
For usage python files as scripts is highly recommend to use following
```py
if __name__ == "__main__":
    #This code will be executed only, if the file was called as a script, not imported
```

### Objects

Nearly everything in a python is object. String is an object, list is an object. It's very handy to see all the atributes and methods any object.
```py 
dir(anything)
```

## Printing
```py
>>> print('"len(myArr[3])": {}'.format(len(myArr[3]):))
"len(myArr[3])": 7
```

## Variables
?

## Handy methods

### len()
priceless method, can be used for number of characters of a string as well as number of elements of an array

### Slicing

Basicly anything, which can be iterated retrieve slice, after useing [:]
```py
string[firstLetter:LetterNotToBeSeen]
array[firstItem:] #To the end
array[firstItem:-1] #To the end
array[firstItem:-5] #To the fifth last
```

Examples
```py
# Slice DOCTYPE out of html #
text = text[len('<!DOCTYPE html>\n'):]
```

## Data types

### type()

Recognize type of a passed object
```
type(a) == type({})
```

## String

There is four types how to quote a string
```py
# Two equivalens how write single-line string
'string'
"another string"
# Two equivalens how write multi-line string
'''
multiline string
'''
"""
another multiline string
"""
```
Raw string
```py
r'in this string, the \n won\'nt be and newline'
```

### Format and f string
```py
# Using stirng.format()
pathToNewFile = '{folder}{file}.{fileType}'.format(
    folder=download_folder, file=xlsName, fileType='xls')
# f string
pathToNewFile = f'{download_folder}{xlsName}.{"xls"}'
```

### String functions

```py
# slit
"string string2".split()
# join
' '.join(['string', 'string2', 'string3'])
# strip
"          string                ".strip()
# find
"string about nothing".find('abo')
# rfind
".hiden_file_.txt".rfind('.')

# count
question = "Hi mom, how much coins i need to buy coin keeper for my coin sessions?"
question.count("coin") # 3
```

## Bytes

```py
bytes_1 = b"Bytes form this string"
bytes_2 = "Bytes form this string".encode()

string_from_bytes = bytes_1.decode()
```

[link](https://www.tutorialspoint.com/python/string_decode.htm)

## Collections

### Lists

```py
l = ["a", "b"]
ll = ["c", "d"]
# Append
l.append(ll)
# Pop
l.pop()
# Extend
ll.extend(l)
# Insert
ll.insert(index, item)
# Convert string to list
list("All the beautiful strings")
```

Generator notation
```py
myList = [x for x in range(5)]
```
Copy vs. deep copy
```py
# Shallow copy, changes in list2 affects list1
list2 = list1
# Two independent lists, changes in one doesn't effect the other one
list2 = list1.copy()
```

### Dictionary

```py
# For loop with dictionaries
for key in myDict:
    print(myDict[key])

for key, value in myDict.items():
    print(key)
    print(value)
```

## Conditions

ternary assigning
```
variable = value if (condition) else otherValue
```

## Loops

[top](#python)
```py
for x in almostAnything:
    print(x)
```

## Imports
```py
from xy import xyz as x
```

## Inputs, outputs

### Input arguments

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

### Standard input

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
with open('obrazek.png', mode='rb') as f:
    data = f.read(NUMBER_OF_BYTES)
    f.tell()                # tells position
    #Doesn't move the reading head
    #return at least desired number of bytes
    f.peek(NUMBER_OF_BYTES) 
```

[source](http://vyuka.ookami.cz/materialy/python/files/basics.xml)

## os

```py
import os

# Get full (absolute) path (maybe antipattern, dunno)
os.path.abspath("./build/knapsack.so")
```

## Asserting
```py
assert(len(tables)==1), f"len(tables) = {len(tables)}"
```

## Json

```py
import json

json_string = json.dumps({1: "yes", 2: "no", 3: "maybe"})
```

## Regex

```py
import re

# Using more flags
x = re.findall(r'CAT.+?END','Cat \n eND',flags=re.I | re.DOTALL)
```

### Match 

Matches from the begining of the string

### fullmatch

the whole pattern must match

[Module re](https://docs.python.org/2/library/re.html)
[Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

## Lambda

```py
candidates[DEGREE] = candidates[[DEGREE, DEGREE_TMP]].apply(lambda x:
    np.nan if (pd.isnull(x[0]) & pd.isnull(x[1])) else
        x[0] if pd.isnull(x[1]) else
            x[1] if pd.isnull(x[0]) else x[0]+x[1], axis=1)
```

[More information](https://thispointer.com/python-how-to-use-if-else-elif-in-lambda-functions/)

## Datetime


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

## argparse

```py
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-t", "--type", choices=[NA, AA], help="reformat nucleic acid or amino acid sequence")
    args = parser.parse_args()
```

## Compress, decompress, checksum

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


## ctypes

[top source](https://www.auctoris.co.uk/2017/04/29/calling-c-classes-from-python-with-ctypes/)
[real pyhton c binding](https://realpython.com/python-bindings-overview/)
[read docu for c/python types](https://docs.python.org/3.6/library/ctypes.html)
[source 2](https://medium.com/@stephenscotttucker/interfacing-python-with-c-using-ctypes-classes-and-arrays-42534d562ce7)
[source 3](https://solarianprogrammer.com/2019/07/18/python-using-c-cpp-libraries-ctypes/)

```cpp
void c_fun(const char * bytes);
```

```py
c_fun("super unicode".encode())
```
[pass unicode as bytes](https://stackoverflow.com/questions/27285405/how-can-ctypes-be-used-to-parse-unicode-strings)

## Python 2 differences

### Math in pyton2 doesn't work well
```
>>> 4**2
16
>>> 16**(1/2)
1
```
---
