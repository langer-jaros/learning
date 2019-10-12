<?php

# Arguments
// Passing like a reference
function swap(&$a, &$b){
    $b = $b + $a;
    $a = $b - $a;
    $b = $b - $a; 
}

# Built-in functions
// Random number function
$num = rand(10,99);

# REGEX
// Match case 
$subject = "abcdef";
$pattern = '/def/';
preg_match($pattern, $subject, $matches);
print_r($matches); // [ "def" ]

// Splitting
$string = "1+2-3";
$array = preg_split('/[+-]/', $string);
print_r($array);    // [1, 2, 3]
