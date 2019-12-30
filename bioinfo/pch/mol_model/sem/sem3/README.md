# Seminar third

[Clausiova-Clapeyronova rovnice](https://physics.mff.cuni.cz/kfpp/skripta/kurz_fyziky_pro_DS/display.php/molekul/8_2)

## Postup

1) V systému se dvema fázemi oddělenými rovinným
rozhraním stanovte tlak nasycených par v závislosti
na teplotě pro dvě teploty. Pouěijte MD s libovolným
termostatem.
1) Stanovte střední teplotu a tlak, simulací páry v MC
pak stanovte kompresibilitní faktor.
1) Z Clausiovy–Clapeyronovy rovnice (s opravou na neidealitu páry) stanovte výparnou entalpii včetně odhadu standardní chyby.
1) Stanovte výparnou entalpii ze střední potenciální energie kapaliny v periodických
okrajových podmínkách.
1) Porovnejte obe hodnoty. 

## Numbers from python calculator
```
>>> T1
0.149762
>>> p1
0.000826012
>>> T2
0.189763
>>> p2
0.00417761
>>> t_avg
0.16976249999999998
>>> p_avg = math.sqrt(p1*p2)
>>> p_avg
0.00185762105697583
>>> rho_avg = p_avg/t_avg
>>> rho_avg
0.010942469962305162
>>> -0.914521*((math.log(p1/p2))/(1/T1 - 1/T2))
1.0531452756069177
>>> 0.914521 * (math.sqrt(p1**2 + p2**2)/(1/T1 - 1/T2))
0.002766887132472206
```