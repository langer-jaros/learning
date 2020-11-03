# vi

## Contents <!-- omit in toc -->

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
