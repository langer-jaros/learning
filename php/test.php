<?php
/*
$a = 
var_dump($a);

$a['a'][]= 10
*/
// TELL TYPE
function tell_type($x){
    echo is_numeric($x)? "numeric\n" : "";
    echo is_float($x)? "float\n" : "";
    echo is_bool($x)? "bool\n" : "";
    echo is_array($x)? "array\n" : "";
    echo is_string($x)? "string\n" : "";
    echo is_integer($x)? "numeric\n" : "";
    echo is_object($x)? "numeric\n" : "";
}


$i = "10"; $s = 8; $t = '1e1';

tell_type($i);
tell_type($s);
tell_type($t);


$aa = array(12,343,523,235,235,45);
var_dump($aa);

echo $aa[-1]."\n";

/* FUNCTION SWAP
function swap(&$a, &$b){
    $b = $b + $a;
    $a = $b - $a;
    $b = $b - $a; 
}
$a = 5; $b = 10;
var_dump($a);
var_dump($b);
swap($a, $b);
var_dump($a);
var_dump($b);
*/
