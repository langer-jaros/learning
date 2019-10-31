# General goods for PHP

## Namespaces 
//TODO

## Autoloading

### Without namespaces

When you write something like:
```$obj = new Class1();```
You needed to require or include the Class1 in a way like:
```require_once './path/you/desire/Class1.php';```

Much nicer way is to use this block of code:
```
spl_autoload_register(function ($className){
    require __DIR__.'/path/you/desire/'.$className.'.php';
});
```
Which once it reaches Class1 will search for ./path/you/desire/Class1.php

### With namespaces

With namespaces, the interpret will reach something like:
```$obj = new Namespace1\Namespace2\Class1();```

Because in UNIX like systems is for directory used separator '/'
You only need to replace the backslashes from namespace with slashes and it will work fine again.
```
spl_autoload_register(function($className) {
    require __DIR__.'/path/you/desire/'.str_replace('\\', '/', $className).'.php';
});
```
