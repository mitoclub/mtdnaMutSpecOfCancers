import os
import sys
from collections import defaultdict
from functools import partial, reduce

import numpy as np
import pandas as pd
from Bio import SeqIO

from mutspec.annotation import CodonAnnotation
from mutspec.io import read_genbank_ref

PATH_TO_SEQS = "./data/external/NC_012920.1.gb"

coda = CodonAnnotation(2)


def get_alt_codon(cdn, pic, alt_nuc):
    if not isinstance(cdn, str):
        return cdn
    assert pic in {1,2,3}
    
    alt_cdn = list(cdn)
    alt_cdn[pic - 1] = alt_nuc
    return "".join(alt_cdn)


for record in SeqIO.parse(PATH_TO_SEQS, format="gb"):
    genome = read_genbank_ref(record)
    genome = genome[~genome["Context"].isna()]
    genome["AltNuc"] = genome.Nuc.apply(lambda x: [y for y in "ACGT" if y != x])
    genome = genome.explode("AltNuc", ignore_index=True)
    genome["MutBase"] = genome.Nuc + ">" + genome.AltNuc
    genome["Mut"] = genome.Context.str.get(0) + "[" + genome["MutBase"] + "]" + genome.Context.str.get(-1)
    genome["AltCodon"] = genome.apply(lambda x: get_alt_codon(x.Codon, x.PosInCodon, x.AltNuc), axis=1)
    genome["Label"] = genome.apply(lambda x: coda.get_mut_type(x.Codon, x.AltCodon, x.PosInCodon - 1)[0], axis=1)

    a = 1