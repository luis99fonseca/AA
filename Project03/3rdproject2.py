import random
import string
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

stream_list = [''.join(random.choice(string.ascii_lowercase)) for _ in range(10000)]

# d = np.random.normal(13, 3, 10000).astype(np.int)
# stream_list = [string.ascii_lowercase[i] for i in d]

for r in range(2):

    if r == 0:
        stream_list = [''.join(random.choice(string.ascii_lowercase)) for _ in range(10000)]
    else:
        d = np.random.normal(13, 3, 10000).astype(np.int)
        stream_list = [string.ascii_lowercase[i] for i in d]

    real_count = Counter(stream_list)
    print(real_count)

    real_count = dict(sorted(real_count.items(), key=lambda item: item[0]))
    plt.bar(real_count.keys(), real_count.values())
    plt.title(("Uniform" if r == 0 else "Normal") + " Distribution" + " Real Count")
    # plt.show()
    plt.savefig(("Uniform" if r == 0 else "Normal") + " Distribution" + " Real Count" + ".png")
    plt.clf()

    for k in range(5, len(string.ascii_lowercase), 5):

        T = {}

        for n in stream_list:
            if n in T:
                T[n] += 1
            elif len(T) < k:
                T[n] = 1
            else:
                j = min(T, key=T.get)
                T[n] = T.pop(j) + 1


        print("Count", dict(sorted(T.items(), key=lambda item: item[0])))

        T = dict(sorted(T.items(), key=lambda item: item[0]))
        plt.bar(T.keys(), T.values())
        plt.plot(T.keys(), [((1/k)*len(stream_list))] * len(T.keys()), c="red")
        plt.title(("Uniform" if r == 0 else "Normal") + " Distribution" + "; k=" + str(k))
        # plt.show()
        plt.savefig(("Uniform" if r == 0 else "Normal") + " Distribution" + "; k=" + str(k) + ".png")
        plt.clf()

