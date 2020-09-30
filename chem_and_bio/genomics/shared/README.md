# Homework 1

`2020/09/30, Jaroslav Langer`

## Content

- [Assignment](#assignment)
- [Aliases](#aliases)
- [Showroom](#Showroom)
    + [Task 1 - Reformat DNA (AA)](#task-1---reformat-dna-(aa))
    + [Task 2 - Reverse complement](#task-2---reverse-complement)
    + [Task 3 - Statistic DNA](#task-3---statistic-dna)
    + [Task 4 - Get region](#task-4---get-region)
    + [Task 5 - Translate](#task-5---translate)
- [Links](#links)

## Assignment

[Assignment](http://bio.img.cas.cz/GAA2020/E1/)

The "scripts" are created as three python files.

1. bio_config.py - all the code and biological configurations
2. bio_tools.py - all the code logic
3. bio.py - script which uses argparse, so it works as any other command, just start with `./bio.py --help`

## Aliases

For usage of the separate commands without calling `./bio.py format dna < in > out`.

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

## Showroom

### Task 1 - Reformat DNA (AA)

```sh
### Reformat mm_pax6-plain.txt ###
reformat_DNA < data/real/mm_pax6-plain.txt > data/results/mm_pax6_reformated.txt
### See the difference with mm_pax6.fasta ###
diff data/real/mm_pax6.fasta data/results/mm_pax6_reformated.txt | wc -l # 95 (93 diff lines + 2 informative)
cat data/real/mm_pax6.fasta data/results/mm_pax6_reformated.txt | wc -l # 93 (lines - absolutely different files)
```

**Files are different because of different line lengths**

```sh
### Reformat mm_pax6-plain.txt with line lengths ###
reformat_DNA -l 70 < data/real/mm_pax6-plain.txt > data/results/mm_pax6_reformated_l_70.txt
### See the difference with mm_pax6.fasta ###
diff data/real/mm_pax6.fasta data/results/mm_pax6_reformated_l_70.txt
```

```stdout
1c1
< >gi|860610049|ref|NM_001244198.2| Mus musculus paired box 6 (Pax6), transcript variant 1, mRNA
---
> > Unknown sequence
55d54
< 
```

### Task 2 - Reverse complement

```sh
# Reverse complement the reformated data
reformat_DNA < data/real/mm_pax6-plain.txt | reverse_complement > data/results/mm_pax6_rc.txt
# See difference of reformated mm_pax6-plain.txt and its reverse_complement
diff data/results/mm_pax6_reformated.txt data/results/mm_pax6_rc.txt | wc -l # 76 (74 + 2)
cat data/results/mm_pax6_reformated.txt data/results/mm_pax6_rc.txt | wc -l # 76 (Only the name is identical)
```

**Try to do two reverse complements in a row**

```sh
# Reverse complement the reverse complement of the reformated mm_pax6-plain.txt
reformat_DNA < data/real/mm_pax6-plain.txt | reverse_complement | reverse_complement > data/results/mm_pax6_rc_rc.txt
# Compare reformated mm_pax6-plain.txt with two times reverse complement of reformated mm_pax6-plain.txt
diff data/results/mm_pax6_reformated.txt data/results/mm_pax6_rc_rc.txt | wc -l # 0 (identical files)
```

### Task 3 - Statistic DNA

```sh
# Create statistic of reformated mm_pax6-plain.txt
reformat_DNA < data/real/mm_pax6-plain.txt | statistic_DNA > data/results/mm_pax6_stat.txt
# Show statistics
cat data/results/mm_pax6_stat.txt
```

```stdout
> NAME: Unknown sequence
Length: 3651
Composition: adenine=29.6%, cytosine=22.0%, guanine=22.5%, thymine=25.9%, other=0.0%, gap=0.0%
Checksum(crc32): 3344005577

```

**Compare the statistics with statistics of mm_pax6.fasta**

```sh
statistic_DNA < data/real/mm_pax6.fasta | diff data/results/mm_pax6_stat.txt -
```

```stdout
1c1
< > NAME: Unknown sequence
---
> > NAME: gi|860610049|ref|NM_001244198.2| Mus musculus paired box 6 (Pax6), transcript variant 1, mRNA
```

### Task 4 - Get region

```sh
# Get region 286-1596 from mm_pax6.fasta
get_region 286 1596 < data/real/mm_pax6.fasta > data/results/mm_pax6_cds.fasta
# Count expected length
echo "1596 - 286 + 1" | bc # 1311
# Check length
statistic_DNA data/results/mm_pax6_cds.fasta
```

```stdout
> NAME: gi|860610049|ref|NM_001244198.2| Mus musculus paired box 6 (Pax6), transcript variant 1, mRNA
Length: 1311
Composition: adenine=28.6%, cytosine=27.4%, guanine=25.2%, thymine=18.8%, other=0.0%, gap=0.0%
Checksum(crc32): 701706402

```

### Task 5 - Translate

```sh
# translate region 286 1596 of mm_pax6.fasta
translate < data/results/mm_pax6_cds.fasta > data/results/mm_pax6_aa.fasta
# Let's look at it
cat data/results/mm_pax6_aa.fasta
```

```stdout
> gi|860610049|ref|NM_001244198.2| Mus musculus paired box 6 (Pax6), transcript variant 1, mRNA
MQNSHSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQTHADAKVQVLDNENVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSK
IAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEKQQMGADGMYDKLRMLNGQTGSWGTRPGWYPGTSVPGQPTQDGCQQQEGGGEN
TNSISSNGEDSDEAQMRLQLKRKLQRNRTSFTQEQIEALEKEFERTHYPDVFARERLAAKIDLPEARIQVWFSNRRAKWRREEKLRNQRRQASNTPSHIP
ISSSFSTSVYQPIPQPTTPVSSFTSGSMLGRTDTALTNTYSALPPMPSFTMANNLPMQPPVPSQTSSYSCMLPTSPSVNGRSYDTYTPPHMQTHMNSQPM
GTSGTTSTGLISPGVSVPVQVPGSEPDMSQYWPRLQ*
```

## Links

- [IUB CODES](http://bioinformatics.org/sms2/iupac.html)
- [AMINO GROUPS](https://www.britannica.com/science/amino-acid/Standard-amino-acids)
- [DNA CODON TABLE](https://en.wikipedia.org/wiki/DNA_codon_table)

## TODO

- delete space after SEQ_NAME_START (e.g. ">beatiful" not "> ugly")
- add possibility to specify SEQ_NAME_DEFAULT
- start the name with given operation if seq name not given (e.g. ">translated: bla bla mRNA")
- split translated proteins by STOP codons with number (e.g. ">translated: bla bla #3)
