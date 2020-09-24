#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name:   Get region AA
Author: Jaroslav Langer (langera@vscht.cz)
Description:
Script reads sequences at stdin, gives basic statistics about sequences lengths, AA composition etc.
Details:
The amino acid percents are provided togeather with a crc32 checksum.
"""
# základní statistika fasta filu (délka sekvence, ACGT složení, nejasné báze, kontrolní součet

# TODO some problems with argparse, maybe just sys.argv[0] will be easier

from bio_tools import iterSequences, NA
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('integers', type=int, nargs='2', help='range of letters both edges included, first letter has number 1')
    args = parser.parse_args()
    for name, sequence in iterSequences(NA, filter=True):
        print("PL")
        # print(sequence[args.integers[0] - 1 : args.integers[1]])
