#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name:   Bioinformatic tools
Author: Jaroslav Langer (langera@vscht.cz)
Description:
    Script reads sequences at stdin and formates it at stdout.
Lines starting with SEQ_NAME_START are considered starts of new sequences.
"""
import sys
import re
import argparse
import zlib
from bio_config import *

def readSequenceName(line, seq_start):
    """Extract sequence name from given string. Return None if SEQ_NAME_START is not found."""
    if (line[0: len(seq_start)] == seq_start):
        pattern = '(?<={}).*(?=\n)'.format(seq_start)
        name = re.search(pattern, line)
        return name.group(0).strip() if (name is not None) else line[1:-1].strip()
    return None

def sequenceListFromLine(sequence_line, filter, seq_type):
    if (not filter):
        return sequence_line[0 : -1]
    elif (seq_type == RNA):
        return [c.replace(T, U) for c in sequence_line.upper().replace(U, T) if c in IUB_CODES[DNA]]
    return [c for c in sequence_line.upper() if c in IUB_CODES[seq_type]]

def iterSequences(file_in, seq_type, filter=False, seq_start=SEQ_NAME_START):
    """Yield name, sequence tuple for every sequence found at stdin."""
    name = None
    seq_substrings = []
    for line in file_in:
        next_name = readSequenceName(line, seq_start)
        if ((next_name) and (name is None) and (len(seq_substrings) == 0)):
            name = next_name
        elif (not next_name):
            seq_substrings.extend(sequenceListFromLine(line, filter, seq_type))
        else:
            yield name, ''.join(seq_substrings)
            name = next_name
            seq_substrings = []
    yield name, ''.join(seq_substrings)

def writeSequence(file_out, name, sequence, line_length=LINE_LENGTH, seq_start=SEQ_NAME_START):
    """Print sequence name and sequence. Sequence is splited according to the line_length, sequence name is not."""
    name = name if (name is not None) else SEQ_NAME_GENERIC
    file_out.write("{} {}\n".format(seq_start, name))
    for i in range(0, len(sequence), line_length):
        line = sequence[i : i + line_length] if (i < len(sequence) - line_length) else sequence[i : ]
        file_out.write('{}\n'.format(line))

def getReverseComplement(sequence, seq_type):
    if (seq_type == RNA):
        return ''.join([COMPLEMENTS[x] for x in reversed(sequence.upper().replace(U, T))]).replace(T, U)
    return''.join([COMPLEMENTS[x] for x in reversed(sequence.upper())])
     

def residuePercent(sequence, residue):
    count = sum([sequence.count(c) for c in residue]) if isinstance(residue, list) else sequence.count(residue)
    return ((count / len(sequence)) * 100) if (len(sequence) is not 0) else 0.0

def writeStatistics(file_out, name, seq, seq_type, seq_start=SEQ_NAME_START):
    file_out.write('{} NAME: {}\n'.format(seq_start, name))
    file_out.write('Length: {}\n'.format(len(seq)))
    file_out.write('Composition: ')
    for key, group in GROUPS[seq_type].items():
        file_out.write('{}={:.3}%'.format(key, residuePercent(seq, group)))
        file_out.write(', ') if (key != list(GROUPS[seq_type].items())[-1][0]) else file_out.write('\n')
    file_out.write('Checksum(crc32): {}\n\n'.format(zlib.crc32(bytes(seq, "utf-8"))))

def getRegion(sequence, first, last):
    return sequence[first - 1: last]

def translateCodon(codon, codon_len=CODON_LEN):
    return CODONS.get(codon[0], {}).get(codon[1], {}).get(codon[2], XAA) if (len(codon) == codon_len) else XAA

def translateSequence(sequence, codon_len=CODON_LEN):
    sequence = sequence.upper().replace(U, T)
    return ''.join([translateCodon(sequence[i : i + codon_len]) for i in range(0, len(sequence), codon_len)])

