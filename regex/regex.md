# Regular expresions
Jaroslav Langer
17/10/2019

##
# Atempts
//1 $pattern = '/[[:digit:]\,\.]+\ *(Kč|\,\-)/';
//2 $pattern = '/[[:digit:]\.]+(,)\ *(Kč|\,\-)/';
//3 $pattern ='/[[:digit:]]+((\.|,)[[:digit:]])?/';

//$pattern = '/[[:digit:]\.](,|\ )? *(Kč|\,\-)/';

// Number anywhere on the line
$pattern = '/[[:digit:]]+/';

// Tousand dot every third position from end
$pattern = '/[[:digit:]]{1,3}(\.[[:digit:]]{3})*/';

// Tousand - dot every third position from end, ,-
$pattern = '/[[:digit:]]{1,3}(\.[[:digit:]]{3})*(\ )*,-/';

// Tousand dot every third position from end with comma
$pattern = '/([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?/';

// Tousand dot every third position from end with comma and Kč
$pattern = '/([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?(\ )*Kč/';

$pattern = '/([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?(\ )*CZK/';
// CZK(\ )*([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?/';
$pattern = '/CZK(\ )*([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?/';

$pattern = '/(([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?(\ )*CZK|CZK(\ )*([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?)/';

$pattern = '(([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?(\ )*CZK|CZK(\ )*([[:digit:]]){1,3}(\.[[:digit:]]{3})*(,[[:digit:]]*)?)';

$pattern = '/'.$pattern.'/';
