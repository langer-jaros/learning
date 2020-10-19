# Shell 

The art of using PC like a human being

```2020/09/11, Jaroslav Langer, using linux mint 19```

## MENU

Basics - [click](#basics)

- [First of all](#first-of-all)
- [Shell principle - commands structure](#shell-principle---commands-structure)
- [Paths](#paths)
- [Manipulation with files and directories](#manipulation-with-files-and-directories)
- [Find anything](#find-anything)
- [Wildcards - symbols with special meaning](#wildcards---symbols-with-special-meaning)
- [Install stuff](#install-stuff)
- [Compression and decompression](#Compression-and-decompression)

Advanced - [click](#advanced)

- [User management and priviledges](#user-management-and-priviledges)
- [Files - introduction](#files---introduction)
- [Compare two files](#compare-two-files)
- [Usefull commands - good to know](#usefull-commands---good-to-know)
- [Practicals](#practicals)
- [ssh](#ssh)
- [Find process](#find-process)
- [Enviroments and variables](#enviroments-and-variables)
- [History](#history)
- [Regular Expressions](#regular-expressions)
- [Vi basics](#vi-basics)

Linux - [click](#linux)
- [Linux directory structure](#linux-directory-structure)
- [Type special characters](#Type-special-characters)

Computers - [click](#computers)
- [BOM](#bom)

Theory from seminars - [click](#theory-from-seminars)

## Todo

1) difference between bash, shell, terminal etc

1)

```sh
top
```

---

## Introduction

This document is written in purpose to simplify the access to the advanced usage of a computer.
The knowledge is based on the PVS course of VSCHT, Prague.

### Conventions and symbols

- [ ] (square brackets) - means optionality i.e. the things inside may be left out
- / (slash) - means exclusive or i.e. it is possible to use either the left or the right part but not both
- | (vertical bar) - means logical (inclusive) or between the the things on the right and on the left
- CAPITAL_LETTER - the words written in uppercase means they should be substituted - in this case with "A" for example. 

Basics
===

## Open terminal

Press Ctrl+Alt+T.

If it does not work:
1) open menu ~ press super key (windows key)
1) type "term" and you should see either "Terminal", "xterm" or something similar.
1) open it ~ press Enter (double-click).

### Putty access from Windows

TBD

147.251.253.55

## The terminal enviroment

Once the terminal is open, what you see is the Command-line interface (CLI).
On the left to the cursor is the prompt, which prompts you to take action.

Usually the prompts tells a name of a current user, the name of the machine (hostname) and the location where the user is relatively to the machine (path). Typicaly it also shows, whether the logged user is a normal user ($) or superuser (#).

Example of common appearance should be:

```
USER_NAME@HOSTNAME:PATH$
```

## First of all

### USE TAB autocompletion

Whenever, you press tab, the terminal autocomplete the word you are writting.
If there is more than one posibility, nothing happens. Until you press tab twice.
Than it shows you the all the possible completions.
**It's unbeliveable great feature**.

---

## Shell principle 

There are planty of things you can do in terminal. 
However the more programming-like stuff will be usually enclosed to bash script.
That means, the work with terminal (shell) will be mostly about using commands to do the job for you.

### What happens when i type to terminal

Shell has many words reserved it can be "echo" for printing, "exit" for leaving, or "if" for conditioning.
Besides these, anything you write to the terminal shell expects to be a command.

### Commands structure

Next to the prompt there is a place for typing commands. 
Shell is case-sensitive, so `exit` works, where `Exit` doesn't.

The shell works like this. 
- The line is executed on press of an enter.
- Most simple is to put one command on one line.
- For one command scenario, the line starts with a command name, folow options and arguments
- Options can be either
    + single letter, starts with hyphen-minus character `-x`
    + full text (no spaces), stars with double minus `--xxxx`
- Argument can be anything

Command structure
```sh
command [-o | --options] [arguments]
```
[Back to menu](#menu)

### Expansions

Not everything you write shell interprets as you wrote it. 
Many characters are expanded. Such as ~ is expanded as /home/your_username

There are various [expansions](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html)
for now is good to know, that double quotes suppres any expansions except the starting with dolar such as "$USER".

The single quotes supress any expansions.
---

## Comments

Comments are also more useful for writting bash scripts but it is important to know what the hesh means.
The terminal ignores the whole line, which follows after this symbol #

```sh
# here can be written anything and nothing happens
```

## Files and directories

### Paths

There is always a need to specify a path to the file a directory you want to work with.
The file can be a document you want to read, an image or simply anything.
Directory is a container for such a files and other directories.
Besides the files and directories the path may specify a command to be used.

There is already a [directory structure](#linux-directory-structure) by default.
Important is that there is one root directory, where every other directories are either in the root directory or nested into its subdirectories. Also every user has its own user directory.
At every point in a terminal you are in some directory.

```sh
# Path to the root dicionary
/

# Path to the current dictionary
.

# Path to your home dicionary
~

# Dictionary separator
/

# Show path to the current dictionary
pwd
```

If i would have a directory called "tutorial" in my user directory, the path would be

```sh
# The path to the tutorial directory
/home/USER_NAME/tutorial

# or
~/tutorial

# or, if I am in my user directory
./tutorial
```

[Back to menu](#menu)

## Manipulation with files and directories

```sh
# Go (move) to the specified dictionary
cd ./path/to/the/dictionary

# Create new directory
mkdir NEW_DIRECTORY

# Copy file1 to file2
cp file1 file2
# Copy all from dir1 to dir2
cp -r dir1 dir2

# Move file to another place
mv /old/path/to/file1 /new/path/to/file1

# Rename file1 as file2 and check if not overwriting
mv -i file1 file2

# Create new directory and put everything in
mv ./!(dir1) ./dir1/

# Remove file
rm file
# Remove directory (recursively with all files)
rm -r
```
[Back to menu](#menu)

## Information about files, directories

### Commands: ls, tree, du, wc, stat

```sh
# Shows all files of given directory
ls ./path/to/the/directory

# Show structure of all files and dictionaries from your dictionary 
tree

# Shows counts of lines, words and bytes
wc FILE_NAME
# show number of lines (-l) words (-w) and bytes (-c)
wc -l FILE_NAME

# Recursively shows sizes (disk usage) of directories and files 
du ./path/to/the/directory 
# Show size of the DIRECTORY and its direct children (2 ~ levels down etc.) 
du -d 1 ./path/to/the/DIRECTORY

# show file statistics
stat file1
```

## Find anything

```sh
find /  -name   "toBeFound"     ACTIONS -delete
        -regex  '.*anything.*'
        -type f d l s                   -ls 
        -user                           -exec ls -l {} \;
        -size   +-nc k M G              -ok
        -empty
        -mindepth -maxdepth n
        -perm 	400 	u=rw 	-u=rmw 	/u=r,o=x
		-user 	langera
		-group
```
[Back to menu](#menu)

---

## Wildcards - symbols with special meaning

Especially useful when we don't know the name exactly or we perpahps want to use more than one exact name.

```sh
# Anything
*

# One character
?

# Not containig anything from bracket
[! ]
# Equivalent in RegEx
[^ ]

# Ranges
[a-dsu]
[3-7a-g]

# Groups
[:digit:]
[:alpha:]
[:alnum:]
[:upper:]
[:lower:]

# Examples
ls ?[[:digit:]]*
ls ?[4-6]
```
[Back to menu](#menu) |
[More information](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/x11655.htm)

---

## Install stuff

### Install from official repositories

```sh
sudo apt-get install almost_anything
```

### Install from package .deb

works the same way for an update

```sh
sudo dpkg -i package_name.deb
```

#### For resolving possibly corupted dependencies

```sh
sudo apt-get install -f
```
[source](https://unix.stackexchange.com/questions/159094/how-to-install-a-deb-file-by-dpkg-i-or-by-apt)

### Search for package

```sh
apt-cache search KEYWORD
```
[source](https://askubuntu.com/questions/160897/how-do-i-search-for-available-packages-from-the-command-line)

### Check if installed

```sh
dpkg-query -l 'someth*'
```
[Back to menu](#menu)

---

## Compression and decompression

(Uploading and downloading in ohter way is **damn** slow)

### Command zip

Zip files into new.zip

```sh
zip new file1 file2 file3
```

Unzip files from new.zip
```sh
unzip new.zip
# to NEW_DIR
unzip new.zip -d PATH/NEW_DIR
```

### Command tar

+ Compress files to new.tar.gz
```sh
# -c = create
# -v = verbose
# -z = gzip / gz / zip
# -f = following files

tar -cvzf new.tar.gz file1 file2 file3
```
+ Decompress from new.tar.gz
```
# -x = extract

tar -xvzf oldFile.tar.gz
```
+ Decompress from new.tar.bz2
```
# -j = bz2
# -C = where to extract

tar -xvjf oldFile.tar.bz2 -C /path/Directory
```
[Back to menu](#menu) |
[source](https://www.interserver.net/tips/kb/use-tar-command-linux-examples/) |
[source - bz2](https://linuxize.com/post/how-to-extract-unzip-tar-bz2-file/)

---

Advanced
===

## User management and priviledges

### TBD Bacis commands

```sh
groupmod
whoami
who
groups
```

### Add,delete  user | group

```sh
adduser USERNAME
deluser USERNAME
groupadd GROUPNAME
goupdel GROUPNAME
```

### Add user to group

```sh
usermod -a -G GROUP USER
```

### Group information

Read file containing information about groups.
Every line of the file has following structure:
GROUP_NAME:PASSWORD:GROUP_ID:GROUP_USER_1, GROUP_USER_2, GROUP_USER_3

```sh
less /etc/group
```

### Change password

```sh
[sudo] passwd [username]
```

### Switch user

```sh
su USERNAME
```

Every su opens a new shell.

```sh
# Show number of open shells
echo $SHLVL
```

### Superuser

Login as superuser, superuser's password required.
```sh
su
```
Login as superuser, current user's password required.
```sh
sudo su
```
grant to the command priviledges of superuser
```sh
sudo COMMAND
```

### User permissions

Everything has set permissions.

Exemple

```sh
ls -la
#drwxrwxrwx NUMBER USER USER NUMBER DATE NAME_OF_THE_FILE
```
The first 10 letters are the permissions, the structre follows
```
-        ---  ---   ---
filemode user group others
```
filetypes

+ d - directory 
+ l - link 	
+ b - bloc type (harddisc) 
+ c - chartype

### Change permissions

chmod u-x
	rename needs directory priviladges
	to read files directory needs r+x
	to rename files directory needs w+x
	--- 000	0
	--x 001 1
	-w- 010 2
	-wx 011 3
	r-- 100 4... 	chmod 755 text.txt chmod u=rw,g+rw ccc.txt

### Change ownership

```sh
chown USER[:GROUP] OBJECT
```
[Back to menu](#menu)

---

## Files - introduction

```sh
# Create new (empty) file
touch path/to/my/newFileName.anything

# Print sth to terminal
echo sth

# Take output of command and writes it to the file
command > file
echo text > fileExample

# Take output of command and writes it at the end of file
command >> file
echo next >> soubor

# Output every line from file
cat file

# Output every line from file in reverse order
tac file

# Output first 5 lines from file in reverse order
head file
# Output first n lines from file in reverse order
head -n 3 file

# Output last 5 lines from file in reverse order
tail file

# Sort output

# Example 
sudo du -a | sort -n -r | head -n 20
```
[Back to menu](#menu)

---

## Usefull commands - good to know

### Get basic info about command

```sh
# Where is the command from
which command_name

# One line information
whatis command_name
# Equivalent to
man -f command_name
```

### Show big files in a terminal

```sh
# Ouput stays into terminal after pressing q to quit
more
# File open in vim-like enviroment after pressing :q to quit the terminal is clean
less
```
[Back to menu](#menu)

### show terminal heigth and width

```sh
# show heigth
tput lines
# show width
tput cols
```

---

## Compare two files

### Command diff

```sh
diff --side-by-side --suppress-common-lines FILE_A FILE_B

diff --side-by-side --suppress-common-lines FILE_A FILE_B | more
```
or
```sh
diff -u file1 file2
```

file_2 as stdin

```sh
some_command | diff file_1 -
```

[Back to menu](#menu) |
[source1](https://community.spiceworks.com/topic/85704-how-can-i-make-diff-only-show-differences-between-two-files) |
[source2](https://www.computerhope.com/unix/udiff.htm)

### cmp

```sh
cmp file1 file2
```

---

## Practicals

+ [Copy from terminal to clipboard](#copy-from-terminal-to-clipboard)

### Open anything in terminal

Works like double-click
```sh
xdg-open ANY_NAME.ANYTHING
```

### Push process the backround

"I have opened something with terminal, now i see the process and can not use the terminal anymore"

Situation as described is the single most common example when is super nice to push the process to the background.

#### How to do it?

Press **Ctrl+Z**, then type
```sh
bg
```

the proccess will continue in background.

If you want to bring the process back to the foreground, type
```sh
fg
```
[source](https://superuser.com/questions/154486/how-to-run-programs-from-a-linux-terminal-without-blocking-the-terminal)

---

### Copy from terminal to clipboard

```sh
pwd | xclip -selection clipboard
```
[Source](https://askubuntu.com/questions/597788/copy-to-clipboard-current-path-from-console-with-no-mouse)

### See images in terminal

```sh
cacaview image.jpg
```
[Back to menu](#menu)

---

### Links

+ hard link
```sh
ln FILENAME LINKNAME
cp -l FILENAME LINKNAME
```
+ soft link
```
ln -s FILENAME LINKNAME
cp -s FILENAME LINKNAME
```

[Back to menu](#menu)

---

## SSH

```sh
ssh USER@99.888.777.22
```

### Copy files over ssh

scp [OPTION] [user@]SRC_HOST:]file1 [user@]DEST_HOST:]file2

```sh
scp -r compute  USER@78.128.250.10:/home/USER/computing/
```

[scp link](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)

### Screen

```sh
# Creat screen 
screen

# Detach from screen
screen -d

# Reattach to screen
screen -r

# List all screens
screen -ls

# Kill screen
screen -X -S SESSION_ID_FROM_LS kill
```

[screen link](https://linuxize.com/post/how-to-use-linux-screen/)
[kill screen](https://stackoverflow.com/questions/1509677/kill-detached-screen-session)

## SSHFS

### Mount local direcotry to remote directory

```sh
sshfs $USER@remote.example.com:/home/$USER/code ~/remote_code
```
### If user on local is different than the one logging with ssh

Uncomment user allow_other in /etc/fuse.conf

```/etc/fuse.conf
user_allow_other
```

```sh
sshfs -o allow_other user@myserver:/home/user/myprojects ~/mount/myprojects
```

### Unmount

```sh
fusermount -u ~/mount/myprojects
```


## Find process

```sh
ps aux | grep cat
```
[Back to menu](#menu)

### Kill process

```sh
# kill one specific precess id
kill -9 3827

# kill family of proceses
killall -9 chrome
```

[source](https://www.linux.com/training-tutorials/how-kill-process-command-line/)

---

## Enviroments and variables

Variables and functions, can be exported (global) or not.

### set

can be used to set various shell options, or the positional parameters. If no arguments or options are given, then it prints all shell variables and functions.

### Print value of variable

```sh
echo ${...}
```

### compgen -v

outputs only names of all shell variables, exported or not.

### GLOBAL: env, printenv ...

#### export

can be used to export variables or functions. With the -p option, it prints exported variables and functions

#### env

The env command can run other commands with modified environments. If no command is given, env prints environment variables (i.e., exported variables)

### printenv

prints environment variables

### LOCAL

    set | grep ''
    vara=123a

[source](https://askubuntu.com/questions/953579/what-is-the-difference-between-env-declare-and-compgen-v)

```sh
    CONSTS: $USER; $PATH; $SHLVL; $SHELL;

    variables:  name=value [[:alnum:]]
                unset ... (local)
                declare [-i; -r] ...
```
### Open new bash

```sh
bash
# See bash level
echo $SHLVL
# exit bash i.e. go to the previous enviroment
exit
```

```sh
    bash    child[sub]   interactive / uninteractiv - | read   
                exit
    startup
        login shell            
            /etc/profile
            $HOME/ [.profile; .bash_profile; .bash_login]
        non-login shell
            /etc/.bashrc
            $HOME/.bashrc
            source
```
[Back to menu](#menu)

---

## History

settings of history file 
```sh
~/.bashrc
```
Edit size of history command and history file
```sh
HISTSIZE=1000
HISTFILESIZE=10000
```
path to historyfile
```sh
echo $HISTFILE
```
how to stop logging ls command in history
```sh
echo 'export HISTIGNORE="ls:tree:cat:tail:head"' >> ~/.bashrc
```
run 111st command
```sh
history !111
```

press - ctrl+R - for searching of a commands from past

[Back to menu](#menu) |
[Source](https://www.rootusers.com/17-bash-history-command-examples-in-linux/)

---

## Regular Expressions

`“REGEX” or “REGEXP”?  ->  /REGEXP?/`
```sh
	. * [^- ] ^ $ 		- BRE
	+ ? { } ( ) | \		- ERE
BRE: 	grep - BRE
ERE: 	egrep 	grep -E 	grep \ERE 

grep -options 'RE' where
	[abc]
options: -n -c -i -v
	[: :]
		[:alpha:] 	[a-zA-Z]
		[:digit:] 	[0-9]
		[:lower:]	
		[:upper:]
		[:alnum:]
		[:word:]	[a-zA-Z_]
		[:blank:]	[mezera\t]
		[:xdigit]	[a-fA-F0-9]
	kvantifikatory:
		* + ? {}
		{min, max}
		? nemusi a kdyz tak pouze jednou
		+ musi minimalne jednou
		*

	Specialni znaky
		\b \< \> \w \W \s 	skoro_i \d
	RE1|RE2
	'<(h[1-6])>.*</\1>'
fgrep
rgrep
USAGE:
	less /
	locate --regexp [bre] --regex [ere]
    [Find anything](#find-anything)
```
[Back to menu](#menu)

---

## Vi basics

```sh
vi 		normal mode		hjkl	gg G 	w e b 	x X 	r 	J 	o O 	
						dd p P yy 7yy	. u CTR+r
		insert mode	 	i esc
		command mode	:	q	q!	:w 	:r 	:e :set tabstop=4
						:set nu!
						:set :split	:vsplit		ctrl+w+w
						:wqa!
		visual mode		v V ctrl+V
```
[Back to menu](#menu)

---

Linux
===

## Copy and past in terminal

### Copy from terminal

Highlight the text and press Ctrl+Shift+C

### Past to terminal

Press Ctrl+Shift+V

## Linux directory structure

+ /bin - executables
+ /home/* | /root - *users | roots personal data
+ /opt – Optional software (thigs you can't instal with package manager)
+ /etc - configuration files
+ /lib – Shared libraries

[Back to menu](#menu) |
[More information](https://linuxhandbook.com/linux-directory-structure/)

---

## Type special characters

Perhaps to write a dash, in linux there is a way to write unicode symbols.

1) press Ctrl+Shift+U
1) type the unicode code, perhaps 2014
1) press Space

voila —

---

Computers
===

## BOM

    byte order mark (BOM) is a particular usageof the special Unicode character, U+FEFF`

### UTF-8 bom

```sh
0xEF,0xBB,0xBF
```

### UTF-16 BOM

```sh
U+FEFF
```
[Back to menu](#menu) |
[Source](https://en.wikipedia.org/wiki/Byte_order_mark)

---

## Theory from seminars

### Theory from seminar 1

#### Types of commands

1) unkonwn
1) built in 	enable or compgen -b
1) executable	/bin 	/usr/bin
1) functions
1) aliases - concatenating more commands

enable
compgen -b

#### Create function
```sh
function pozdrav() { echo "ahoj"; }
```

#### Alias
```sh
alias neco='prikaz; prikaz'
unalias
```

#### Info about commands

1) help
1) man
1) info
1) apropos / man -k 

#### Move in terminal

+ alt B / F

#### Manipulation with text in terminal

+ alt U / l
+ alt t
+ ctrl t
+ kill ring CTRL K ctrl+y alt y


### Knowledge from seminar 3

```sh
locate -b -i -n 17 -S -u

VSTUP, VYSTUP, PRESMEROVANI
STDIN STDOUT STDERR
0<      1> >>   2>       
1> kamChci     2>&1
&> kamChci
PIPE    |   sort, uniq, less, head, 
    tail -f
    tee
file
```

### Knowledge from seminar 4


### Expansions

```sh 
# wild cards * ? ' ' $
mv old/* new/

# paths \ . ..
ls ..

# brace expansion {}
mkdir task_{a,b,c} # mkdir task_a task_b task_c
mkdir task{01..04} # mkdir task01 task02 task03 task04

# tilde expansion
ls ~/Documents # ls /home/$USER/Documents

# parameter and variable expansion
variable=10
echo ${variable} # echo 10

# command substitution
$(echo echo 2) # echo 2

# arithmetic expansion + - * / % ** ++ --
echo $((1238 % 17)) echo 14

# word splitting
# filename expansion
# quote removal
```

[Documentation](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html)

### Supressions

white space is suppresed.
- "double quotes" - suppress all except $ notation
- 'single quotes' - suppress everything

### calculator bc
echo "scale=2; 3/2" | bc

### Knowledge from seminar 5

```sh
/etc/shadow

setuid bit 		chmod 	u+s ... 4777
setgid bit 		chmod	g+s ...	2777
sticky bit 		chmod	+t ...	1777

umask	0224		d- 777	f- 666
```

### Knowledge from seminar 8

```sh
split - rozdeleni obsahu
    split -l 100 filename (rozdeli soubor podle definovaneho poctu radku)        
        split -n 3 filename (rozdeli soubor na zadany pocet souboru, proporcne podle velikosti)
        split -n 3 -d filename (zmeni abecedni suffix na numericky)
        split -n 3 -a 5 filename (zmeni delku suffixu, implicitne 2)
        split -n 3 filename prefix (zmeni implicitni prefix x na uzivatelem definovany)

cat - spojeni obsahu
    cat file_0* > merge

        cut - extrakce textu z radky
            cut -f 3 filename (implicitni oddelovac je TAB)
            cut -f 1,3 filename (vybrane sloupce)
            cut -f 2-3 filename (rozsah sloupcu)

            cut -d ':' -f 1 /etc/password | head (explicitni definice oddelovace)

            cut -c 2-10 (extrakce znaku na urcenych pozicich, jednotlive i rozsah)

        paste - spojeni sloupcu/radku
            paste file1 file2 file3 (implicitni oddelovac je TAB)
            paste -d ':' file1 file2 file3 (explicitni definice oddelovace)
            paste -s file1 file2 file3 (spoji obsahy jednotlivych souboru za sebou po radcich)

        sort - razeni
            sort file1 file2 file3 > file (serazeni a slouceni vice souboru)
                cut -d ':' -f 1 /etc/passwd | sort
            sort -r file (reverzni razeni)
            sort -n file (numericke razeni misto abecedniho)
                cut -d ':' -f 3 /etc/passwd | sort
                cut -d ':' -f 3 /etc/passwd | sort -n
            sort -k file (razeni podle k-teho sloupce ve vypisu, implicitni oddelovac je mezera a TAB)
                ls -l | sort -nr -k 5 (seradi numericky podle klice = od 5. sloupce v tabulce)
                sort --key=1,1 --key=2n filename (razeni podle vice klicu)
                sort -k 3.7nbr -k 3.1nbr -k 3.4nbr filename (offset v ramci sloupce)
                sort -t ':' -k 7 /etc/passwd (explicitni definice oddelovace)

transformace obsahu

tr - znakova transliterace (najdi a nahrad)
    prikaz ocekava dva argumenty: sadu znaku, ktere ma nahradit a sadu znaku, kterymi je ma nahradit
    sady znaku mohou byt vyjadreny tremi zpusoby
        - vycet znaku ABCDEFGH
            echo "mala pismenka" | tr abc 123
        - rozsah znaku A-H
            echo "mala pismenka" | tr a-z A-Z
            echo "mala pismenka" | tr a-z 1-3
        - pomoci POSIX znakovych trid
            echo "mala pismenka" | tr [:lower:] A
    sady znaku nemusi byt stejne dlouhe
        - echo "aaabbbccc" | tr a-b 1-3 (pokud je prvni sada kratsi, zbytek zustane bez zmeny)
        - echo "aaabbbccc" | tr a-c 1-2 (pokud je druha sada kratsi, zbytek se nahradi poslednim znakem nahrady)
    echo "aaabbbccc" | tr -s ab (smaze opakujici se instance uvedenych znaku, musi byt za sebou)
    echo "abcabcabc" | tr -s ab
    echo "aaabbbccc" | tr -d ab (smaze vybrane znaky)

sed - stream editor pro filtrovani a transformaci textu
    format: sed options 'script' file
    options - volby
        -n  potlaci autoprint radku
        -i  potlaci presmerovani na obrazovku a zmeny zapise do souboru
    addresses - adresy
        n           cislo radky
        addr1,addr2 rozsah radku
        first~step  prvni a kazdy dalsi po definovanem kroku
        $           posledni radka
        addr1,+n    zacatek a n nasledujicich radku
        addr!       vsechny ostatni radky krome definovanych (definovane mohou byt vsemi uvedenymi zpusoby)
        /regexp/    radka, ktera splnuje definovany BRE vyraz (delimiter je delimiter / nebo \cregexpc kde c je libovolny znak)
    commands - prikazy (singleline - jednoradkove)
        p   tisk vybraneho radku
            sed 'p' filename
            sed -n 'p' filename
        i   vlozi text pred aktualni radek
            sed 'i text' filename
        a   vlozi text za aktualni radek
            sed 'a text' filename
        d   vymaze aktualni radek
            sed 'd' filename
            sed '2~2d' filename
        =   zobrazi cislo aktualniho radku
            sed '=' filename
            sed '2,5=' filename
        c   zmeni text aktualniho radku
            sed '2c text' filename
            sed '2,5c text' filename
        r   cteni radku ze souboru
            sed 'r input1' input2
            sed '2,3r input1' input2
        w   zapis radku do souboru
            sed 'w input' output    (alternativa k cp)
            sed '2,3w input' output
        s/regexp/replacement/   substituce
             echo "pes" | sed 's/pes/kocka/'
            sed s/pes/kocka/ filename > newfilename            
            replacement
                muze obsahovat znak &, ktery vlozi text definovany regularnim vyrazem
                muze obsahovat back references \1 - \9
            flags
                prikazu s mohou nasledovat ruzne priznaky
                    echo "aaabbbccc" | sed 's/b/1/'   (nahradi pouze prvni vyskyt)
                    echo "aaabbbccc" | sed 's/b/1/g'  (nahradi globalne v celem radku)
                    echo "aaabBbccc" | sed 's/b/1/Ig' (nahradi globalne v celem radku a ignoruje velikost pismen)
        y/set1/set2/   transliterace
            echo "aaabbbccc" | sed 'y/abc/123/'
                 na rozdil od prikazu tr vyzaduje stejnou delku znakovych sad
                 nepodporuje rozsah (-) ani POSIX znakove tridy => vycet znaku musi byt presne definovan

ostatni
    vice prikazu najednou (oddeluji se strednikem ve slozenych zavorkach s option -e)
        sed -e '{s/pes/slon/; s/oves/zito/}' filename
        sed -e 's/pes/slon/; s/oves/zito/' filename
        sed 's/pes/slon/; s/oves/zito/' filename

    aplikace transformaci ulozenych v souboru (kazdy prikaz na samostatnem radku)
        sed -f script.sed filename
            script.sed
                s/pes/slon/
                s/oves/zito/
```

### Knowledge from seminar 9

```sh
sed i a =   p d n
            P D N
#   sed '/prvni/{N; s/\n/ /}' radky2
#   sed '=' radky2 | sed '/[1-9]/{N; s/\n/ /}'
#   sed '/^$/{N; /treti/D}' radky1

awk [-options]  '{program}' filenames
    -F :            print   $0, $1     "string"
    
        konsts:
            FS=":"              #input separator
            OFS="/"             #output separator
            FIELDWIDTHS="4 4" 
            NF=""               #Number of Fields
            FNR=                #File Number Row
            NR=                 #Number of Row
        BEGIN {} {} END {}
        array["a"]=7
        math:
            sin(); sqrt(); rand(); int()
        functions:
            lenght(); tolower(); toupper()
    operators:
            ~ !~ < > == !=
    regexps:
            ~ /RE/  
        do{}while()
        while(){}
        for(){}
```

### Knowledge from seminar 11 (24/04/2019)

```sh
shell
    max 255 znaků
    echo $0
    PATHS: /etc/shells
    chsh username
script
    exec. - $PATH / path/script 
    #!/bin/bash
    $0
    basename $0
    $1 - $9 ${10} - $#
    
    read -> $REPLY
    options:
        respons respons1 ...
        -n 3 
        -p "zadej cislo: "
        -t secs
        -s
        IFS = ':'
        X NEVER - echo "abc" | read
```

## Exit status

Every command in bash returns a status, number between 0 and 255, 0 menas success.

```sh
# Read the last exit status
echo $?
```

Bash script or terminal itself can return status code, command exit
```sh
# Success
exit # exit 0
# Failure
exit 1 # exit 255
```
```sh
	True; echo $? = 0
	False: echo $? = 1

	Testt -e soubor; echo $?
	[_ _] -f
		-d    #directory
		-L    #link symbolic
		-r    #readable by test
		-w    #permision to write
		-x    #executable
		-s    #not empty
		[ -s pokus]; echo $?
		[ f1 -nt f2 ]; echo $?
		-ot
		strings:
			-n
			-z
			==
			!=
			<
			>
	
		cisla:
			-eq
			-ne
			-lt
			-le
			-gt
			-ge
	[[_ _]]
		1)	x1
		2)	x1 == x2(d)
		3)	x1 =~ ERE
	((_ _))
		1)	$x1 .... x1 i pro stringy
		2)	== funguje pro cisla
		prirazeni:
			+=
			-=
			/=
			%=
			*=:
			++
			--
		ternary op conditional:
			(( a<1? (a=+2) : (a-=3) ))
	logicke operace
AND     -a 		&&
OR      -o 		!!
NOT     !		!

if commands; then commands

if [[ condition ]]; then
	commands
elif [[ condition ]]; then
	commands
else
	commands
fi

&& 
	- druhy proved pouze, pokud prvni exitstatus=0
||
	- pokud je prvni chybovy proved druhy
;
	- proved oba

date -r s1
stat
```

### Knowledge from seminar 12 (15/05/2019)

```sh
case variable in
    pattern)   commands;
        ;;
esac
    PATERN: letter)
            *)
            ?)  e.g.    ???.txt)
            [abc])  OR  [3-9])  OR  [[:digit:]])

select variable in[list] do
    commands;
done

LOOPS:

while commands; do
    commands;
done

until commands; do
    commands;
done

for  var [in list]; do
    commands;
done

LIST:   letters
        a" a b c d "
        $a
        /home/xxx/*
        {3..9}  OR  {3..9..3}
        array
        $@  # when missing [in list], uses argument from input
for ((i=0; i<10; i++))

while IFS=":" read a b c; do echo $a, $b, $c; done < /etc/group

break number    # breaks to the defined level 
continue number # implicit 1; starts next iteration of def. loop


Functions:

function name{
    commands;
}

name () {
    commands;
}

return # if not, then exit status of function is the es of last function

to return string:
        last line echo var
exec:   x=$(fu)

Variables:
[implicit (global) | local optional] variablename

VI
set tabstop=8 softtabstop=0 expandtab shiftwidth=4 smarttab
```

### Knowledge from seminar 13 (22/05/2019)

```sh
$# -> počet argmentů
$* -> přehled věšech argumentu
shift [n]

mkfifo

${var}
    :="value "
    :=
    :?
    :+

${var}
    :-value -> pokud v proměnné není nic, vypíše se value, ale nepřiřadí se
        aaa=
        echo ${aaa:-test} -> vypíše slov text

    :=value -> přiřadí i proměnnou(taková default)

    :? -> na prázdnost,vrátí -1, nebo zvolenou hlášku
    :+123 -> pokud není prázdná, dočasněji změn na 123

${!pattern -> vrátí podle vzoru všechny proměnné, které mu odpovídají
aaa=abc
echo ${!S*}
     
var/pattern/value -> nahraď pattern valuelem :P -> pouze pro 1. výskyt vzoru
var//pattern/value -> globální nahrazení v názvu
${var/pattern/value} # for change all matches //
aaa=abcdefghjiklmnopqrtuvwxyz
:offset echo ${aaa:4:6} -> usekne 4 znaky od začátku a pouze do 6
: -offset -> od konce ${aaa -6:3}
${#var}
#pattern ->vrátí podle vzoru 
##pattern ->požadavek na co nejdelší usek vrácení
%pattern    ->řeže to co vrátí patter
%%pattern   -> řeže to enjdelší    

numbers
    num     #r=10
    0num    #r=8
    0xnum   #r=16
    n#num   #r=n

bc 
    echo "obase=10; ibase=2; 1101" | bc
    
manipulators
    >   <   >>  
    <<< #here-string
    #<< OPENCLOSE  #here-document 
    OPENCLOSE

comments
    #<< _COMMENT_
    lalala
    _COMMENT_

    True '    ' OR :' '

screen
    ^a 
        c    #new bash window
        "    "#shows open windows 
        S   #devide horizontaly
        |   #devide verticaly
        TAB #change region
        A   #rename region
        k   #kill actual screen
        X   #close region
        Q   #close regions

top #command shows processes
```
