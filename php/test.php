<?php

function match ($list, $pattern){
    foreach ($list as $subject) {
        preg_match($pattern, $subject, $matches);
        echo $value = ($matches)? $matches[0]."\n" : '' ;
        //print_r([0]?: "");
        $a[]=$matches;
    }
return $a;
}

$input = file_get_contents($argv[1]);
echo $input;
echo "\n------------input end ------------\n";
$list = explode("\n", $input);

$integers = '[[:digit:]]{1,3}(\.[[:digit:]]{3})*';
$floats = $integers.'(,[[:digit:]]*)?';

$price = '/'.$integers.'(\ )*,-/';
$kc = '/'.$floats.'(\ )*Kč/';
$czk = '/(CZK(\ )*'.$floats.')|('.$floats.'(\ )*CZK)/';

// $pattern = $price;
//$pattern = $kc;
$pattern = $czk;
$out = match($list, $pattern);
// var_dump($out);
//var_dump(sizeof($out));
/*/
foreach ($list as $subject){
    echo $subject."\n";
}
/*/

