# Vim

Vi improved - visual text editor for life.

`2021 Feb 02, Jaroslav Langer`

## Contents

<!-- TOC GFM -->

* [Introduction](#introduction)
    * [Where to learn vim](#where-to-learn-vim)
    * [Vim modes](#vim-modes)
        * [Normal mode](#normal-mode)
        * [Insert mode](#insert-mode)
        * [Visual mode](#visual-mode)
        * [Command mode](#command-mode)
* [Basics](#basics)
    * [Basic movement](#basic-movement)
    * [Basic editing](#basic-editing)
        * [Insert mode editing](#insert-mode-editing)
    * [Basic operations](#basic-operations)
    * [Basic commands](#basic-commands)
    * [Search for pattern](#search-for-pattern)
    * [Copy from and past to clipboard](#copy-from-and-past-to-clipboard)
    * [Autocomplete](#autocomplete)
* [Advanced](#advanced)
    * [Advanced movement](#advanced-movement)
    * [Editing movement combination](#editing-movement-combination)
    * [Visual modes](#visual-modes)
    * [Change view](#change-view)
    * [Replace pattern](#replace-pattern)
    * [Other movements](#other-movements)
    * [Commands](#commands)
    * [Settings](#settings)
    * [Check spelling](#check-spelling)
* [Rest of the previous Czech version (something duplicated)](#rest-of-the-previous-czech-version-something-duplicated)
    * [Cut](#cut)
    * [Copy](#copy)
    * [Paste](#paste)
    * [General](#general)
    * [Find Character](#find-character)
    * [Find Pattern](#find-pattern)
    * [Commands](#commands-1)
    * [Visual mode](#visual-mode-1)
    * [More files](#more-files)
* [Configuration file](#configuration-file)

<!-- /TOC -->

## Introduction

* [What Are The Differences Between Vi And Vim? (shell-tips.com)](https://www.shell-tips.com/linux/vi-vs-vim/)

### Where to learn vim

1) Inside the vim editor.
   - `:Tutor` - start tutorial.
2) [vim tutor by Luke Smith](https://www.youtube.com/watch?v=d8XtNXutVto)
3) [learn by playing a game (vim adventures)](https://vim-adventures.com/)
4) [Basic Vi Commands (Colorado State University)](https://www.cs.colostate.edu/helpdocs/vi.html)

### Vim modes

#### Normal mode

* Every vim session starts in normal mode.
* In normal mode keys do not write down their letters, they all have special actions.

#### Insert mode

* Insert mode works the same as normal text editor.
    * If you type "b" the "b" appears on the screen.
* To enter the insert mode press `i`.
* Press `esc` to exit the insert mode.

#### Visual mode

* Visual mode enables to visually select the text and apply editing to the selection.
* To enter the visual mode press `v`.
* Press `esc` to exit the visual mode.

#### Command mode

* Command mode allows you to use advanced commands such as replacing text with regex.
    * It also allows you to set up the editor e.g. set search to be case insensitive.
* To enter the command mode press `:`.
* Use `backspace` to exit the command mode.

## Basics

### Basic movement

| Shortcut   | Action                  |
| :---:      | ---                     |
| j          | Move down.              |
| k          | Move up.                |
| h          | Move right.             |
| l          | Move left.              |
| gg         | Move to the first line. |
| shift+g    | Move to the last line.  |
| 12+shift+g | Move to the 12th line.  |
| :12        | Move to the line 12.    |
| ctrl+u     | Move half page up.      |
| ctrl+d     | Move half page down.    |

### Basic editing

| Shortcut | Action                                                         |
| :---:    | ---                                                            |
| dd       | Delete current line.                                           |
| yy       | Yank (copy) current line.                                      |
| p        | Paste deleted or yanked line below the cursor.                 |
| x        | Delete character under the cursor.                             |
| r8       | Replace the cursor character with number 8.                    |
| shift+r  | Start replacing all characters (like insert mode) until `esc`. |
| shift+j  | Delete current line's newline.                                 |

#### Insert mode editing

| shift+x  | Delete character before the cursor (backspace).               |
| i        | Start insert mode right before the cursor.                    |
| shift+i  | Start insert mode at the beginning of the line.               |
| a        | Start insert mode right after the cursor.                     |
| shift+a  | Start insert mode at the end of the line.                     |
| esc      | Exit insert mode = start normal mode.                         |
| o        | Create paragraph bellow the cursor and enter the insert mode. |
| shift+o  | Create paragraph above the cursor and enter the insert mode.  |

### Basic operations

| Shortcut        | Action              |
| :---:           | ---                 |
| u               | Undo action.        |
| ctrl+r          | Redo action.        |
| .               | Repeat last action. |

### Basic commands

| Keystrokes | Action                                               | Alternatives |
| ---        | ---                                                  |              |
| :q         | Quit vim.                                            |              |
| shift+zq   | Quit even though the file was changed.               | :q!          |
| :w         | Save file (write the changes to the file).           |              |
| shift+zz   | Save and quit.                                       | :x :wq       |
| :w !sh     | Execute like a shell script (write buffer to shell). | :w !bash     |

* [Execute current buffer as bash script from vim (stackexchange.com)](https://vi.stackexchange.com/questions/10209/execute-current-buffer-as-bash-script-from-vim)

### Search for pattern

| Keystrokes | Action                                              |
| :---:      | ---                                                 |
| /something | Search for "something" and go to the first match.   |
| n          | Go the next match.                                  |
| shift+n    | Go to the previous match.                           |
| *          | Search for the cursor word.                         |
| :noh       | Abbreviation for :nohlsearch (no highlight search). |

### Copy from and past to clipboard

Use the `y` and `p` the same way, only type `"+` before the action.
* e.g use `"+p` to paste the content from the clipboard or use `"+yy` to copy the current line.

### Autocomplete

| Shortcut | Action                         |
| :---:    | ---                            |
| ctrl+n   | Go to next recommendation.     |
| ctrl+p   | Go to previous recommendation. |

## Advanced

### Advanced movement

| Shortcut | Action                                        |
| :---:    | ---                                           |
| w        | Move to the beginning of the next word.       |
| shift+w  | Move one position after next whitespace.      |
| b        | Move to the beginning of the previous word.   |
| shift+b  | Move one position before previous whitespace. |
| e        | Move to the end of the next word.             |
| shift+e  | Move at the position before next whitespace.  |
| ge       | Move to the end of the previous word.         |
| $        | Move to the end of the line.                  |
| 0        | Move to the beginning of the line.            |
| ^        | Move to the beginning of the first word.      |
| {        | Move to the previous empty line (paragraph).  |
| }        | Move to the next empty line (paragraph).      |
| (        | Move to the previous sentence.                |
| )        | Move to the next sentence.                    |
| %        | Move to the matching  parentheses.            |

### Editing movement combination

dw - delete to the end of the word
shift+d d$ - delete to the end of the line

daw dap da( da"
diw dip di( di"

4k - Every action may start with number of repetition.

c - delete and trigger insert mode.
shift+c c$ - delete rest of the line and trigger insert mode.I

yap yaw

### Visual modes

v - triggers visual mode.
shift+v - triggers line visual mode.
ctrl+v - triggers block visual mode.

:norm 02wyl$p - example: go to the first character of second word and past it at the end.

### Change view

zt - move current line to the top.
zz - move cursor line to the middle.
zb - move cursor line to the bottom.

### Replace pattern

:/what_to_replace/with_what/ - replace one match
:/what_to_replace/with_what/g - g for replacing every match

### Other movements

ctrl+g - show current line of the file and percentage.
20% - move to the 20% of the document.
'' - go to the previous location

### Commands

Command mode starts with press of the key `:`.

| Command | Example usage | Description                             |
| :---:   | ---           | ---                                     |
| retab   | :retab        | Convert tabs to spaces.                 |
| !       | :!            | Runs any terminal command.              |
| w       | :w filename   | Write as a filename.                    |
| r       | :r filename   | Open file.                              |
| e       | :e filename   | Open new file.                          |
| qa      | :qa           | Quit all files.                         |
| sort    | :sort         |                                         |
| earlier | :earlier 15m  |                                         |
| later   | :later 10m    |                                         |
| source  | :so %         | Read file and treat it as a vim script. |

* [https://superuser.com/questions/132029/how-do-you-reload-your-vimrc-file-without-restarting-vim (superuser.com)](https://superuser.com/questions/132029/how-do-you-reload-your-vimrc-file-without-restarting-vim)

### Settings

| Command            | Action                                         |
| ---                | ---                                            |
| :set nu!           | turns on/off the line number                   |
| :set tabstop=4     | sets the number of spaces for tab              |
| :set softtabstop=0 |                                                |
| :set expandtab     |                                                |
| :set shiftwidth=4  |                                                |
| :set smarttab      |                                                |
| :set ignorecase    | also `set ic` search will be case insensitive  |

### Check spelling

| :setlocal spell! spelllang=en_us |                                    |
| :setlocal spell!                 |                                    |
| z                                | Get the dictionary to choose from. |
| ]s                               | Go to next missspelled word.       |

## Rest of the previous Czech version (something duplicated)

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

### Commands

| Command          | Action |
| ---              | --- |
| :s               | substituce (v zakladu stejna syntaxe jako sed)
| :%s/Line/line/g  | rozsah celeho souboru
| :%s/Line/line/gc | potvrzeni nahrady (y - ano, n - ne, a - ano a vsechny nasledujici, q - ukonci, l - ano a ukonci)


| Command  | Action |
| ---      | --- |
| :split   | rozdeli okno horizontalne
| :vsplit  | rozdeli okno vertikalne

### Visual mode

| Shortkey | Action |
| ---      | --- |
| v        | volny vyber oblasti |
| V        | radkovy vyber oblasti |
| Ctrl+v   | blokovy vyber oblasti |

- na vybranou oblast lze aplikovat prikazy d y c
- prikaz c smaze vybranou oblast a prejde do INSERT MODE
- ukonci se ESC ESC

### More files

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

* [How to configuration](https://www.linode.com/docs/guides/introduction-to-vim-customization/)

