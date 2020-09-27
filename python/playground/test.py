#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse

parser = argparse.ArgumentParser(description=__doc__)

parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
# parser.parse_args(['input.txt', 'output.txt'])
args = parser.parse_args()

print(f"infile: {args.infile}, outfile: {args.outfile}")

args.outfile.write("AHOJ, jak se mas")

# parser.add_argument('first', type=int, help='First index of desired string range. String is indexed from 1 to n.')
# parser.add_argument('last', type=int, help='Last index of desired string range. String is indexed from 1 to n.')
# parser.add_argument('integers', type=int, nargs=2, help='Two integers')
# parser.add_argument("-t", "--type", choices=["DNA", "AA"], help="reformat nucleic acid or amino acid sequence")
# args = parser.parse_args()

# print(f'argv.type: {args.type}')
# print(f'argv.integers: {args.integers}')
# print(f'first: {args.first}, last: {args.last}')
