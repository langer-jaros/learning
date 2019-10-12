<?php

# Printing #
// For text and simple datatypes
echo "hello php";
// For more complex datatypes 
var_dump($variable);
// Another way
print_r($variable);
// Concatenating string
echo '$var '.$var."\n";


# Comments #
// Single line
# 
// OR 
//
// Multi-line
/*
comment
*/
// OR
$doc = <<<SAMEPHRASE
Author: Jaroslav Langer
Date: 12/10/2019
Decsription: Homework-01 from BI-PHP.1
(Regex, sorting, sumation)
SAMEPHRASE;


# Data types recognition #
is_numeric($x)? "numeric\n" : "";
is_float($x)? "float\n" : "";
is_bool($x)? "bool\n" : "";
is_array($x)? "array\n" : "";
is_string($x)? "string\n" : "";
is_integer($x)? "numeric\n" : "";
is_object($x)? "numeric\n" : "";


# Arrays #
// Creation with brackets
$letters = [1,2,3,4,5];
// Creation with keyword
$aa = array(12,343,523,235,235,45);
// Addition at new available index
$a['a'][]= 10;
// Index -1 isn't the last, makes ERROR
echo $aa[-1]."\n";
// Create array from string
$list = explode("\n", $input);


# Conditions #
// Ternary operator
$var = is_numeric($x)? "numeric\n" : "";


# Loops #
// Foreach
foreach ($array as $key => $value) {
    echo $array[$key] == $value;
}
// Doesn't work with string
foreach ($string as $letter) {
    echo "Next letter is: ".$lettter."\n";
};
