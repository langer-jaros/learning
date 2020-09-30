# Homework 1

`2020/09/30, Jaroslav Langer`

## Content

- [Assignment](#assignment)
- [Aliases](#aliases)
- [Sources](#sources)

## Assignment

[Assignment](http://bio.img.cas.cz/GAA2020/E1/)

The "scripts" are created as three python files.

1. bio_config.py - all the configuration and biological data
2. bio_tools.py - all the code logic
3. bio.py   - script which uses argparse, so works as every command

## Aliases

for usage of the separate commands without calling `./bio.py format dna < in > out`

```sh
alias bio="./bio.py"
alias reformat_DNA="bio reformat dna"
alias reformat_AA="bio refo aa"
alias reverse_complement="bio rc dna"
alias statistic_DNA="bio statistic dna"
alias statistic_AA="bio stat aa"
alias get_region="bio gr"
alias translate="bio tran"
```

## Sources

- [IUB CODES](http://bioinformatics.org/sms2/iupac.html)
- [AMINO GROUPS](https://www.britannica.com/science/amino-acid/Standard-amino-acids)
- [DNA CODON TABLE](https://en.wikipedia.org/wiki/DNA_codon_table)

