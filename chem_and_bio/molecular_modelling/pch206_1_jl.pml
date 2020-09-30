fetch 1pcq

select GroES, chain O + chain P + chain Q + chain R + chain S + chain T + chain U
color white, GroES

select cis, chain A + chain B + chain C + chain D + chain E + chain F + chain G
color bluewhite, cis

select trans, chain H + chain I + chain J + chain K + chain L + chain M + chain N 
color grey, trans
select GroEL, (cis) or (trans)

select cap, chain O
color magenta, cap

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
zoom chain A

hide (sth)



select asp52, resn asp and resi 52 and chain A

select thr89-90, resn thr and resi 89-90 and chain A

bind-loop, resi 87-91 and chain A

select asp52_398, resn asp and (resi 52,398) and chain A

select gly_53, resn gly and resi 53 and chain A

select k, symbol k and chain A

select mg, symbol mg and chain A

select AlF3, resn AF3 and chain A

