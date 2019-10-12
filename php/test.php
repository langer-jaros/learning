<?php

$input =<<< INPUT
Rohlík 5Kč
CZK400 Knížka
Pivo 42,-
Houska 4 Kč
Máslo 49,00 Kč
Herní konzole 4.900 CZK
Rádio CZK550
CZK 1.600,59 Natural 95
INPUT;

// Kč
$s1 = "Rohlík 5Kč";
$s2 = "Houska 4 Kč";
// ,- cele cislo bez haleru
$s3 = "Pivo 42,-";
$s4 = "Pivo 42,-";
// CZK
$s5 = "CZK400 Knížka";
$s6 = "Herní konzole 4.900 CZK";
$s7 = "Rádio CZK550";
$s8 = "CZK 1.600,59 Natural 95";

function match ($list, $pattern){
    foreach ($list as $subject) {
        preg_match($pattern, $subject, $matches);
        print_r($matches?: "");
    }
}
/*/
$subject = $s1;
preg_match($pattern, $subject, $matches);
/*/
$pattern = '/[[:digit:]\,\.]+\ *(Kč|\,\-)/';
$list = explode("\n", $input);
match($list, $pattern);
