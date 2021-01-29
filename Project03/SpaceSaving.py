import string
from collections import Counter
import matplotlib.pyplot as plt
import sys


def spaceSaving(file_name):
    with open(file_name, "r") as file01:
        stream_list = list(file01.readline())

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
        plt.title("Real Count")
        plt.show()
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
            plt.title("Distribution" + "; k=" + str(k))
            plt.show()
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
        plt.show()
        plt.clf()

# runs as 'python3 SpaceSaving <file>', example for <file>: 100-Normal\ Distribution.txt
if __name__ == '__main__':
    spaceSaving(sys.argv[1])
