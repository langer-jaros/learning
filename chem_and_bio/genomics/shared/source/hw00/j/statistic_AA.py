#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name:   Statistic AA
Author: Jaroslav Langer (langera@vscht.cz)
Description:
Script reads sequences at stdin, gives basic statistics about sequences lengths, AA composition etc.
Details:
The amino acid percents are provided togeather with a crc32 checksum.
"""
# základní statistika fasta filu (délka sekvence, ACGT složení, nejasné báze, kontrolní součet

from bio_tools import iterSequences, AA, writeStatistics

if __name__ == "__main__":
    for name, sequence in iterSequences(AA):
        writeStatistics(name, sequence, AA)
