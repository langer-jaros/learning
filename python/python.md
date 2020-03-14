# Python

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
+ [Python 2 differences](#python-2-differences)

## First things first
```
#!/usr/bin/env python3
```

## Printing
```py
>>> print('"len(myArr[3])": {}'.format(len(myArr[3]):))
"len(myArr[3])": 7
```

## Variables
?

## Data types

### len()
priceless method, can be used for number of characters of a string as well as number of elements of an array

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

### Lists

Generator notation
```
myList = [x for x in range(5)]
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
```
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
```
with open('obrazek.png', mode='rb') as f:
    data = f.read(NUMBER_OF_BYTES)
    f.tell()                # tells position
    #Doesn't move the reading head
    #return at least desired number of bytes
    f.peek(NUMBER_OF_BYTES) 
```
[source](http://vyuka.ookami.cz/materialy/python/files/basics.xml)

## Asserting
```
assert(len(tables)==1), "len(tables) = {}".format(len(tables))
```

## Python 2 differences

### Math in pyton2 doesn't work well
```
>>> 4**2
16
>>> 16**(1/2)
1
```
---
`2020/02/29, Jaroslav Langer`