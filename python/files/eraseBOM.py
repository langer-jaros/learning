#!/usr/bin/env python3

import sys

assert (len(sys.argv) == 3 or len(sys.argv) == 4), "The number of input parameters is not sufficient ({})".format(len(sys.argv))

OLD_FILE_NAME = sys.argv[1]
NEW_FILE_NAME = sys.argv[2]
BOM_LENGTH = int(sys.argv[3]) if(len(sys.argv) == 4) else 6

with open(OLD_FILE_NAME, mode='br') as template:
    print(template.peek(BOM_LENGTH)[:BOM_LENGTH])
    bom = template.read(BOM_LENGTH)
    print(bom)
    print(template.tell())
    
    data = template.read()
    #print(len(data))
    
with open(NEW_FILE_NAME, mode='bx') as modified:
    modified.write(data)
