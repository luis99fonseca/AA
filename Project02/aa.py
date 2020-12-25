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


def countLog(word):
    counter = {}
    for l in word:
        if l not in counter:
            counter[l] = 0
        if random.random() < (1 / (2 ** counter[l])):
            counter[l] += 1
    return counter


trials = 5
word_len = 50

t_word = "".join([random.choice(["a", "c", "b"]) for i in range(word_len)])

print("Exact Counter:")
exact_dict = count(t_word)
print(exact_dict)

print("1/16 Counter:")
prob16_dict = {}

for i in range(trials):
    v = countProb(t_word)
    # print(v)
    for key in v:
        v[key] *= 16
        if key not in prob16_dict:
            prob16_dict[key] = [v[key]]
        else:
            prob16_dict[key].append(v[key])

if True:
    for key in prob16_dict:
        print("Letter: ", key)
        print("all: ", prob16_dict[key])
        print("Expected value: ", exact_dict[key])
        print("Variance: (?)", "?")
        print("𝑠𝑡𝑑𝑑𝑒𝑣: ", np.sqrt(exact_dict[key]) / 2)

        print()

        print("--Errors: ", np.abs(np.array(prob16_dict[key]) - exact_dict[key]))
        print("  MeanAE: ", np.mean(np.abs(np.array(prob16_dict[key]) - exact_dict[key])))
        print("  MeanRE: ", np.mean(np.abs(np.array(prob16_dict[key]) - exact_dict[key]) / exact_dict[key] )  * 100 )
        print("  MeanRE: ", np.mean(np.abs((np.array(prob16_dict[key]) - exact_dict[key]) / exact_dict[key] )   ) * 100 )
        print("  MaxRE: ", np.max( np.abs((np.array(prob16_dict[key]) - exact_dict[key]) / exact_dict[key] )   ) * 100 )
        print("  MinRE: ", np.min( np.abs((np.array(prob16_dict[key]) - exact_dict[key]) / exact_dict[key] )   ) * 100 )

        print("  MaxRE: ", np.max( np.abs(np.array(prob16_dict[key]) - exact_dict[key]) / exact_dict[key] )    * 100 )
        print("  MinRE: ", np.min( np.abs(np.array(prob16_dict[key]) - exact_dict[key]) / exact_dict[key] )    * 100 )


        print()

        print("smallest counter value:", np.min(prob16_dict[key]))
        print("largest counter value:", np.max(prob16_dict[key]))

        print()

        mean = np.mean(prob16_dict[key])
        print("--Mean: ", mean)
        print("--Deviation")
        abs_deviations = np.abs(np.array(prob16_dict[key]) - mean)
        print("  All DEVS: ", abs_deviations)
        print("  𝑚𝑎𝑑: ", np.mean(abs_deviations))
        print("  𝑚𝑎𝑥𝑑𝑒𝑣: ", np.max(abs_deviations))
        print("  𝑠𝑡𝑑𝑑𝑒𝑣: ", np.sqrt(np.mean(np.square(np.array(prob16_dict[key]) - mean))) )
        print("  𝓋𝒶𝓇𝒾𝒶𝓃𝒸𝑒: ", np.mean(np.square(np.array(prob16_dict[key]) - mean)))

        print()
if True:
    headers = ["Letter", "ExpVal", "ExpVar", "ExpStdDev", "Mean-AR", "Mean-RE", "Max-RE", "Min-RE", "SmallVal", "BigVal", "MeanVal", "MAD", "StdDev", "MaxDev", "Var"]
    head = "\t".join(f"{x:>7}" if len(x) < 8 else f"{x:>9}" for x in headers )
    print(head)
    for key in prob16_dict:
        mean = np.mean(prob16_dict[key])
        abs_deviations = np.abs(np.array(prob16_dict[key]) - mean)
        print(f"{key:>7}\t"
              f"{exact_dict[key]:>7}\t"
              f"{'???':>7}\t"
              f"{'???':>9}\t"
              
              f"{np.mean(np.abs(np.array(prob16_dict[key]) - exact_dict[key])):>7.4}\t"

              f"{np.mean( np.abs(np.array(prob16_dict[key]) - exact_dict[key]) / exact_dict[key] ):>7.1%}\t"
              f"{np.max( np.abs(np.array(prob16_dict[key]) - exact_dict[key]) / exact_dict[key] ):>7.1%}\t"
              f"{np.min( np.abs(np.array(prob16_dict[key]) - exact_dict[key]) / exact_dict[key] ):>7.1%}\t"
              
              f"{np.min(prob16_dict[key]):>8}\t"
              f"{np.max(prob16_dict[key]):>7}\t"

              f"{mean:>7}\t"
              f"{np.mean(abs_deviations):>7.4}\t"
              f"{np.max(abs_deviations):>7.4}\t"
              f"{np.sqrt(np.mean(np.square(np.array(prob16_dict[key]) - mean))):>7.4}\t"
              f"{np.mean(np.square(np.array(prob16_dict[key]) - mean)):>7.4}\t"

              )


# print("Log2 Counter:")
# for i in range(10):
#     print(countLog(t_word))
# c = countLog(t_word)["c"]
# print((2 ** c - 2 + 1) / (2 - 1))
