# How to Python

## MENU

## First things first
```
#!/usr/bin/env python3
```

## Printing

## Variables

## Data types

## Conditions

## Loops

## Imports
```
from xy import xyz as x
```

## Inputs
### Arguments
```
import sys
print ("the script has the name: {}".format(sys.argv[0]))
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

## Math
### ?
```
>>> 4**2
16
>>> 16**(1/2)
1
```
---
## jupyter notebook
[install](https://jupyter.org/install)
http://guessthecorrelation.com/

---
`2019/12/04, Jaroslav Langer`