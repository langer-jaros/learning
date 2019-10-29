<?php
/*
spl_autoload_register(function ($className){
    #require __DIR__.'/classes/'.$className.'.php';
    include_once __DIR__.'/classes/'.$className.'.php'; 
});
*/
/*/
spl_autoload_register(function($className) {
    require  __DIR__ . '/classes/' . str_replace('\\', '/', $className).'.php';
});
/*/
/*/
function fu1(&$b)
{
	$b[0]=99;
}

function fu(&$a)
{
	$b = &$a;
	fu1($b);
}


$arr = array(1,2,3);

fu($arr);

var_dump($arr);
$tree1 = (new Node(1))
->setLeft((new Node(2))
->setLeft(new Node(4))
->setRight(new Node(5))
)
->setRight(new Node(3));

//var_dump($tree1);

$tree2 = $tree1;
$tree2->setLeft(null);
$tree2->setRight(null);
/*/

//var_dump($tree1);


$arr = array();
array_push($arr, "a");

array_push($arr, "b");

echo array_pop($arr) . "\n";
array_push($arr, "c");
echo array_pop($arr) . "\n";
echo array_pop($arr) . "\n";
/*/
$stack->push("a");
$stack->push("b");
$stack->push("c", "d");
$stack->push(...["e", "f"]);


/*/