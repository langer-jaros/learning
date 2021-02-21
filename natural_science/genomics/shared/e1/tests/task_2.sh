#!/bin/bash

# commands assinments
reformat_DNA="./bio.py reformat dna"
reverse_complement="./bio.py rc dna"

echo '-------------------------------------------------------------------------
# Reverse complement the reformated data
# and see difference of reformated mm_pax6-plain.txt and its reverse_complement
# 
# commands:
# ```sh
reformat_DNA < data/real/mm_pax6-plain.txt | 
reverse_complement > data/results/mm_pax6_rc.txt

diff_lines=$(
    diff data/results/mm_pax6_reformated.txt data/results/mm_pax6_rc.txt |wc -l
)
total_lines=$(
    cat data/results/mm_pax6_reformated.txt data/results/mm_pax6_rc.txt | wc -l
)

echo "Lines from both files - different lines: \
$total_lines - $(($diff_lines-2)) = $(($total_lines - $(($diff_lines - 2)))) \
(~ lines with sequence name are identical)"
# ```
-------------------------------------------------------------------------'

# Reverse complement the reformated data
$reformat_DNA < data/real/mm_pax6-plain.txt | 
$reverse_complement > data/results/mm_pax6_rc.txt
# See difference of reformated mm_pax6-plain.txt and its reverse_complement
diff_lines=$(diff data/results/mm_pax6_reformated.txt data/results/mm_pax6_rc.txt | wc -l) # 76 (74 + 2)
total_lines=$(cat data/results/mm_pax6_reformated.txt data/results/mm_pax6_rc.txt | wc -l) # 76 (Only the name is identical)

echo "Lines from both files - different lines: \
$total_lines - $(($diff_lines-2)) = $(($total_lines - $(($diff_lines - 2)))) \
(~ lines with sequence name are identical)"

echo '-------------------------------------------------------------------------
# Try to do two reverse complements in a row
# 
# commands:
# ```sh
reformat_DNA < data/real/mm_pax6-plain.txt \
| $reverse_complement | $reverse_complement > data/results/mm_pax6_rc_rc.txt

diff_lines=$(
    diff data/results/mm_pax6_reformated.txt data/results/mm_pax6_rc_rc.txt | wc -l
)
echo "Number of different lines: $diff_lines"
# ```
-------------------------------------------------------------------------'

# Reverse complement the reverse complement of the reformated mm_pax6-plain.txt
$reformat_DNA < data/real/mm_pax6-plain.txt | $reverse_complement | $reverse_complement > data/results/mm_pax6_rc_rc.txt
# Compare reformated mm_pax6-plain.txt with two times reverse complement of reformated mm_pax6-plain.txt
diff_lines=$(diff data/results/mm_pax6_reformated.txt data/results/mm_pax6_rc_rc.txt | wc -l) # 0 (identical files)
echo "Number of different lines: $diff_lines"




