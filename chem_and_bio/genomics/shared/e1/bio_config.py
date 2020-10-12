#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name:   Bioinformatic configuration
Author: Jaroslav Langer (langera@vscht.cz)
Description:
    Module where all the bioinformatic and other constants are set (e.g. LINE_LENGTH).
"""
LINE_LENGTH = 100 # Newline character is not included i.e. for width 80 write 79
SEQ_NAME_GENERIC = "Unknown sequence"
SEQ_NAME_START = '>'
STOP = '*'
CODON_LEN = 3

DNA,    RNA,   AA,   ADENINE,   CYTOSINE,   GUANINE,   THYMINE,   URACIL =\
'DNA', 'RNA', 'AA', 'adenine', 'cytosine', 'guanine', 'thymine', 'uracil'

A,    C,   G,   T,   U,   A_G, C_T, C_G, A_T, G_T, A_C, C_G_T, A_G_T, A_C_T, A_C_G, A_C_G_T, GAP_1, GAP_2 =\
'A', 'C', 'G', 'T', 'U', 'R', 'Y', 'S', 'W', 'K', 'M', 'B',   'D',   'H',   'V',   'N',     '-',   '.'

ALA, ASX, CYS, ASP, GLU, PHE, GLY, HIS, ILE, LYS, LEU, MET, ASN, PRO, GLN, ARG, SER, THR, VAL, TRP, XAA, TYR, GLX =\
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'

OTHER,    GAP,   NONPOLAR,   POLAR_UNCHARGED,   ACIDIC,   BASIC =\
'other', 'gap', 'nonpolar', 'polar_uncharged', 'acidic', 'basic'

COMPLEMENTS = {
    A: T, C: G, G: C, T: A, A_G: C_T, C_T: A_G, G_T: A_C, A_C: G_T, C_G: C_G, A_T: A_T,
    C_G_T: A_C_G, A_G_T: A_C_T, A_C_T: A_G_T, A_C_G: C_G_T, A_C_G_T: A_C_G_T, GAP_1: GAP_1, GAP_2: GAP_2,
}
GROUPS = {
    DNA: {
        ADENINE: [A], CYTOSINE: [C], GUANINE: [G], THYMINE: [T], 
        OTHER: [A_G, C_T, C_G, A_T, G_T, A_C, C_G_T, A_G_T, A_C_T, A_C_G, A_C_G_T], 
        GAP: [GAP_1, GAP_2],
    },
    RNA: {
        ADENINE: [A], CYTOSINE: [C], GUANINE: [G], URACIL: [U], 
        OTHER: [A_G, C_T, C_G, A_T, G_T, A_C, C_G_T, A_G_T, A_C_T, A_C_G, A_C_G_T], 
        GAP: [GAP_1, GAP_2],
    },
    AA: {
        NONPOLAR: [GLY, ALA, VAL, LEU, ILE, PRO, PHE, MET, TRP],
        POLAR_UNCHARGED: [SER, CYS, THR, TYR, ASN, GLN],
        ACIDIC: [ASP, GLU],
        BASIC: [ARG, HIS, LYS],
        OTHER: [ASX, GLX, XAA],
    },
}
IUB_CODES = {
    DNA: [code for group in GROUPS[DNA].values() for code in group],
    AA: [code for group in GROUPS[AA].values() for code in group],
}
CODONS = {
    T: {
        T: {T: PHE, C: PHE, C_T: PHE,               # phenylalanine
            A: LEU, G: LEU, A_G: LEU,},             # leucine
        C: {code: SER for code in IUB_CODES[DNA]},  # serine
        A: {T: TYR, C: TYR, C_T: TYR,               # tyrosine
            A: STOP, G: STOP, A_G: STOP},           # stop codon (Ochre, Amber)
        G: {T: CYS, C: CYS, C_T: CYS,               # cysteine
            A: STOP,                                # stop codon (Opal)
            G: TRP},                                # tryptophan
        },
    C: {
        T: {code: LEU for code in IUB_CODES[DNA]},  # leucine
        C: {code: PRO for code in IUB_CODES[DNA]},  # proline
        A: {T: HIS, C: HIS, C_T: HIS,               # histidine
            A: GLN, G: GLN, A_G: GLN,},             # glutamine
        G: {code: ARG for code in IUB_CODES[DNA]},  # arginine
        },
    A: {
        T: {T: ILE, C: ILE, A: ILE, A_C: ILE, A_T: ILE, C_T: ILE, A_C_T: ILE, # isoleucine
            G: MET},                                # methionine
        C: {code: THR for code in IUB_CODES[DNA]},  # threonine
        A: {T: ASN, C: ASN, C_T: ASN,               # asparagine
            A: LYS, G: LYS, A_G: LYS,},             # lysine
        G: {T: SER, C: SER, C_T: SER,               # serine 
            A: ARG, G: ARG, A_G: ARG,},             # arginine
        },
    G: {
        T: {code: VAL for code in IUB_CODES[DNA]},  # valine
        C: {code: ALA for code in IUB_CODES[DNA]},  # alanine
        A: {T: ASP, C: ASP, C_T: ASP,               # asparatic acid
            A: GLU, G: GLU, A_G: GLU,},             # glutamic acid
        G: {code: GLY for code in IUB_CODES[DNA]},  # glycine
        },
}
