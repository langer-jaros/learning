# Vi

## Contents <!-- omit in toc -->

- [Introduction](#introduction)
  - [Copy from and past to clipboard](#copy-from-and-past-to-clipboard)
  - [Autocomplete](#autocomplete)
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

Where to learn vim
1) In vim
   - `:Tutor` - start tutorial.
2) [vim tutor by Luke Smith](https://www.youtube.com/watch?v=d8XtNXutVto)
3) [learn by playing a game (vim adventures)](https://vim-adventures.com/)
4) [Basic Vi Commands (Colorado State University)](https://www.cs.colostate.edu/helpdocs/vi.html)

#### Basic movement

| Shortcut | Action      |
| :---:    | ---         |
| j        | move down.  |
| k        | move up.    |
| h        | move right. |
| l        | move left.  |

#### Basic editing

| Shortcut | Action                                          |
| :---:    | ---                                             |
| x        | Delete character.                               |
| dd       | Delete current line.                            |
| yy       | Yank (copy) current line.                       |
| p        | Paste content below the cursor line.            |
| i        | Start insert mode right before the cursor.      |
| shift+i  | Start insert mode at the beginning of the line. |
| a        | Start insert mode right after the cursor.       |
| shift+a  | Start insert mode at the end of the line.       |
| esc      | Exit insert mode = start normal mode.           |

#### Basic operations

| Shortcut        | Action         |
| :---:           | ---            |
| u               | Undo action.   |
| ctrl+r          | Redo action.   |
| :q shift+zq     | Quit.          |
| :x :wq shift+zz | Save and quit. |

#### Advanced movement

| Shortcut | Action                                          |
| :---:    | ---                                             |
| w        | Move to the next beginning of a word.           |
| shift+w  | Move one position after next whitespace.        |
| b        | Move to the previous beginning of a word.       |
| shift+b  | Move one position before previous whitespace.   |
| e        | Move to the end of the next word.               |
| shift+e  | Move at the position before next whitespace.    |
| ge       | Move to the end of previous word.               |
| $        | Move cursor to the end of a line.               |
| 0        | Move cursor to the beginning of a line.         |
| ^        | Move cursor to the beginning of the first word. |

dw - delete to the end of the word
shift+d d$ - delete to the end of the line

ctrl+u - move half page up
ctrl+d - move half page down

zt - move current line to the top.
zz - move cursor line to the middle.
zb - move cursor line to the bottom.

{ - move to the previous empty line.
} - move to the next empty line.
( - Move to the previous sentence.
) - Move to the next sentence.

daw dap da( da"
diw dip di( di"

4k

:sort
:earlier 15m
:later 10m

r - Replace one character.
shift+r - Replace multiple characters (replace, not insert).

c - delete and trigger insert mode.
shift+c c$ - delete rest of the line and trigger insert mode.I

ctrl+g - show current line of the file and percentage.
20% - move to the 20% of the document.
shift+g - move to the end of the document.
gg - move to the top of the document.

/ - go to the first result of searched thing
n - go the next match
shift+n - go to the previous match.

o - creates paragraph bellow the cursor and trigger insert mode.
shift+o - creates paragraph beneath the cursor and trigger the insert mode.

% - move the cursor (to matching) parentheses.

:/what_to_replace/with_what/ - replace one match
:/what_to_replace/with_what/g - g for replacing every match

'' - go to the previous location

:! - runs any terminal command

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

### Copy from and past to clipboard

Use the `y` and `p` the same way, only type `"+` before the action.
- e.g use `"+p` to paste the content from the clipboard or use `"+yy` to copy the current line.

### Autocomplete

| Shortcut | Action |
| :---:    | --- |
| ctrl+n   | Go to next recommendation.     |
| ctrl+p   | Go to previous recommendation. |

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

Command mode starts with press of the key `:`.

| Command     | Action                          |
| ---         | ---                             |
| :q          | Quit vi.                        |
| :q!         | Force the quit no matter what.  |
| :w          | Write the changes to the file.  |
| :w filename | Write as a filename.            |
| :r filename | Open file.                      |
| :e filename | Open new file.                  |
| :wq         | Write changes and quit.         |
| :qa         | Quit all files.                 |
| :retab      | Convert tabs to spaces.         |

| Command          | Action |
| ---              | --- |
| :s               | substituce (v zakladu stejna syntaxe jako sed)
| :%s/Line/line/g  | rozsah celeho souboru
| :%s/Line/line/gc | potvrzeni nahrady (y - ano, n - ne, a - ano a vsechny nasledujici, q - ukonci, l - ano a ukonci)

| Command            | Action                                         |
| ---                | ---                                            |
| :set nu!           | turns on/off the line number                   |
| :set tabstop=4     | sets the number of spaces for tab              |
| :set softtabstop=0 |
| :set expandtab     |
| :set shiftwidth=4  |
| :set smarttab      |
| :set ignorecase    | also `set ic` search will be case insensitive  |


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
