# $\LaTeX$

`2021 Feb 04, Jaroslav Langer`

## Contents

<!-- TOC GFM -->

* [TeX vs LaTeX](#tex-vs-latex)
* [Install latex compiler](#install-latex-compiler)
* [Most basic latex you are good to go with](#most-basic-latex-you-are-good-to-go-with)
* [Compile .tex into pdf](#compile-tex-into-pdf)
* [Document class](#document-class)
* [Other TeXs](#other-texs)
* [XeLatex](#xelatex)

<!-- /TOC -->

## TeX vs LaTeX 

TeX is both a program (which does the typesetting, tex-core) and format (a set of macros that the engine uses, plain-tex). 
LaTeX is a generalised set of macros to let you do many things. Most people don't want to have to program TeX, especially to set up things like sections, title pages, bibliographies and so on. LaTeX provides all of that: these are the 'macros' that it is made up of.

* [what-is-the-difference-between-tex-and-latex (stackexchange)](https://tex.stackexchange.com/questions/49/what-is-the-difference-between-tex-and-latex)

## Install latex compiler

```sh
sudo apt-get install texlive-latex-base
```

* [Choosing_a_LaTeX_Compiler (overleaf.com)](https://www.overleaf.com/learn/latex/Choosing_a_LaTeX_Compiler)

## Most basic latex you are good to go with

* [LaTeX_mathematical_symbols (oeis.org)](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols)

| Symbol             | How to write it    |
| ---                | :---:              |
| $\in$              | `\in`              |
| $\subset$          | `\subset`          |
| $\forall$          | `\forall`          |
| $\exists$          | `\exists`          |
| $\emptyset$        | `\emptyset`        |
| $\setminus$        | `\setminus`        |
| $\{ \}$            | `\{ \}`            |
| $\left ( \right )$ | `\left ( \right )` |
| $\langle \rangle$  | `\langle \rangle`  |
| $\neq$             | `\neq`             |
| $\leq$ $\geq$      | `\leq` `\geq`      |
| $\to$              | `\to`              |
| $\infty$           | `\infty`           |
| $\varphi$          | `\varphi`          |
| $\mathbb{N}$       | `\mathbb{N}`       |
| $\land$            | `\land`            |
| $\cap$             | `\cap`             |
| $\bigcap$          | `\bigcap`          |
| $\textrm{normal}$  | `\textrm`          |
| $\cdot$            | `\cdot`            |
| $\odot$            | `\odot`            |
| $\circ$            | `\circ`            |
| $\times$           | `\times`           |
| mod $\quad$ p      | `\quad`            |
| $\dots$            | `\dots`            |
| $\implies$         | `\implies`         |
| $\equiv$           | `\equiv`           |
| $\partial$         | `\partial`         |
| $\nabla$           | `\nabla`           |
| $\sum$             | `\sum`             |
| $\prod$            | `\prod`            |
| $\mathcal{O}$      | `\mathcal{O}`      |
| $\sqrt[3]{x}$      | `\sqrt[3]{x}`      |

* [Greek letters (overleaf.com)](https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols)
* [Big O and related notations in LaTeX (texblog.com)](https://texblog.org/2014/06/24/big-o-and-related-notations-in-latex/)
* [Fractions and Roots (maths.tdc.ie/~dwilkins)](https://www.maths.tcd.ie/~dwilkins/LaTeXPrimer/FractsRoots.html)


## Compile .tex into pdf

```sh
pdflatex hello_tex.tex
```

## Document class

| class | usage |
| --- | --- |
| article | For articles in scientific journals, presentations, short reports, program documentation, invitations, ... |
| IEEEtran | For articles with the IEEE Transactions format. |
| proc | A class for proceedings based on the article class. |
| report | For longer reports containing several chapters, small books, thesis, ... |
| book | For books. |
| slides | For slides. The class uses big sans serif letters. |
| memoir | For changing sensibly the output of the document. It is based on the book class, but you can create any kind of document with it [1] |
| letter | For writing letters. |
| beamer | For writing presentations (see LaTeX/Presentations). |

## Other TeXs

* (The TeX family tree: LaTeX, pdfTeX, XeTeX, LuaTeX and ConTeXt (overleaf.com))[https://www.overleaf.com/learn/latex/Articles/The_TeX_family_tree:_LaTeX,_pdfTeX,_XeTeX,_LuaTeX_and_ConTeXt]

## XeLatex

* [font problems -> xetex](https://stackoverflow.com/questions/25969041/package-inputenc-error-unicode-char-u8%CE%B2-not-set-up-for-use-with-latex)
* [install xetex](https://tex.stackexchange.com/questions/179778/xelatex-under-ubuntu)
[tex to pdf](https://tug.org/pipermail/xetex/2009-November/014991.html)
* [xetex in vs code](https://stackoverflow.com/questions/56109128/enable-xelatex-in-latex-workshops-for-visual-studio-code)

