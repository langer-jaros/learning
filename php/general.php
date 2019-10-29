<?php

# Autoloading
// Tries to find 
spl_autoload_register(function ($className){
    require __DIR__.'/folderPath/'.$className.'.php';
});

$obj = new Namespace1\Class1();
