#!/usr/bin/env python3

BOM_LENGTH = 6
OLD_FILE_NAME = ''
NEW_FILE_NAME = ''

with open(OLD_FILE_NAME, mode='br') as template:
    print(template.peek(BOM_LENGTH)[:BOM_LENGTH])
    bom = template.read(BOM_LENGTH)
    print(bom)
    print(template.tell())
    
    data = template.read()
    #print(len(data))
    
with open(NEW_FILE_NAME, mode='bx') as modified:
    modified.write(data)
