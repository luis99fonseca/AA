import random
import string
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

stream_list = [''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 50))) for i in range(2)]

stream_list = [''.join(random.choice(string.ascii_lowercase)) for _ in range(10000)]

# d = np.random.normal(13, 3, 10000).astype(np.int)
# stream_list = [string.ascii_lowercase[i] for i in d]
#stream_list = ['a', 'a', 'a', 'b', 'b', 'c', 'a']
#stream_list = ['o', 'm', 'o', 'm', 'n', 'o', 'n', 'n', 'l', 'o']
# print(stream_list)
# print(stream_list[-1])

for r in range(1):
    T = {}
    # k = 5
    count = 0
    for k in range(5, len(string.ascii_lowercase) + 1, 5):
        for n in stream_list:
            count += 1
            # print("At: ", n)
            if n in T:
                T[n] += 1
            elif len(T) < k:
                T[n] = 1
            else:
                j = min(T, key=T.get)
                # print("Removing: ", j, " to add: ", n, " Count: ", T[j])
                T[n] = T.pop(j) + 1

        real_count = Counter(stream_list)
        print(real_count)
        print("Count", dict(sorted(T.items(), key=lambda item: -item[1])))

        plt.bar(real_count.keys(), real_count.values())
        plt.title(("Uniform" if r == 0 else "Normal") + " Distribution" + " Real Count")
        plt.show()

        plt.bar(T.keys(), T.values())
        plt.title(("Uniform" if r == 0 else "Normal") + " Distribution" + "; k=" + str(k))
        plt.show()
    # plt.savefig("ola.png")
