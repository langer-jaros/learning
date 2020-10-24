# PHP

```11/10/2019, Jaroslav Langer```

## Základy

- skriptovací, interpretovaný (facebook to nějak umí)
- php = ~personal homepages~
- dynamicky typovaný
- možná práce s lokálním systémem
- možné #! cestu k interpretru a pouštět v shellu

## syntax

\<?php a ?>

- otevírací značka, aby se oddělil od html
    - nedoporučuje se mít v jednom souboru
- nedoporučuje se používat uzavírací značku

příkazy se oddělují středníkem
bloky se uzavírají { }

### Comments

//  |  /* */  |  /** * */

## Proměnné

+ začínají dolarem
+ jsou case sensitivní
+ doporučená je malá camelNotace
+ nesmí začínat číslem
+ inicializace probíhá hodnotou

### možnost pojmenovat proměnou pomocí proměnné i u funkcí

>$promenna = prom
$$promenna = prom2

### Viditelnost proměnných

Proměnné jsou viditelné v bloku kde je a níž

## Reference

&$b = $a

## Konstanty

keyword const
existuji magicke konstanty

### Statické proměnné

drží sí místo v paměti, například pro proměnné ve funci

### Superglobální pole

$_GET $_POST $_COOKIE uspořádané v poli $_REQUEST

**!!! Potenciálně nebezpečné**

## Funkce pro práci s proměnnými

+ isset($prom)
+ empty
+ is_numeric
+ is_{bool, inteege, float, string, ...}

+ unset() - u pole je možné smazat index z pole
 - možnost uvolnit pamět 

get_class, instaceof

## Datové typy

+ jednoduché
+ složené

## řetězce

### Practies

## Užitečné

 printr
 clone
 - když je 

 !!! Linux days

# TODO PHP

+ General/Namespaces 

+ https://stackoverflow.com/questions/45965699/mocks-vs-stubs-in-phpunit
+ https://www.geeksforgeeks.org/php-gettype-function/

---