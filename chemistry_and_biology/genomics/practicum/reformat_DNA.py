#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Name: Reformat dna
Author: Jaroslav Langer (langera@vscht.cz)
Description:
Does a reformat of a given file into format fasta.
Details:
If a line starts with symbol '>' it is taken as a start of a new sequence
Arguments:
Script takes at least one argument - name of the input file
If second argument is given it is taken as the name of the output file,
otherwise the output file is derived from the input name. 
'''
import sys
import re

# CONSTATNS
LINE_LENGTH = 100
IUB_CODES = ['A','C','G','T','R','Y','K','M','S','W','B','D','H','V','N']
SEQ_NAME_SYMBOL = '>'
SEQ_NAME_GENERIC = "Unknown sequence"

def resolve_arguments():
    if (len(sys.argv) < 2):
        print("Τhe path to the file was not specified, give it as a first argument.")
        return None
    elif (len(sys.argv) == 2):
        path_in = sys.argv[1]
        i = path_in.rfind('.')
        path_out = [char for char in path_in]
        path_out.insert(i, '_refined')
        path_out = ''.join(path_out)
    else:
        if (len(sys.argv) > 3):
            print("\nWARNING! - Too much input parameters, only the first two are used (as input path and output path).\n")
        path_in = sys.argv[1]
        path_out = sys.argv[2]
    return (path_in, path_out)

# Returns true when the full file was read
def readSequence(f_in, f_out):
    line = f_in.readline()
    if (line[0] == SEQ_NAME_SYMBOL):
        f_out.write(f'{line}\n')
        chars = []
    else:
        f_out.write(f'{SEQ_NAME_SYMBOL} {SEQ_NAME_GENERIC}\n')
        chars = [x for x in line if x.upper() in IUB_CODES]

    for line in f_in:
        if (line[0] == SEQ_NAME_SYMBOL):
            f_out.write(f"{''.join(chars)}\n")
            return False
        print(f'chars len {len(chars)}')
        new_chars = [x for x in line if x.upper() in IUB_CODES]
        print(f"len new chars: {len(new_chars)}")
        chars.extend(new_chars)
        print(f"len chars extended: {len(chars)}\n")
        print(f'how much lines - len(chars) // LINE_LENGTH {len(chars) // LINE_LENGTH}')
        for i in range(0, len(chars) // LINE_LENGTH):
            f_out.write(''.join(chars[i*LINE_LENGTH:(i + 1) * LINE_LENGTH]))
            f_out.write('\n')
        remains = len(chars) % LINE_LENGTH
        chars = chars[- remains:] if remains > 0 else []
        print(f"len rest chars {len(chars)}\n")
    f_out.write(f"{''.join(chars)}\n")
    return True

# def writeSequence(seq, file):
#     lines_num = (len(sequence) // LINE_LENGTH) + 1 # Number of lines to write the sequence 
#     ll = LINE_LENGTH
#     seq_lines = [seq[i*ll : (i+1)*ll] if (i < lines_num-1) else seq[i*ll : ] for i in range(0, lines_num)]
#     file.write(f"{'\n'.join(seq_lines)}\n")

# postDegreePattern = r'.*(?P<{columnName}>\s({NP}|{R}|{T}|{V})(\.|\s|\Z).*)'\
#     .format(columnName=DEGREE_TMP, NP=degreeNP, R=degreeR, T=degreeT, V=degreeV)
# columns = candidates[NAME_SURNAME].str.extract(postDegreePattern, flags=re.IGNORECASE)

import re
m = re.search('(?<=abc)def', 'abcdef')
m.group(0)
'def'
 
def readFirstLine(line):
    if (line[0] == SEQ_NAME_SYMBOL):
        pattern = f'(?<={SEQ_NAME_SYMBOL}\\s).*(?=\n)'
        name = re.search(pattern, line)
        return name.group(0) if (name is not None) else line[1:-1]
    return None
# return re.findall(pattern, line, flags=re.I | re.DOTALL)
# Using more flags

    # return line  else None

# TODO: what hepens when file does (not) exist? 
def iterSequencesFile(file_name):
    with open(file_name, mode='tr') as f:
        name = None
        seq_chars = []
        for line in f:
            next_name = readFirstLine(line)
            if (not next_name):
                seq_chars.extend([c for c in line if c.upper() in IUB_CODES])
            else:
                yield name, ''.join(seq_chars)
                name = next_name
                seq_chars = []
        yield name, ''.join(seq_chars)


if __name__ == "__main__":
    try:
        path_in, path_out = resolve_arguments()
        print(f'Path in {path_in}, path out: {path_out}')
    except TypeError as e:
        print("Reading of input arguments were unsuccessful.")


    for name, sequence in iterSequencesFile(path_in):
        print(f"name: {name}\nsequence: {sequence}\nsequence length: {len(sequence)}\n")
        writeSequences(sequence)

    # f_out.write(f'{name}\n')
    #     # writeSequence(sequence, f_out)

    # with open(path_in, mode='tr') as f_in, open(path_out, mode='tw') as f_out:
    #     # eof = False
    #     # while(not eof):
        #     eof = readSequence(f_in, f_out)


## FOR CASE, WHERE THE SEQUENCE CAN NOT BE IN MAMORY AT ONCE
## READLINE - WRITELINE - READLINE - WRITELINE (still not safe for oneliner)
# def readSequence(f_in, f_out):
#     line = f_in.readline()
#     if (line[0] == SEQ_NAME_SYMBOL):
#         f_out.write(f'{line}\n')
#         chars = []
#     else:
#         f_out.write(f'{SEQ_NAME_SYMBOL} {SEQ_NAME_GENERIC}\n')
#         chars = [x for x in line if x.upper() in IUB_CODES]

#     for line in f_in:
#         if (line[0] == SEQ_NAME_SYMBOL):
#             f_out.write(f"{''.join(chars)}\n")
#             return False
#         print(f'chars len {len(chars)}')
#         new_chars = [x for x in line if x.upper() in IUB_CODES]
#         print(f"len new chars: {len(new_chars)}")
#         chars.extend(new_chars)
#         print(f"len chars extended: {len(chars)}\n")
#         print(f'how much lines - len(chars) // LINE_LENGTH {len(chars) // LINE_LENGTH}')
#         for i in range(0, len(chars) // LINE_LENGTH):
#             f_out.write(''.join(chars[i*LINE_LENGTH:(i + 1) * LINE_LENGTH]))
#             f_out.write('\n')
#         remains = len(chars) % LINE_LENGTH
#         chars = chars[- remains:] if remains > 0 else []
#         print(f"len rest chars {len(chars)}\n")
#     f_out.write(f"{''.join(chars)}\n")
#     return True
