#!/bin/bash
#Jaroslav Langer
#01/05/2019

read -p "Zadejte desetinne cislo: "
echo ''
line=$(egrep $2 $1)

echo "struktura = $2"
# kod struktury beze změny

nazev=$(echo $line | cut -d ':' -f 2)
echo "nazev = $nazev"
# název beze změny

roz=$(echo $line | cut -d ':' -f 3)
echo $REPLY | awk -v var="$roz" '{print "rozliseni = ",var,"+",$1,"=",var+$1}'
 # původní hodnota a hodnota zvětšená o uživatelem vložené číslo

autori=$(echo $line | cut -d ':' -f 4)
echo $autori | awk '{print "autori =",toupper($0)}'
# jména autorů velkými písmeny

rok=$(echo $line | cut -d ':' -f 5)
echo $rok | sed 's/\([[:alnum:]]\{4\}\).*/rok = \1/'
# z celého datumu pouze rok
