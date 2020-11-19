# Linux

The art of using PC like a human being.

```2020/11/14, Jaroslav Langer, using linux mint 19```

## Terminal

### Copy and past in terminal

#### Copy from terminal

Highlight the text and press Ctrl+Shift+C

#### Past to terminal

Press Ctrl+Shift+V

### Linux directory structure

+ /bin - executables
+ /home/* | /root - *users | roots personal data
+ /opt – Optional software (thigs you can't instal with package manager)
+ /etc - configuration files
+ /lib – Shared libraries

- [More information](https://linuxhandbook.com/linux-directory-structure/)

### Type special characters

Perhaps to write a dash, in linux there is a way to write unicode symbols.

1) press Ctrl+Shift+U
1) type the unicode code, perhaps 2014
1) press Space

## Set caps lock to esc

1) System Settings
2) Keyboard 
3) Layouts
4) Options
5) Caps Lock key behavior
6) Select Make Caps Lock an additional ESC

## Set key stroke rate

```sh
xset r rate 200 20
```

## Computers

### BOM

Byte order mark (BOM) is a particular usageof the special Unicode character, U+FEFF`

#### UTF-8 bom

```sh
0xEF,0xBB,0xBF
```

#### UTF-16 BOM

```sh
U+FEFF
```

- [Source](https://en.wikipedia.org/wiki/Byte_order_mark)

