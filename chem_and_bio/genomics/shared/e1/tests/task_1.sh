#!/bin/bash

# commands assinments
reformat_DNA="./bio.py reformat dna"
data_path=".."

echo '-------------------------------------------------------------------------
Reformat mm_pax6-plain.txt with line lengths 70
and perform diff with mm_pax6.fasta.

commands:
```sh
reformat_DNA -l 70 < data/real/mm_pax6-plain.txt > \
data/results/mm_pax6_reformated_l_70.txt

diff data/real/mm_pax6.fasta data/results/mm_pax6_reformated_l_70.txt
```

See difference between well formated fasta, and plain.txt reformated:
-------------------------------------------------------------------------'

# Reformat mm_pax6-plain.txt with line lengths 70
$reformat_DNA -l 70 < data/real/mm_pax6-plain.txt\
> data/results/mm_pax6_reformated_l_70.txt
# See the difference with mm_pax6.fasta
diff data/real/mm_pax6.fasta data/results/mm_pax6_reformated_l_70.txt

