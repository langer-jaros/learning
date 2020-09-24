#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name:   Reformat AA
Author: Jaroslav Langer (langera@vscht.cz)
Description:
Script reads sequences at stdin and formates it as fasta at stdout.
Details:
All non-IUB AA codes are ignored.
"""
from bio_tools import iterSequences, AA, writeSequence

if __name__ == "__main__":
    for name, sequence in iterSequences(AA, filter=True):
        writeSequence(name, sequence, 60)
