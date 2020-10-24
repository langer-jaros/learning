# Textovy editor vi.

## Menu
+ [Normal mode](#normal-mode)
+ [Insert mode](#insert-mode)
+ [Command mode](#command-mode)
+ [Visual mode](#visual-mode)
+ [vice souboru](#vice-souboru)

## Normal mode
        pohyb
            h j k l     kurzorove sipky
            gg          prvni radek
            G           posledni radek
            n G         n-ty radek
            w           zacatek dalsiho slova
            e           konec dalsiho slova
            b           zacatek predchoziho slova
            {           nasledujici odstavec (prazdny radek)
            }           predchozi odstavec (prazdny radek)

        editace
            x           vyjme znak na kurzoru (3x aktualni + 2 dalsi)
            X           vyjme znak pred kurzorem (BACKSPACE)
            r [char]    nahradi znak na kurzoru
            J           odstrani konec radku na kurzoru (spoji radky)
            a           spusti editaci na aktualni pozici kurzoru (jako i)
            A           spusti editaci na konci aktualniho radku
            o           otevre novy radek pod aktualnim
            O           otevre novy radek pred aktualnim

        vyjmuti
            dd          aktualni radek (5dd aktualni + 4 dalsi)
            dw          znaky od kurzoru do konce slova
            d$          znaky od kurzoru do konce radky
            d^          znaky od kurzoru do zacatku radky

        kopirovani
            yy          aktualni radek (5yy aktualni + 4 dalsi)
            yw
            y$
            y^

        vlozeni
            p           vlozi data z buffer za aktualni radek
            P           vlozi data z buffer pred aktualni radek

        obecne
            .           opakuje posledni prikaz
            u           undo
            Ctrl+r      redo

        hledani
            f [char]    vyhleda zadany znak na aktualnim radku v oblasti za kurzorem
            F [char]    vyhleda zadany znak na aktualnim radku v oblasti pred kurzorem
            t [char]    vyhleda a skoci pred zadany znak na aktualnim radku v oblasti za kurzorem
            T [char]    vyhleda a skoci za zadany znak na aktualnim radku v oblasti pred kurzorem
                ;   najde dalsi vyskyt znaku
                ,   najde dalsi vyskyt znaku v opacnem smeru

            / [pattern] vyhleda vzor v oblasti za kurzorem
            ? [pattern] vyhleda vzor v oblasti pred kurzorem
                n   najde dalsi vyskyt vzoru
                N   najde dalsi vyskyt vzoru v opacnem smeru

## Insert mode
        - po stisku klavesy i v normalnim modu
        - umoznuje pouze zakladni editaci
        - ukonci se ESC

## Command mode
        - po stisku klavesy :

        :q                  ukonci
        :q!                 ukonci bez kontroly ulozeni
        :w                  zapis zmeny do existujiciho souboru
        :w filename         uloz soubor
        :r filename         otevri soubor
        :e filename         otevri novy soubor
        :wq                 zapis a ukonci
        :qa                 ukonci vsechny soubory

        :s                  substituce (v zakladu stejna syntaxe jako sed)
        :%s/Line/line/g     rozsah celeho souboru
        :%s/Line/line/gc    potvrzeni nahrady (y - ano, n - ne, a - ano a vsechny nasledujici, q - ukonci, l - ano a ukonci)

        :set tabstop=4      nastavi pocet mezer tabulatoru
        :set nu!            zapne/vypne cisla radku

        :split              rozdeli okno horizontalne
        :vsplit             rozdeli okno vertikalne

## Visual mode
        v                   volny vyber oblasti
        V                   radkovy vyber oblasti
        Ctrl+v              blokovy vyber oblasti

        - na vybranou oblast lze aplikovat prikazy d y c
        - prikaz c smaze vybranou oblast a prejde do INSERT MODE
        - ukonci se ESC ESC

## vice souboru
        vi -o file1 file2       otevre soubory v horizontalne rozdelenem okne
        vi -O file1 file2       otevre soubory ve vertikalne rozdelenem okne

        Ctrl + w + w            prepnuti mezi okny
        Ctrl + w + [hjkl]       prepnuti do sousedniho okna v danem smeru

