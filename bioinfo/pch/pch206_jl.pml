fetch 1pcq
#print(cmd.get_object_list('all'))

select GroEL, chain A + chain B + chain C + chain D + chain E + chain F + chain G + chain H + chain I + chain J + chain K + chain L + chain M + chain N 
color cyan, GroEL

select GroES, chain O + chain P + chain Q + chain R + chain S + chain T + chain U
color green, GroES

color red, resn adp

color violet, resn AF3
color green, symbol f
color darksalmon, symbol al

color orange, symbol k
color yellow, symbol mg

deselect

set_view (\
    -0.917876959,    0.339205325,    0.205929220,\
     0.283684462,    0.198055163,    0.938221872,\
     0.277472764,    0.919614553,   -0.278019875,\
     0.002011210,    0.000015639, -134.798355103,\
    34.714260101,  -80.804893494,  -10.898902893,\
    80.322494507,  191.408370972,  -20.000000000 )

#rock
