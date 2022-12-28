import os
import sys
from Bio import SeqIO

N = 100

i = 1
seqs = []
path = sys.argv[1]
for rec in SeqIO.parse(path, format="fasta"):
    seqs.append(rec)

    if len(seqs) == N:
        with open(os.path.join(os.path.dirname(path), f"chunks/{i}.fasta"), "w") as fout:
            SeqIO.write(seqs, fout, "fasta")
        seqs = []
        i += 1
    
if len(seqs):
    with open(os.path.join(os.path.dirname(path), f"chunks/{i}.fasta"), "w") as fout:
        SeqIO.write(seqs, fout, "fasta")