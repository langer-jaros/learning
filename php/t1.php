<?php
$input = file_get_contents($argv[1]);
// var_dump($input);

$list = explode("\n", $input);
$start = microtime(true);

/*/
for ($i=0; $i < 1000000; $i++) { 
    $a = array();
    foreach ($list as $value) {
        array_push($a, $value);
    }
}
$time_elapsed_secs = microtime(true) - $start;
echo "push: $time_elapsed_secs s\n";

/*/
for ($i=0; $i < 1; $i++) { 
    foreach ($list as $value) {
        $a[]=$value;
    }
}
$time_elapsed_secs = microtime(true) - $start;
echo "[]= $time_elapsed_secs s\n";
//var_dump($a);

$s = 'Herní konzole 4.900 CZK';


str_replace ( $searchVal, $replaceVal, $subjectVal, $count );