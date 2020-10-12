# Umělá inteligence

## Obsah

- [Přednáška 1](#přednáška-1)
- [Přednáška 2](#přednáška-2)
- [Přednáška 3](#přednáška-3)

Nahrát na gitlab, přidat cvičícího jako pozorovatele.
(Můžu odevzdat klidně ještě vysavač)
[results](https://users.fit.cvut.cz/surynpav/teaching/restricted_2020-2021-ZS/results.php)

## Přednáška 1

## Definice ai

Pokus nejen o porozumění ale i o sestrojení umělé inteligence.

## Rozdělení

Uvnitř: myslet jako člověk | myslet racionálně
Venku: jednat jako člověk | jednat racionálně

## Nebude strojové učení

- nebudou neuronové sítě, SVM, rozhodovací stromy

## Předhistorie

- Filosofie
- Matematika
- Ekonomie
- Neurovědy
- Počítačové inženýrství
- Teorie řízení a kybernetika
- Lingvistika

## Historie ai

- Formování (1943)
    + Turing, von Neuman
- Zrození (1956)
    + Logic theorist - Newell Simon
- Nadšení
- Vystřízlivění
- počítač 5. generace 
    + (JP) logické programování, Prolog
- Rozmach (1990-...)

## Touringův test

## 

- řešení úloh prohledáváním
- splňování omezujících podmínek
- splnitelnost
- automatické plánování
- modelování úloh
- zpracování přirozeného jazyka
- robotika

## ai jako tvorba

Vytváření počítačových artefaktů

## Typy artefaktů

- pasivní - nevykazuje aktivitu (mapa)
    + skvěle se testují, vychází z lokálních vlastností
- aktivní - vykazuje aktivitu (hrací agent)
    + obtížné testovat správnost

## Úrovně artefaktů

0.  - aktivní - člověk hraje za stroj
    - pasivní - člověk si vytvoří sám
1.  - aktivní - člověk napíše program co hraje šachy
    - pasivní - člověk napíše program co něco spočítá
2.  - člověk vytvořil robota, ten vytváří kód
3.  - robot už vytvořil robota, který píše kód 

## Řešení úloh - tvorba pasivních artefaktů

- Formulace cíle
- formulace úlohy
- řešení úlohy
- provedení úlohy

## Formulace úlohy

- situace (agent je v Rumunsku, má si užít dovolenou)
- zjednodušení (jet do bukurešti)

## Hračkové příklady

- vysavač
- 8 dam

## Reálné příklady

- Amazon roboti

## Neinformované prohledávání

- prohledávání do hloubky
- prohledávání do šířky
- iterované prohledávání do hloubky
- prohledávání heuristicky (A*)
- RBFS

## Závěrečné poznámky

- pozor na opakovatelné stavy
- prohledávání s využitím externí paměti
    + organizace těchto dat
- heuristika musí být monotóní a jednoznačná?
- obousměrné prohledávání

## Přednáška 2

## Constrains satisfaction problem - CSP - Splňování omezení

Tvorba pasivních artefaktů.

(X, D, C)
- X - konečná množina proměnných - vlastnosti rozhodující o řešení
- D - konečná doména (možnosti)
- C - množina podmínek nad X 
    + relací - podmnožina kartézského součinu domény

Konjunkce všech podmínek

### Definice

- Stav S' - částečné ohodnocení proměných
- Konzistentní stav - všchny podmínky splněny
- počáteční stav - prázdné ohodnocení proměných
- akce - 
- cílový stav - všechny proměnné ohodnoceny

## Chronologický backtracking

- DFS v kontextu CSP
    + dopředný chod - přiřazují se proměnné
    + zpětný chod - odpřiřadí se poslední proměnná a zkouší se znovu
- složitost velikost domény na počet proměnných

## Filtrace domén

### Forward checking

- při akci zkontroluji pro všechny dotčené podmínky dotčené proměnné a vyškrtneme z pracovní domény proměné (nesplňující ohodnocení)
- kontrola podpory, kontrola jestli hodnota dotčené proměnné neztratila podporu

## Arc consistency - Hranová konzistence

- Kontrolujeme hranu z X1 do X2
(pro každou proměnou v pracovní doméně hledáme podporu, taková D2, že s D1 splňují podmínku)
- dvě proměné jsou 
- cíl celý problém má být hranově konzistentní
- všechny hrany musejí být oboustranně konzistentní (všchny hodnoty jedné proměnné mají podporu a opačně)
    + kontrola zasažených hran

### algoritmus AC3 

- pro frontu hran, hledá podporu

## Heuristiky

### Výběr nejvíce omezené proměnné v algoritmu 

- ohodnocujeme doménu, která má nejméně hodnot

### Výběr klíčové proměnné

### Hodnoty vybíráme tak, abychom co nejdříve narazili na řešení

## Využítí struktury

### Výběrem proměnných rozložit na komponenty

## Složitost CSP

NP úplný problém

## Optimalizace CSP

branch and bound nad celou arc consistency, ...

## Spojité CSP

CSP s rozvrhováním - výrobní linky atd

## Programování s omezeními

## CSP, A*, Simulované žíhání

- Simulované žíhání - lokální, dobrý, na problémy co nejdou řešit systematicky
- A* - vymyslet heuristiku pro NP problém je problematické
- CSP - jak šité na barvení mapy

## Přednáška 3

## Back jumping
- spočítám konfliktní množinu
- listové řešení
- nelistové řešení

## TODO

bi-zum
bi-ag2 (a*)
lineární programování