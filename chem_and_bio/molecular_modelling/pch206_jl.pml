# Jaroslav Langer 2020/01/16
# Gather trans GroEL and paint it grey #
reinitialize
bg white

fetch 1pcq, trans
fetch 1pcq
#hide all
#show cartoon, all
rotate x, 90

select trans, trans
remove (chain A + chain B + chain C + chain D + chain E + chain F + chain G + chain O + chain P + chain Q + chain R + chain S + chain T + chain U) and trans
color grey, trans

# Gather cis GroEL and GroEs #
# and paint it whiteblue, white respectively #

remove (chain H + chain I + chain J + chain K + chain L + chain M + chain N) and 1pcq 

select GroES, chain O + chain P + chain Q + chain R + chain S + chain T + chain U
color white, GroES

select cis, chain A + chain B + chain C + chain D + chain E + chain F + chain G
color bluewhite, cis

# Paint magenta part of GroES connected to chain A #
select cap, chain O
color magenta, cap

rotate y, 90

select apical, resi 193-375 and chain A
color red, apical

select intermediate, (resi 138-192 or resi 376-410) and chain A
color green, intermediate

select  equatorial, (resi 1-137 or resi 411-524) and chain A
color cyan, equatorial

select  equatorial_trans, (resi 1-137 or resi 411-524) and chain H
color cyan, equatorial_trans

select intermediate_trans, (resi 138-192 or resi 376-410) and chain H
color green, intermediate_trans

select apical_trans, resi 193-375 and chain H
color red, apical_trans

# Folowing doesn't work as expected #
#rotate z, 180,  trans
#align trans, cis

# Paint ADP and AlF3 #
color red, hetatm and chain A
select AlF3, resn AF3 and chain A
color violet, AlF3
color forest, symbol f and chain A
color darksalmon, symbol al and chain A

# Paint sites interacting with AlF3 #
color orange, symbol k and chain A
color yellow, symbol mg and chain A
select bind-loop, resi 87-91 and chain A and 1pcq
color blue, bind-loop
select thr89-90, resn thr and resi 89-90 and chain A and 1pcq
color deeppurple, thr89-90

select asp52_398, resn asp and (resi 52,398) and chain A and 1pcq
color purpleblue, asp52_398

select gly_53, resn gly and resi 53 and chain A and 1pcq
color deepsalmon, gly_53

deselect

# Overall picture of 1pcq #
set_view (\
     0.999673545,    0.023698376,   -0.007747645,\
    -0.022014135,    0.984844565,    0.171912193,\
     0.011703811,   -0.171685129,    0.985065162,\
    -0.000000000,    0.000000000, -714.230102539,\
    79.272903442,  -51.978923798,   -6.390968323,\
   484.791992188,  943.668029785,  -20.000000000 )

# Picture of GroEL cis monomer with binded ADP/AlF3 #
set_view (\
     0.987364769,   -0.035122894,    0.154434755,\
     0.007654809,    0.984528244,    0.174964234,\
    -0.158191368,   -0.171570629,    0.972373009,\
     0.000000000,    0.000000000, -346.048156738,\
    89.246261597,  -14.712966919,   33.665977478,\
   296.019836426,  396.076293945,  -20.000000000 )

# Picture of GroEL trans monomer with not binded ATP #
set_view (\
    -0.727017283,    0.096057706,   -0.679846406,\
    -0.043732170,   -0.994612753,   -0.093765222,\
    -0.685203373,   -0.038442478,    0.727314115,\
     0.000000000,    0.000000000, -312.703430176,\
    54.065456390,  -96.539840698,   32.703926086,\
   265.460113525,  359.946777344,  -20.000000000 )

# Picture of GroEL AlF3 bining-site #
set_view (\
    -0.999278307,    0.036936365,    0.003998172,\
     0.029146358,    0.712661982,    0.700858891,\
     0.023040548,    0.700494945,   -0.713240266,\
     0.000000000,    0.000000000, -105.727012634,\
    86.901069641,  -24.914100647,   38.611782074,\
    35.820537567,  175.633377075,  -20.000000000 )

