#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name:   Reformat DNA
Author: Jaroslav Langer (langera@vscht.cz)
Description:
    Script reads sequences at stdin and formates it at stdout.
Lines starting with SEQ_NAME_SYMBOL are considered starts of new sequences.
"""
import sys
import re
import argparse

LINE_LENGTH = 100 # Newline character is not included i.e. for width 80 write 79
NA = "NA"
AA = "AA"
IUB_CODES = {
    NA: ['A','C','G','T','R','Y','K','M','S','W','B','D','H','V','N'],
    AA: ['A','B','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
}
SEQ_NAME_SYMBOL = '>'
SEQ_NAME_GENERIC = "Unknown sequence"

def readSequenceName(line):
    """Extract sequence name from given string. Return None if SEQ_NAME_SYMBOL is not found."""
    if (line[0] == SEQ_NAME_SYMBOL):
        pattern = f'(?<={SEQ_NAME_SYMBOL}).*(?=\n)'
        name = re.search(pattern, line)
        return name.group(0).strip() if (name is not None) else line[1:-1].strip()
    return None

def iterSequences(seq_type):
    """Yield name, sequence tuple for every sequence found at stdin."""
    name = None
    seq_chars = []
    for line in sys.stdin:
        next_name = readSequenceName(line)
        if ((next_name) and (name is None) and (len(seq_chars) == 0)):
            name = next_name
        elif (not next_name):
            seq_chars.extend([c.upper() for c in line if c.upper() in IUB_CODES[seq_type]])
        else:
            yield name, ''.join(seq_chars)
            name = next_name
            seq_chars = []
    yield name, ''.join(seq_chars)

def writeSequence(name, sequence):
    """Print sequence name and sequence. Sequence is splited according to the LINE_LENGTH, sequence name is not."""
    print(f"{SEQ_NAME_SYMBOL} {name}") if (name is not None) else print(f"{SEQ_NAME_SYMBOL} {SEQ_NAME_GENERIC}")
    for i in range(0, len(sequence), LINE_LENGTH):
        print(sequence[i : i + LINE_LENGTH]) if (i < len(sequence) - LINE_LENGTH) else print(sequence[i : ])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-t", "--type", choices=[NA, AA], help="reformat nucleic acid or amino acid sequence")
    args = parser.parse_args()
    for name, sequence in iterSequences(args.type):
        writeSequence(name, sequence)
