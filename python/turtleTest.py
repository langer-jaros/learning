#!/usr/bin/env python3
 
# import modulu
import turtle as t

# CONSTANTS
leng = 20
deg = 45
defClr = 'brown'
penSize = 3
ang = 25

# INITS
'''
ww, wh = t.window_height(), t.window_width()
ww_half = ww // 2
t.setworldcoordinates (-ww_half, 0, ww_half, ww)
'''

stack = []
t.color(defClr)
t.pensize(penSize)
t.left(90)
t.speed(0)
t.tracer(1000)

def showTree(s):
    for ch in s:
        if ch is '1':
            t.forward(leng)
        elif ch is '[':
            stack.append((t.pos(), t.heading()))
            t.left(deg)
        elif ch is ']':
            (p,h) = stack.pop()
            t.penup()
            t.setposition(p)
            t.pendown()
            t.setheading(h)
            t.right(deg)
        elif ch is '0':
            t.color('green')
            t.forward(leng)
            t.color(defClr)
    # hlavní GUI-smyčka (aby se okno nezavřelo samo od sebe)
    t.mainloop()
    # t.done()

def showPlant(s):
    for ch in s:
        if ch is 'F':
            t.forward(leng)
        if ch is '-':
            t.left(ang)
        if ch is '+':
            t.right(ang)
        elif ch is '[':
            stack.append((t.pos(), t.heading()))
        elif ch is ']':
            (p,h) = stack.pop()
            t.penup()
            t.setposition(p)
            t.setheading(h)
            t.pendown()

    # hlavní GUI-smyčka (aby se okno nezavřelo samo od sebe)
    t.mainloop()
    # t.done()


# RULES
'''
variables : 0, 1
constants: [, ]
axiom : 0
rules : (1 → 11), (0 → 1[0]0)
'''
# AUTOMAT
def tree(ch):
    if ch is '0':
        return '1[0]0'
    elif ch is '1':
        return '11'
    else:
        return ch
# RULES
'''
variables : X F
constants : + − [ ]
start : X
rules : (X → F+[[X]-X]-F[-FX]+X), (F → FF)
angle : 25°
'''
def plant(ch):
    if ch is 'X':
        return 'F+[[X]-X]-F[-FX]+X'
    elif ch is 'F':
        return 'FF'
    else:
        return ch

def getNextGen(sP):
    sN = ''
    fl = False
    automat = plant

    for ch in sP:
        fl = True if (ch is 'X') else False
        chN = automat(ch) if (fl) else ch
        sN += chN
    return sN

#s0 = '1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0'
s0 = 'X'
s1 = getNextGen(s0)
s2 = getNextGen(s1)
s3 = getNextGen(s2)
s4 = getNextGen(s3)
s5 = getNextGen(s4)
s6 = getNextGen(s5)
s7 = getNextGen(s6)
s8 = getNextGen(s7)

print(s1)
print(s2)
showPlant(s6)

'''
# nakreslení čtyř stran čtverce
for i in range(4):
    t.forward(100)
    t.left(90)
'''
 
'''
t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:
        break
t.end_fill()
'''