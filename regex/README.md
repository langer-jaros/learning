# Regular expresions

## MENU

+ [Integer](#integer)
+ [Float](#float)

## Regex Or |

every thing from | to closest bracets, left and right

```
/onePattern|secondPattern/
```
is equivalent to
```
/(onePattern|secondPattern)/
```
not equivalent to this
```
/(one)(Pattern|second)(Pattern)/
```



---
## Integer
### anywhere on the line
```
$pattern = '/[[:digit:]]+/';
```
### Tousand dot every third position from end
```
$integer = '/[[:digit:]]{1,3}(\.[[:digit:]]{3})*/';
```
### Tousand - dot every third position from end, ,-
```
$pattern = '/[[:digit:]]{1,3}(\.[[:digit:]]{3})*(\ )*,-/';
```
---
## Float
### Tousand dot every third position from end with comma
```
$float = '/([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?/';
```
### Tousand dot every third position from end with comma and Kč
```
$pattern = '/([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?(\ )*Kč/';
```
### Tousand dot every third position from end with comma and CZK
```
$pattern = '/([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?(\ )*CZK/';
```
### CZK and tousand dot every third position from end with comma
```
$pattern = '/CZK(\ )*([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?/';
```
### CZK at start or end and tousand dot every third position from end with comma
```
$pattern = '/(([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?(\ )*CZK|CZK(\ )*([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?)/';
```
---
```10/11/2019, Jaroslav Langer```

