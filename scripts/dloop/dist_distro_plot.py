import numpy as np
import matplotlib.pyplot as plt

N = 55180

# dd = np.random.randn(1000000) * 10 + 24
# dd = np.concatenate([dd, np.random.randn(200000) * 10 + 624])
dd = np.load("./data/dloop_pairwise_dists.npy")
dd = dd[np.where(dd > 0)]


font = {
    'family': 'Arial',
    'color':  'black',
    'weight': 'normal',
    'size': 15,
}


def get_yticks_labels(a):
    l = []
    for x in a:
        x = str(int(x))
        if len(x) > 4:
            y = ""
            for i, s in enumerate(x[::-1], 1):
                y += s
                if i % 3 == 0:
                    y += ","
            x = y.strip(",")[::-1]
        l.append(x)
    return l


# fig = plt.figure(figsize=(12, 4))
# plt.grid(axis="y")
# ax = fig.axes[0]
# ax.set_axisbelow(True)
# plt.hist(dd, 50, color="dimgrey", edgecolor="white")

# ticks = ax.get_yticks()
# yt_labels = get_yticks_labels(ticks)
# print(ticks)
# print(yt_labels)

# plt.yticks(ticks, yt_labels)
# plt.xlabel("Difference in D-loop, nt", fontdict=font)
# plt.ylabel("Number of D-loop pairs", fontdict=font)
# plt.show()
# plt.savefig("./figures/dloop/dists.png")


fig, (ax, ax2) = plt.subplots(1, 2, sharex=False, sharey=False, facecolor='w')
fig.set_size_inches(12, 6)
ax.hist(dd, 100, color="dimgrey", edgecolor="white")
ax2.hist(dd, 100, color="dimgrey", edgecolor="white")

ax.set_xlim(0, 75)
ax2.set_xlim(585, 700)

ax.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.yaxis.set_visible(False)

d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((1-d, 1+d), (-d, +d), **kwargs)
ax.plot((1-d, 1+d), (1-d, 1+d), **kwargs)

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1-d, 1+d), **kwargs)
ax2.plot((-d, +d), (-d, +d), **kwargs)


ticks = ax.get_yticks()
yt_labels = get_yticks_labels(ticks)
ax.set_yticks(ticks, yt_labels)

ax.set_xlabel("Difference in D-loop, nt", fontdict=font, loc="right")
ax.set_ylabel("Number of D-loop pairs", fontdict=font)
# plt.show()
plt.savefig("./figures/dloop/dists.png")
