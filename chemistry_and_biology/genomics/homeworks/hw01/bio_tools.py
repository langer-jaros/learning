#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name:   Bioinformatic tools
Author: Jaroslav Langer (langera@vscht.cz)
Description:
    Script reads sequences at stdin and formates it at stdout.
Lines starting with SEQ_NAME_SYMBOL are considered starts of new sequences.
"""
import sys
import re
import argparse
import zlib

LINE_LENGTH = 100 # Newline character is not included i.e. for width 80 write 79
NA = "NA"
AA = "AA"
IUB_CODES = {
    NA: ['A','C','G','T','R','Y','K','M','S','W','B','D','H','V','N'],
    AA: ['A','B','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
}
COMPLEMENTS = {
    'A': 'T',    'C': 'G',    'G': 'C',    'T': 'A',
    'R': 'Y',    'Y': 'R',    'K': 'M',    'M': 'K',
    'B': 'V',    'D': 'H',    'H': 'D',    'V': 'B',
    'S': 'S',    'W': 'W',    'N': 'N'
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

def iterSequences(seq_type, filter=False):
    """Yield name, sequence tuple for every sequence found at stdin."""
    name = None
    seq_substrings = []
    for line in sys.stdin:
        next_name = readSequenceName(line)
        if ((next_name) and (name is None) and (len(seq_substrings) == 0)):
            name = next_name
        elif (not next_name):
            substrings = [c.upper() for c in line if c.upper() in IUB_CODES[seq_type]] if filter else line[0 : -1]
            seq_substrings.extend(substrings)
        else:
            yield name, ''.join(seq_substrings)
            name = next_name
            seq_substrings = []
    yield name, ''.join(seq_substrings)

def writeSequence(name, sequence, line_length=LINE_LENGTH):
    """Print sequence name and sequence. Sequence is splited according to the line_length, sequence name is not."""
    print(f"{SEQ_NAME_SYMBOL} {name}") if (name is not None) else print(f"{SEQ_NAME_SYMBOL} {SEQ_NAME_GENERIC}")
    for i in range(0, len(sequence), line_length):
        print(sequence[i : i + line_length]) if (i < len(sequence) - line_length) else print(sequence[i : ])

def getReverseComplement(sequence):
    return ''.join([COMPLEMENTS[x] for x in reversed(sequence)])

def basePercent(sequence, base):
    return (sequence.count(base) / len(sequence)) * 100 if len(sequence) is not 0 else 0.0

def writeStatisticsNa(seq):
    A, C, T, G = basePercent(seq, 'A'), basePercent(seq, 'C'), basePercent(seq, 'T'), basePercent(seq, 'G')
    other = 100.0 - (A + C + T + G) if len(seq) > 0 else 0.0
    check = zlib.crc32(bytes(seq, 'utf-8'))
    print(f"length: {len(seq)} nts, A={A:.3}%, C={C:.3}%, T={T:.3}%, G={G:.3}%",
        f", Other={other:.3}%, checksum(crc32): {check}")

def writeStatistics(name, seq, seq_type):
    print(f'NAME: {name}')
    if seq_type == NA:
        writeStatisticsNa(seq)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-t", "--type", choices=[NA, AA], help="reformat nucleic acid or amino acid sequence")
    args = parser.parse_args()
    for name, sequence in reformatSequences(args.type):
        writeSequence(name, sequence)
