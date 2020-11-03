# Exact and Heuristic Approaches for the Constructive Optimization Knapsack Problem

2020/11/02

Jaroslav Langer

<!-- ## MUST BE HERE omit in toc

- Popis implementovaných metod.
- Srovnání výpočetních časů hrubé síly, metody větví a hranic, dynamického programování a heuristiky cena/váha (stačí jedna). Grafy vítány.
  - Tj. závislosti výpočetních časů na velikosti instance
- Porovnání relativních chyb (průměrných a maximálních) obou heuristik.
  - Tj. závislosti rel. chyby na velikosti instance
- U FPTAS algoritmu pozorujte (naměřte, zdokumentujte) závislost chyby a výpočetního času algoritmu na zvolené přesnosti zobrazení (pro několik různých přesností), srovnání maximální naměřené chyby s teoreticky předpokládanou.
  - Tj. zvolte několik požadovaných přesností (ε), v závislosti na ε měřte čas běhu a reálnou (maximální, případně i průměrnou) chybu algoritmu
Zhodnocení naměřených výsledků. -->

## Contents <!-- omit in toc -->

- [Description of Approaches](#description-of-approaches)
- [Time Complexity Comparison](#time-complexity-comparison)
  - [NK](#nk)
  - [ZKC](#zkc)
  - [ZKW](#zkw)
- [Relative Error Comparison](#relative-error-comparison)
  - [NK](#nk-1)
  - [ZKC](#zkc-1)
  - [ZKW](#zkw-1)
- [Complexity and Error Dependencies on Precision](#complexity-and-error-dependencies-on-precision)
  - [NK](#nk-2)
  - [ZKC](#zkc-2)
  - [ZKW](#zkw-2)

## Description of Approaches

1) **Brute Force**

Hrubou silou

1) **Branch and Bound**

Metodou větví a hranic. Metodu větví a hranic použijte tak, aby omezujícím faktorem byla hodnota optimalizačního kritéria. Tj. použijte ořezávání shora (překročení kapacity batohu) i zdola (stávající řešení nemůže být lepší než nejlepší dosud nalezené).

3) **Dynamic Programming**

Metodou dynamického programování (dekompozice podle kapacity nebo podle cen),

4) **Greedy Heuristic**

Jednoduchou greedy heuristikou

5) **REDUX**

Modifikací této heuristiky (redux), která uvažuje také řešení se sólo nejdražší věcí

6) **FPTAS**

FPTAS algoritmem, tj. s použitím modifikovaného dynamického programování s dekompozicí podle ceny (při použití dekompozice podle kapacity není algoritmus FPTAS).
- Pozor! Pokud implementujete FPTAS pomocí zanedbávání bitů, musíte pro daný počet zanedbaných bitů vypočítat max. chybu (ε). V experimentálních výsledcích by počet zanedbaných bitů neměl figurovat, neb neříká nic konkrétního o přesnosti. Pozor, tato max. chyba je jiná pro každou instanci, nezávisí pouze na velikosti instance, ale také na max. ceně.
- Pozor! V některých instancích se objevují věci, které svojí hmotností překračují kapacitu batohu. Samozřejmě se jedná o platné instance. Nicméně tyto věci komplikují přepočet cen u FPTAS. Zvažte sami, jak se s tím vypořádat. Řešení je snadné.

## Time Complexity Comparison

### NK

### ZKC

### ZKW

## Relative Error Comparison

### NK

### ZKC

### ZKW

## Complexity and Error Dependencies on Precision

### NK

### ZKC

### ZKW

