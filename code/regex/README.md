# Regular expresions

## Content <!-- omit in toc -->

- [Regex Or |](#regex-or-)
- [Integer](#integer)
  - [anywhere on the line](#anywhere-on-the-line)
  - [Tousand dot every third position from end](#tousand-dot-every-third-position-from-end)
  - [Tousand - dot every third position from end, ,-](#tousand---dot-every-third-position-from-end--)
- [Float](#float)
  - [Tousand dot every third position from end with comma](#tousand-dot-every-third-position-from-end-with-comma)
  - [Tousand dot every third position from end with comma and Kč](#tousand-dot-every-third-position-from-end-with-comma-and-kč)
  - [Tousand dot every third position from end with comma and CZK](#tousand-dot-every-third-position-from-end-with-comma-and-czk)
  - [CZK and tousand dot every third position from end with comma](#czk-and-tousand-dot-every-third-position-from-end-with-comma)
  - [CZK at start or end and tousand dot every third position from end with comma](#czk-at-start-or-end-and-tousand-dot-every-third-position-from-end-with-comma)

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

[Alternation (regular-expressions info)](https://www.regular-expressions.info/alternation.html)

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

```2020/10/29, Jaroslav Langer```
