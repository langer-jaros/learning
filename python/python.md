# Python

`2020/03/17, Jaroslav Langer`

## TODO

+ work with datetime [link](https://www.journaldev.com/23365/python-string-to-datetime-strptime) string to datetime

## MENU

+ [First things first](#first-things-first)
+ [Printing](#printing)
+ [Variables](#variables)
+ [Data types](#data-types)
+ [Conditions](#conditions)
+ [Loops](#loops)
+ [Imports](#imports)
+ [Input arguments](#input-arguments)
+ [Files](#files)
+ [Asserting](#asserting)

Advanced
+ [Regex](#regex)
+ [lambda](#lambda)
+ [Python 2 differences](#python-2-differences)

## First things first

### Scripts

Python is and excelent language for writing scripts. Every script on linux should start with. Otherwise, there will be misunderstanding between python2 and 3 guys.
```py
#!/usr/bin/env python3
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

### String

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

#### Format and f string
```py
# Using stirng.format()
pathToNewFile = '{folder}{file}.{fileType}'.format(
    folder=download_folder, file=xlsName, fileType='xls')
# f string
pathToNewFile = f'{download_folder}{xlsName}.{"xls"}'
```

## Collections

### Lists

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

## Input arguments

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

## Files

### Text files

```py
# Write xls from response.text to file #
pathToNewFile = '{folder}{file}'.format(folder=download_folder, file=xlsName)
# print('pathToNewFile', pathToNewFile)
with open(pathToNewFile, mode='tx') as newFile:
    newFile.write(response.text)
```

### Binary files
```py
with open('obrazek.png', mode='rb') as f:
    data = f.read(NUMBER_OF_BYTES)
    f.tell()                # tells position
    #Doesn't move the reading head
    #return at least desired number of bytes
    f.peek(NUMBER_OF_BYTES) 
```

[source](http://vyuka.ookami.cz/materialy/python/files/basics.xml)

## Asserting
```py
assert(len(tables)==1), f"len(tables) = {len(tables)}"
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

## Python 2 differences

### Math in pyton2 doesn't work well
```
>>> 4**2
16
>>> 16**(1/2)
1
```
---
