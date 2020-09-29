#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name:   Reverse complement
Author: Jaroslav Langer (langera@vscht.cz)
Description:
    Script reads sequences at stdin and formates it at stdout.
Lines starting with SEQ_NAME_SYMBOL are considered starts of new sequences.
"""
from bio_tools import iterSequences, DNA, writeSequence, getReverseComplement

if __name__ == "__main__":
    for name, sequence in iterSequences(DNA):
        writeSequence(name, getReverseComplement(sequence, DNA))
