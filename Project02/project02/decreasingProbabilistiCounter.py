import random
import numpy as np


def count(word):
    counter = {}
    for l in word:
        if l not in counter:
            counter[l] = 0
        counter[l] += 1
    return counter


def countLog(word):
    counter = {}
    for l in word:
        if l not in counter:
            counter[l] = 0
        if random.random() < (1 / (2 ** counter[l])):
            counter[l] += 1
    return counter


trials = [10000] #[10, 100, 1000, 10000, 100000, 1000000]
words_len = [10000000] #[10, 100, 1000, 10000, 100000, 1000000]

for word_len in words_len:
    word = "luiscarlosduartefonseca"
    splitted_word = [c for c in word]
    t_word = "".join([random.choice(splitted_word) for i in range(word_len)])

    print("Exact Counter:")
    exact_dict = count(t_word)
    print(exact_dict)

    print("Log2 Counter:")
    log2_dict = {}
    log2_exact_dict = {}

    for trial in trials:
        log2_dict = {}
        for i in range(trial):
            v = countLog(t_word)
            # print(v)
            for key in v:
                if key not in log2_exact_dict:
                    log2_exact_dict[key] = [v[key]]
                else:
                    log2_exact_dict[key].append(v[key])
                v[key] = (2 ** v[key] - 2 + 1) / (2 - 1)
                if key not in log2_dict:
                    log2_dict[key] = [v[key]]
                else:
                    log2_dict[key].append(v[key])

        print("Trials: ", trial, "; Len: ", word_len)

        headers = ["Letter", "ExpVal", "ExpVar", "ExpStdDev", "Mean-AE", "Mean-RE", "Max-RE", "Min-RE", "Mean-AcR",
                   "SmallVal", "BigVal", "RealVal", "MeanVal", "MAD", "StdDev", "MaxDev", "Var"]
        head = "\t".join(f"{x:>7}" if len(x) < 8 else f"{x:>9}" for x in headers)
        print(head)
        for key in log2_dict:
            # print(log2_exact_dict[key])
            mean = np.mean(log2_dict[key])
            abs_deviations = np.abs(np.array(log2_dict[key]) - mean)
            print(f"{key:>7}\t"
                  f"{exact_dict[key]:>7}\t"
                  f"{'???':>7}\t"
                  f"{'???':>9}\t"
    
                  f"{np.mean(np.abs(np.array(log2_dict[key]) - exact_dict[key])):>7.4}\t"
    
                  f"{np.mean(np.abs(np.array(log2_dict[key]) - exact_dict[key]) / exact_dict[key]):>7.1%}\t"
                  f"{np.max(np.abs(np.array(log2_dict[key]) - exact_dict[key]) / exact_dict[key]):>7.1%}\t"
                  f"{np.min(np.abs(np.array(log2_dict[key]) - exact_dict[key]) / exact_dict[key]):>7.1%}\t"
    
                  f"{np.mean(np.abs(np.array(log2_dict[key]) / exact_dict[key])):>9.1%}\t"
    
                  f"{np.min(log2_dict[key]):>8}\t"
                  f"{np.max(log2_dict[key]):>7}\t"
                  f"{log2_exact_dict[key][0]:>7}\t"
                    
                  f"{mean:>7.1f}\t"
                  f"{np.mean(abs_deviations):>7.4}\t"
                  f"{np.max(abs_deviations):>7.4}\t"
                  f"{np.sqrt(np.mean(np.square(np.array(log2_dict[key]) - mean))):>7.4}\t"
                  f"{np.mean(np.square(np.array(log2_dict[key]) - mean)):>7.4}\t"

                  )
