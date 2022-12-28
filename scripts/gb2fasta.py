import os
import sys

from Bio import SeqIO
import tqdm

N = 10000

i = 1
seqs = []
path = sys.argv[1]
outdir = sys.argv[2]



def write_seqs(seqs):
    with open(os.path.join(outdir, f"{i}.fasta"), "w") as fout:
        SeqIO.write(seqs, fout, "fasta")


for rec in tqdm.tqdm(SeqIO.parse(path, format="gb")):
    seqs.append(rec)

    if len(seqs) == N:
        write_seqs(seqs)
        seqs = []
        i += 1
    
if len(seqs):
    write_seqs(seqs)
