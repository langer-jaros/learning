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


# Read Input #
$input = file_get_contents($argv[1]);
/* The $argv is array of arguments.
The zero argument is the file itself.
You can use it as any array such with end() etc */
$input = file_get_contents(end($argv));
// import code once - error will stop the code.
require_once './the/path/you/desire.php';
// import code once - only warrning will be shown if error.
include_once './the/path/you/desire.php';
// Or you can include | require all over again
require '.something.php';
include '.something.php';

# Variables
$startsWithDollar;
// Constatns doesn't
const CONSTANT = 'const_value';
// Determin, whether the variable exits.
$array['1']='one';
// compare with null, in this case return false;
var_dump(isset($array['1']['2']['3']));

# Data types recognition #
is_numeric($x)? "numeric\n" : "";
is_float($x)? "float\n" : "";
is_bool($x)? "bool\n" : "";
is_array($x)? "array\n" : "";
is_string($x)? "string\n" : "";
is_integer($x)? "numeric\n" : "";
is_object($x)? "numeric\n" : "";

# String
// Replace substring (delete spaces)
$myString = str_replace ( ' ', '', $myString);
// Deletion of last character
$string = substr_replace($string ,"", -1);

# Arrays #
// Creation with brackets
$letters = [1,2,3,4,5];
// Creation with keyword
$aa = array(12,343,523,235,235,45);
// Addition at next index of array
$array[]= $nextElement;
// Much faster than
array_push($array, $nextElement);
// Index -1 isn't the last, makes ERROR
echo $aa[-1]."\n";
// Create array from string
$list = explode("\n", $input);
// and string from array
$string = implode("\n",$value);
// Sort the array by the keys
$array = ksort($array, sorttype);
// Determin, whether an array contain the key
var_dump( array_key_exists($array_key, $array_name) );
// Sum all values of the $array
$sum = array_sum($array);

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


# Time tracking #
$start = microtime(true);
// Any code here ...
$time_elapsed_secs = microtime(true) - $start;
echo "Any code took: $time_elapsed_secs s\n";

# Asserts
// Needs to set zend.assertions = 1 at php.ini file
// you can find it via php -ini
// i had it there   /etc/php/7.2/cli/php.ini
assert($a === 1, '$a is not 1');
