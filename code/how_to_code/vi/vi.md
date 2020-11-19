# vi

## Contents <!-- omit in toc -->

- [Introduction](#introduction)
- [Normal mode](#normal-mode)
  - [Move](#move)
  - [Edit](#edit)
  - [Cut](#cut)
  - [Copy](#copy)
  - [Paste](#paste)
  - [General](#general)
  - [Find Character](#find-character)
  - [Find Pattern](#find-pattern)
- [Insert mode](#insert-mode)
- [Command mode](#command-mode)
- [Visual mode](#visual-mode)
- [More files](#more-files)
- [Configuration file](#configuration-file)

## Introduction

:Tutor - start tutorial.

j - move down.
k - move up.
h - move right.
l - move left.

u - undo stuff
ctrl+r - redo

x - delete character.
i a - start insert move before/after cursor.
I A - start insert mode at the beginning/end of the line.

:q ZQ - quit.
:wq ZZ x - save and quit.

dw - delete to the end of the word
D d$ - delete to the end of the line

w - move to the next beginning of a word.
e - move to the next end of a word.
b - move to the previous beginning of a word. 
$ - move cursor to the end of a line.
0 - move cursor to the beginning of a line.
^ - move cursor to the beginning of the first word.

dd - delete line

ctrl+u - move half page up
ctrl+d - move half page down

zt - move current line to the top.
zz - move cursor line to the middle.
zb - move cursor line to the bottom.

{ - move to the previous empty line.
} - move to the next empty line.

daw dap da( da"
diw dip di( di"

4k

:sort
:earlier 15m
:later 10m

p - paste below the cursor

r - replace content with something.

c - delete and trigger insert mode.
C c$ - delete rest of the line and trigger insert mode.I

ctrl+g - show current line of the file and percentage.
20% - move to the 20% of the document.
shift+g - move to the end of the document.
gg - move to the top of the document.

/ - go to the first result of searched thing
n - go the next match
shift+N - go to the previous match.

o - creates paragraph bellow the cursor and trigger insert mode.
O - creates paragraph beneath the cursor and trigger the insert mode.

% - move the cursor (to matching) parentheses.

:/what_to_replace/with_what/ - replace one match
:/what_to_replace/with_what/g - g for replacing every match

'' - go to the previous location

:! - runs any terminal command

y - yanks (copy)
yap yaw  

v - triggers visual mode.
shift+v - triggers line visual mode.	
ctrl+v - triggers block visual mode.

:setlocal spell! spelllang=en_us
:setlocal spell!
z - get the dictionary to choose from.
]s - go to next missspelled word.

. - repeat last action.
:norm 02wyl$p - example: go to the first character of second word and past it at the end.

## Normal mode

### Move

| Shortkey | Action
| ---      | --- |
| h j k l  | kurzorove sipky |
| gg       | prvni radek |
| G        | posledni radek |
| n G      | n-ty radek |
| w        | zacatek dalsiho slova |
| e        | konec dalsiho slova |
| b        | zacatek predchoziho slova |
| {        | nasledujici odstavec (prazdny radek) |
| }        | predchozi odstavec (prazdny radek) |

### Edit

| Shortkey | Action |
| ---      | --- |
| x        | vyjme znak na kurzoru (3x aktualni + 2 dalsi) |
| X        | vyjme znak pred kurzorem (BACKSPACE) |
| r [char] | nahradi znak na kurzoru |
| J        | odstrani konec radku na kurzoru (spoji radky) |
| a        | spusti editaci na aktualni pozici kurzoru (jako i) |
| A        | spusti editaci na konci aktualniho radku |
| o        | otevre novy radek pod aktualnim |
| O        | otevre novy radek pred aktualnim |

### Cut

| Shortkey | Action |
| ---      | --- |
| dd       | aktualni radek (5dd aktualni + 4 dalsi) |
| dw       | znaky od kurzoru do konce slova |
| d$       | znaky od kurzoru do konce radky |
| d^       | znaky od kurzoru do zacatku radky |

### Copy

| Shortkey | Action |
| ---      | --- |
| yy       | aktualni radek (5yy aktualni + 4 dalsi)
| yw       |
| y$       |
| y^       |

### Paste

| Shortkey | Action |
| ---      | --- |
| p        | vlozi data z buffer za aktualni radek |
| P        | vlozi data z buffer pred aktualni radek |

### General

| Shortkey | Action |
| ---      | --- |
| .        | opakuje posledni prikaz |
| u        | undo |
| Ctrl+r   | redo |

### Find Character

| Character | Action |
| ---       | --- |
| f [char]  | vyhleda zadany znak na aktualnim radku v oblasti za kurzorem
| F [char]  | vyhleda zadany znak na aktualnim radku v oblasti pred kurzorem
| t [char]  | vyhleda a skoci pred zadany znak na aktualnim radku v oblasti za kurzorem
| T [char]  | vyhleda a skoci za zadany znak na aktualnim radku v oblasti pred kurzorem
| ;         | najde dalsi vyskyt znaku
| ,         | najde dalsi vyskyt znaku v opacnem smeru

### Find Pattern

| Pattern     | Action |
| ---         | --- |
| / [pattern] | vyhleda vzor v oblasti za kurzorem |
| ? [pattern] | vyhleda vzor v oblasti pred kurzorem |
| n           | najde dalsi vyskyt vzoru |
| N           | najde dalsi vyskyt vzoru v opacnem smeru |

## Insert mode

- po stisku klavesy i v normalnim modu
- umoznuje pouze zakladni editaci
- ukonci se ESC

## Command mode

- po stisku klavesy :

| Command     | Action |
| ---         | --- |
| :q          | ukonci |
| :q!         | ukonci bez kontroly ulozeni |
| :w          | zapis zmeny do existujiciho souboru |
| :w filename | uloz soubor |
| :r filename | otevri soubor |
| :e filename | otevri novy soubor |
| :wq         | zapis a ukonci |
| :qa         | ukonci vsechny soubory |

| Command          | Action |
| ---              | --- |
| :s               | substituce (v zakladu stejna syntaxe jako sed)
| :%s/Line/line/g  | rozsah celeho souboru
| :%s/Line/line/gc | potvrzeni nahrady (y - ano, n - ne, a - ano a vsechny nasledujici, q - ukonci, l - ano a ukonci)

| Command            | Action |
| ---                | --- |
| :set nu!           | zapne/vypne cisla radku |
| :set tabstop=4     | nastavi pocet mezer tabulatoru |
| :set softtabstop=0 |
| :set expandtab     |
| :set shiftwidth=4  |
| :set smarttab      |

| Command  | Action |
| ---      | --- |
| :split   | rozdeli okno horizontalne
| :vsplit  | rozdeli okno vertikalne

## Visual mode

| Shortkey | Action |
| ---      | --- |
| v        | volny vyber oblasti |
| V        | radkovy vyber oblasti |
| Ctrl+v   | blokovy vyber oblasti |

- na vybranou oblast lze aplikovat prikazy d y c
- prikaz c smaze vybranou oblast a prejde do INSERT MODE
- ukonci se ESC ESC

## More files

```bash
# otevre soubory v horizontalne rozdelenem okne
vi -o file1 file2
# otevre soubory ve vertikalne rozdelenem okne
vi -O file1 file2
```

| Shortkey          | Action |
| ---               | --- |
| Ctrl + w + w      | prepnuti mezi okny
| Ctrl + w + [hjkl] | prepnuti do sousedniho okna v danem smeru

## Configuration file

- [How to configuration](https://www.linode.com/docs/guides/introduction-to-vim-customization/)
