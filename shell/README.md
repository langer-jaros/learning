# Shell 
##### The art of using PC like human being
```Using linux mint 19```

## MENU

+ [Open anything in terminal](#open-anything-in-terminal)
+ [Copy from terminal to clipboard](#copy-from-terminal-to-clipboard)
+ [Install stuff](#install-stuff)
+ [Compression and decompression](#Compression-and-decompression)
+ [Compare two files](#compare-two-files)
+ [Find](#find)
+ [Change password](#change-password)
+ [Regular Expressions](#regular-expressions)
+ [Knowledge from seminars](#seminar-1)
---
## Open anything in terminal
(double-click like)
### Command xdg
```
xdg-open ANY_NAME.ANYTHING
```
### Push it to the backround in shell
#### press ctrl+z, then type:
```
bg
```
the proccess will continue in background.
#### If you want to bring the process back to the foreground. Press:
```
fg
```
[source](https://superuser.com/questions/154486/how-to-run-programs-from-a-linux-terminal-without-blocking-the-terminal)

---
## Copy from terminal to clipboard
```
pwd | xclip -selection clipboard
```
[source](https://askubuntu.com/questions/597788/copy-to-clipboard-current-path-from-console-with-no-mouse)

---
## Install stuff
### Install from official repositories
```
sudo apt-get install almost_anything
```
### Install from package .deb
```
sudo dpkg -i package_name.deb
```
#### For resolving possibly corupted dependencies
```
sudo apt-get install -f
```
[source](https://unix.stackexchange.com/questions/159094/how-to-install-a-deb-file-by-dpkg-i-or-by-apt)

### Search for package
```
apt-cache search KEYWORD
```
[source](https://askubuntu.com/questions/160897/how-do-i-search-for-available-packages-from-the-command-line)

---
## Compression and decompression
(Uploading and downloading in ohter way is **damn** slow)

### Command zip
Zip files into new.zip
```
zip new file1 file2 file3
```
Unzip files from new.zip
```
unzip new.zip
```

### Command tar
+ Compress files to new.tar.gz
```
tar -cvzf new.tar.gz file1 file2 file3
```
+ Decompress from new.tar.gz
```
tar -xvzf new.tar.gz
```
[source](https://www.interserver.net/tips/kb/use-tar-command-linux-examples/)
---
## Compare two files
### Command diff
```
diff --side-by-side --suppress-common-lines FILE_A FILE_B
```
or
```
diff -u file1 file2
```
[source1](https://community.spiceworks.com/topic/85704-how-can-i-make-diff-only-show-differences-between-two-files)
[source2](https://www.computerhope.com/unix/udiff.htm)

---
## Seminar 1
```
147.251.253.55
CLI
	prompt + kurzor PS1 prompt vice radkovej v PS2
$ norm usr -x- # super user

Typy prikazu
	unkonwn
	built in 	enable or compgen -b
	executable	/bin 	/usr/bin
	funkce
	alias seskupovani vice prikazu

command [-options] [args]
options single letter -x  full text --xxxxxxx

enable
compgen -b

function pozdrav() { echo "ahoj"; }
alias neco='prikaz; prikaz'
unalias

help man info apropos / man -k 

which whatis / man -f

history !111 !!
ctrl R

MOVE
    alt B / F
    
MANIPULATION
    alt U / l
    alt t
    ctrl t
    kill ring CTRL K ctrl+y alt y
```
## Seminar 2
```
pwd tree    cd  ~jmeno
touch   
echo text > soubor
echo next >> soubor
mkdir
cp -r
mv -i
rm -r

Linky
    hard link   ln      cp -l
    soft link   ln -s   cp -s
cacaview
cat     tac
head -n 3 soubor
tail

more
less

WILDCARDS 
    *
    ?
    [! ]
            [^ ]
    ls ?[[:digit:]]*        [:digit:] [:alpha:] [:alnum:] [:upper:] [:lower:]
    ls ?[4-6]       [a-dsu]     [3-7a-g]
```
## Seminar 3
```
locate -b -i -n 17 -S -u
```
## Find
```
find /  -name "toBeFound"       ACTIONS -delete
        -type f d l                     -ls 
        -user                           -exec ls -l {} \;
        -size   +-nc k M G              -ok
        -empty
        -mindepth -maxdepth n
```
```
VSTUP, VYSTUP, PRESMEROVANI
STDIN STDOUT STDERR
0<      1> >>   2>       
1> kamChci     2>&1
&> kamChci
PIPE    |   sort, uniq, less, head, 
    tail -f
    wc -l
    tee
file
```
## Seminar 4
```
Expanse
	* ? ' ' \ . .. $
- space suppression " " - suppress all except $ notation
					 \
					 ' ' - suppress everything
- paths 		
- tilde			~
- arithmetic	$(( )) + - * / % ** ++ -- $[ ] -depracated
expr
bc	scale=2				echo "(((11+45)/2)%3)" | bc -l
						echo "scale=2; 3/2" | bc
- brace 		{} 		mkdir ukol{a,b,c} mkdir ukol{01..06}
- parameter 	$x ${x}
env
- command 		$() 	`which cp`

USER PERMISSIONS
	- rwx rwx rwx
	^filetype	d - directory 
				l - link 	
				b - bloc type (harddisc) 
				c - chartype
	  --- --- --- } filemode user group others
chmod u-x
	rename needs directory priviladges
	to read files directory needs r+x
	to rename files directory needs w+x
	--- 000	0
	--x 001 1
	-w- 010 2
	-wx 011 3
	r-- 100 4... 	chmod 755 text.txt chmod u=rw,g+rw ccc.txt
	
```
## Seminar 5
```
chown user[:group] objekt

find	-perm 	400 	u=rw 	-u=rmw 	/u=r,o=x
		-user 	langera
		-group
/etc/shadow
ps aux | grep cat
	
setuid bit 		chmod 	u+s ... 4777
setgid bit 		chmod	g+s ...	2777
sticky bit 		chmod	+t ...	1777

umask	0224		d- 777	f- 666

adduser
deluser
```
### Change password
```
[sudo] passwd [username]
```
```
groupadd
goupdel
groupmod

whoami
who
groups

sudo		sudo su langera
su ...		

vi 		normal mode		hjkl	gg G 	w e b 	x X 	r 	J 	o O 	
						dd p P yy 7yy	. u CTR+r
		insert mode	 	i esc
		command mode	:	q	q!	:w 	:r 	:e :set tabstop=4
						:set nu!
						:set :split	:vsplit		ctrl+w+w
						:wqa!
		visual mode		v V ctrl+V
```

## Regular Expressions
`“REGEX” or “REGEXP”?  ->  /REGEXP?/`
```
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
	find -regex 
	locate --regexp [bre] --regex [ere]
```
## Seminar 8
```
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
## Seminar 9
```
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
## Seminar 11 (24/04/2019)
```
ENVIROMENT
    GLOBAL: env, printenv ...
            echo ${...}
                    
    LOCAL:  set | grep ''
            vara=123a
            export ...
    CONSTS: $USER; $PATH; $SHLVL; $SHELL;

    variables:  name=value [[:alnum:]]
                unset ... (local)
                declare [-i; -r] ...

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



EXIT STATUS TEST
	0 - 255
	$?

	Ls neexistujici
	Echo $? = 2

	Exit
	Exit n
	

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
## Seminar 12 (15/05/2019)
```
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
## Seminar 13 (22/05/2019)
```
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
---
```10/11/2019, Jaroslav Langer```