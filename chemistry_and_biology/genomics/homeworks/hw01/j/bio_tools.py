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
from bio_config import *

def readSequenceName(line):
    """Extract sequence name from given string. Return None if SEQ_NAME_SYMBOL is not found."""
    if (line[0] == SEQ_NAME_SYMBOL):
        pattern = f'(?<={SEQ_NAME_SYMBOL}).*(?=\n)'
        name = re.search(pattern, line)
        return name.group(0).strip() if (name is not None) else line[1:-1].strip()
    return None

def iterSequences(file_in, seq_type, filter=False):
    """Yield name, sequence tuple for every sequence found at stdin."""
    name = None
    seq_substrings = []
    for line in file_in:
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

def writeSequence(file_out, name, sequence, line_length=LINE_LENGTH):
    """Print sequence name and sequence. Sequence is splited according to the line_length, sequence name is not."""
    name = name if (name is not None) else SEQ_NAME_GENERIC
    file_out.write(f"{SEQ_NAME_SYMBOL} {name}\n")
    for i in range(0, len(sequence), line_length):
        line = sequence[i : i + line_length] if (i < len(sequence) - line_length) else sequence[i : ]
        file_out.write(f'{line}\n')

def getReverseComplement(sequence, seq_type):
    return ''.join([COMPLEMENTS[seq_type][x] for x in reversed(sequence)])

def residuePercent(sequence, residue):
    count = sum([sequence.count(c) for c in residue]) if isinstance(residue, list) else sequence.count(residue)
    return ((count / len(sequence)) * 100) if (len(sequence) is not 0) else 0.0

def writeStatistics(file_out, name, seq, seq_type):
    file_out.write(f'{SEQ_NAME_SYMBOL} NAME: {name}\n')
    file_out.write(f'Length: {len(seq)}\n')
    file_out.write(f'Composition: ')
    for key, group in GROUPS[seq_type].items():
        file_out.write(f'{key}={residuePercent(seq, group):.3}%')
        file_out.write(', ') if (key != list(GROUPS[seq_type].items())[-1][0]) else file_out.write('\n')
    file_out.write(f'Checksum(crc32): {zlib.crc32(bytes(seq, "utf-8"))}\n\n')

def getRegion(sequence, first, last):
    return sequence[first: last + 1]

def translateCodon(codon, seq_type, codon_len=CODON_LEN):
    return CODONS.get(codon[0], {}).get(codon[1], {}).get(codon[2], XAA)

def translateSequence(sequence, seq_type, codon_len=CODON_LEN):
    return ''.join([translateCodon(sequence[i : i + codon_len], seq_type) for i in range(0, len(sequence), codon_len)])

