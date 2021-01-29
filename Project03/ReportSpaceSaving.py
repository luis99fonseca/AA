import random
import string
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

for r in range(2):
    # if r == 0:
    #     continue

    for size in [100, 1000, 10000, 100000, 1000000, 10000000]:
        if r == 0:
            stream_list = [''.join(random.choice(string.ascii_lowercase)) for _ in range(size)]
        else:
            d = np.random.normal(13, 4.5, size).astype(np.int)
            stream_list = [string.ascii_lowercase[i] if i >= 0 and i < len(string.ascii_lowercase) else
                           random.choice(
                string.ascii_lowercase) for i in d]

        with open(str(size) + "-" + ("Uniform" if r == 0 else "Normal") + " Distribution" + ".txt", "w") as file01:
            for s in stream_list:
                file01.write(s)

        real_count = Counter(stream_list)
        print(real_count)

        real_count = dict(sorted(real_count.items(), key=lambda item: item[0]))
        plt.bar(real_count.keys(), real_count.values())

        colors = ["orange", "g", "r", "purple", "y"]
        cc = 0
        for k in range(5, len(string.ascii_lowercase), 5):
            plt.plot(real_count.keys(), [((1 / k) * len(stream_list))] * len(real_count.keys()), label="k=" + str(k),
                     c=colors[cc])
            cc += 1
            plt.legend()
        plt.title(("Uniform" if r == 0 else "Normal") + " Distribution" + " Real Count")
        # plt.show()
        plt.savefig("results/" + str(size) + "-" + ("Uniform" if r == 0 else "Normal") + " Distribution" + " Real Count" + ".png")
        plt.clf()

        cc = 0
        precision_dict = []
        recall_dict = []
        for k in range(5, len(string.ascii_lowercase), 5):

            # Algorithm
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

            frequent_threshold = ((1 / k) * len(stream_list))

            plt.plot(T.keys(), [frequent_threshold] * len(T.keys()), c=colors[cc])
            cc += 1
            plt.title(("Uniform" if r == 0 else "Normal") + " Distribution" + "; k=" + str(k))
            # plt.show()
            plt.savefig("results/" + str(size) + "-" + ("Uniform" if r == 0 else "Normal") + " Distribution" + "; k=" + str(k) + ".png")
            plt.clf()

            frequent_items = dict(filter(lambda e: e[1] > frequent_threshold, real_count.items()))
            precision_dict.append(
                len(dict(filter(lambda e: e[0] in frequent_items, T.items()))) / len(T)
            )
            recall_dict.append(
                len(dict(filter(lambda e: e[0] in frequent_items, T.items()))) / len(frequent_items) if len(
                    frequent_items) > 0 else None
            )

        print(precision_dict)
        print(recall_dict)
        plt.plot([kl for kl in range(5, len(string.ascii_lowercase), 5)], precision_dict, marker="o", label="precision")
        plt.plot([kl for kl in range(5, len(string.ascii_lowercase), 5)], recall_dict, marker="D", label="recall")
        plt.legend()
        plt.xlabel("k")
        plt.title("Metrics in function of k")
        plt.savefig(
            "results/" + str(size) + "-" + ("Uniform" if r == 0 else "Normal") + " Distribution" + "- Metrics in function of k" + ".png")
        plt.clf()
