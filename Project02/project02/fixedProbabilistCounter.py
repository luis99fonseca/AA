import random
import numpy as np


def count(word):
    counter = {}
    for l in word:
        if l not in counter:
            counter[l] = 0
        counter[l] += 1
    return counter


def countProb(word):
    counter = {}
    for l in word:
        if l not in counter:
            counter[l] = 0
        if random.random() < (1 / 16):
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

    print("1/16 Counter:")
    prob16_dict = {}

    for trial in trials:
        prob16_dict = {}
        for i in range(trial):
            v = countProb(t_word)
            # print(v)
            for key in v:
                v[key] *= 16
                if key not in prob16_dict:
                    prob16_dict[key] = [v[key]]
                else:
                    prob16_dict[key].append(v[key])

        print("Trials: ", trial, "; Len: ", word_len)
        headers = ["Letter", "ExpVal", "ExpVar", "ExpStdDev", "Mean-AE", "Mean-RE", "Max-RE", "Min-RE", "Mean-AcR",
                   "SmallVal", "BigVal", "MeanVal", "MAD", "StdDev", "MaxDev", "Var"]
        head = "\t".join(f"{x:>7}" if len(x) < 8 else f"{x:>9}" for x in headers)
        print(head)
        for key in prob16_dict:
            mean = np.mean(prob16_dict[key])
            abs_deviations = np.abs(np.array(prob16_dict[key]) - mean)
            print(f"{key:>7}\t"
                  f"{exact_dict[key]:>7}\t"
                  f"{'???':>7}\t"
                  f"{'???':>9}\t"
        
                  f"{np.mean(np.abs(np.array(prob16_dict[key]) - exact_dict[key])):>7.4}\t"
        
                  f"{np.mean(np.abs(np.array(prob16_dict[key]) - exact_dict[key]) / exact_dict[key]):>7.1%}\t"
                  f"{np.max(np.abs(np.array(prob16_dict[key]) - exact_dict[key]) / exact_dict[key]):>7.1%}\t"
                  f"{np.min(np.abs(np.array(prob16_dict[key]) - exact_dict[key]) / exact_dict[key]):>7.1%}\t"
        
                  f"{np.mean(np.abs(np.array(prob16_dict[key]) / exact_dict[key])):>9.1%}\t"
        
                  f"{np.min(prob16_dict[key]):>8}\t"
                  f"{np.max(prob16_dict[key]):>7}\t"
        
                  f"{mean:>7.1f}\t"
                  f"{np.mean(abs_deviations):>7.4}\t"
                  f"{np.max(abs_deviations):>7.4}\t"
                  f"{np.sqrt(np.mean(np.square(np.array(prob16_dict[key]) - mean))):>7.4}\t"
                  f"{np.mean(np.square(np.array(prob16_dict[key]) - mean)):>7.4}\t"

                  )
