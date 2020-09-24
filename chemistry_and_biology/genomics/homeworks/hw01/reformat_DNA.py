#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name:   Reformat DNA
Author: Jaroslav Langer (langera@vscht.cz)
Description:
Script reads sequences at stdin and formates it as fasta at stdout.
Details:
All non-IUB DNA codes are ignored.
"""
from bio_tools import iterSequences, NA, writeSequence

if __name__ == "__main__":
    for name, sequence in iterSequences(NA, filter=True):
        writeSequence(name, sequence)
