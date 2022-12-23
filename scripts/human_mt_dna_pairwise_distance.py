from multiprocessing import Pool

from Bio import SeqIO
import Levenshtein
import numpy as np
import matplotlib.pyplot as plt
import tqdm

path_to_genbank = "./data/external/human_mt_clean.gb"
dloops = []
npassed = nexdloop = 0
for i, rec in tqdm.tqdm(enumerate(SeqIO.parse(path_to_genbank, format="gb")), total=60000):
    feature_dloop = [x for x in rec.features if x.type == "D-loop"]
    if len(feature_dloop) == 1:
        cur_dloop = str(feature_dloop[0].extract(rec.seq)).upper()
        amb_share = 1 - sum([cur_dloop.count(x) for x in "ACGT"]) / len(cur_dloop)
        if amb_share > 0.05:
            npassed += 1
            continue
        dloops.append((rec.id, cur_dloop))
    else:
        nexdloop += 1
print(len(dloops), npassed, nexdloop)


dloops_clean = [x for x in dloops if len(x[1]) < 1300 and len(x[1]) > 1100]
n = len(dloops_clean)
# n = 1000
data = []


def get_distance(x):
    i, j = x
    d = Levenshtein.distance(dloops_clean[i][1], dloops_clean[j][1])
    return d


def get_iterator():
    for i in range(n):
        for j in range(i + 1, n):
            yield (i, j)

print("Start computing")
with Pool(24) as p:
    ds = p.map(get_distance, get_iterator())
print("Computing done")

dists = np.array(ds)
np.save("./data/dloop_pairwise_dists.npy", dists)

plt.figure(figsize=(12, 4))
plt.hist(dists, 50)
plt.title(f"Pairwise D-loop distance, {len(dloops)} genomes")
plt.xlabel("Distance")
plt.ylabel("Count")
plt.savefig("./figures/dloop/dists.png")

plt.figure(figsize=(12, 4))
plt.hist(dists, 50, (0, 200))
plt.title(f"Pairwise D-loop distance, {len(dloops)} genomes")
plt.xlabel("Distance")
plt.ylabel("Count")
plt.savefig("./figures/dloop/dists200.png")
