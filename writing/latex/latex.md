# Latex


## TeX vs LaTeX 

TeX is both a program (which does the typesetting, tex-core) and format (a set of macros that the engine uses, plain-tex). 
LaTeX is a generalised set of macros to let you do many things. Most people don't want to have to program TeX, especially to set up things like sections, title pages, bibliographies and so on. LaTeX provides all of that: these are the 'macros' that it is made up of.

[source](https://tex.stackexchange.com/questions/49/what-is-the-difference-between-tex-and-latex)

## Install latex compiler

```sh
sudo apt-get install texlive-latex-base
```

[more](https://www.overleaf.com/learn/latex/Choosing_a_LaTeX_Compiler)

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