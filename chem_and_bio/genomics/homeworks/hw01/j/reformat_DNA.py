#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name:   Reformat DNA
Author: Jaroslav Langer (langera@vscht.cz)
Description:
Script reads sequences and formates it as correct fasta.
Details:
All non-IUB DNA codes are ignored.
"""
import sys
import argparse
from bio_tools import iterSequences, DNA, writeSequence

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
        help='Optional input, if not given, stdin is used')
    parser.add_argument('output', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
        help='Optional output, if not given, stdout is used')
    args = parser.parse_args()

    for name, sequence in iterSequences(args.input, DNA, filter=True):
        writeSequence(args.output, name, sequence)
