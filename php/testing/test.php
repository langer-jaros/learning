<?php

spl_autoload_register(function ($className){
    require __DIR__.'/classes/'.$className.'.php';
});

function p ($s1, $s2) {
    echo $s1.": ";
    var_dump($s2);
    echo "\n";
}
