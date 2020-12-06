import sys
import random
from AA.stats_versions import memo_smith_waterman, recur_smith_waterman, dp_smith_waterman
import time

sys.setrecursionlimit(3000)
print(sys.getrecursionlimit())

if __name__ == "__main__":
    alg = sys.argv[1]
    if alg == "dp":
        for i in range(1, 101, 24):
            dp_smith_waterman.basic_operations = 0
            dp_smith_waterman.smith_waterman("".join(random.choice(["A", "C", "G", "T"]) for i in range(i)),
                                             "".join(random.choice(["A", "C", "G", "T"]) for i in range(i)))
            print("bo:", dp_smith_waterman.basic_operations)
            print()
        for i in range(100, 1000, 249):
            dp_smith_waterman.basic_operations = 0
            dp_smith_waterman.smith_waterman("".join(random.choice(["A", "C", "G", "T"]) for i in range(i)),
                                             "".join(random.choice(["A", "C", "G", "T"]) for i in range(i)))
            print("bo:", dp_smith_waterman.basic_operations)
            print()
        for i in range(1000, 7500, 1250):
            dp_smith_waterman.basic_operations = 0
            dp_smith_waterman.smith_waterman("".join(random.choice(["A", "C", "G", "T"]) for i in range(i)),
                                             "".join(random.choice(["A", "C", "G", "T"]) for i in range(i)))
            print("bo:", dp_smith_waterman.basic_operations)
            print()
    elif alg == "memo":
        for i in range(1, 101, 24):
            memo_smith_waterman.basic_operations = 0
            memo_smith_waterman.function_call = 0
            memo_smith_waterman.smith_waterman("".join(random.choice(["A", "C", "G", "T"]) for i in range(i)),
                                             "".join(random.choice(["A", "C", "G", "T"]) for i in range(i)))
            print("bo:", memo_smith_waterman.basic_operations, "fc:", memo_smith_waterman.function_call)
            print()
        for i in range(100, 1000, 249):
            memo_smith_waterman.basic_operations = 0
            memo_smith_waterman.function_call = 0
            memo_smith_waterman.smith_waterman("".join(random.choice(["A", "C", "G", "T"]) for i in range(i)),
                                             "".join(random.choice(["A", "C", "G", "T"]) for i in range(i)))
            print("bo:", memo_smith_waterman.basic_operations, "fc:", memo_smith_waterman.function_call)
            print()
        for i in range(1000, 3000, 1250):
            memo_smith_waterman.basic_operations = 0
            memo_smith_waterman.function_call = 0
            memo_smith_waterman.smith_waterman("".join(random.choice(["A", "C", "G", "T"]) for i in range(i)),
                                             "".join(random.choice(["A", "C", "G", "T"]) for i in range(i)))
            print("bo:", memo_smith_waterman.basic_operations, "fc:", memo_smith_waterman.function_call)
            print()
    elif alg == "recur":
        for i in range(1, 12, 2):
            print("lines:", i + 1, "| cols:", i + 1)
            recur_smith_waterman.basic_operations = 0
            recur_smith_waterman.function_call = 0
            initial_time = time.time()
            recur_smith_waterman.smith_waterman("".join(random.choice(["A", "C", "G", "T"]) for i in range(i)),
                                               "".join(random.choice(["A", "C", "G", "T"]) for i in range(i)), i, i)
            final_time = time.time()
            print("total.", final_time - initial_time)
            print("bo:", recur_smith_waterman.basic_operations, "fc:", recur_smith_waterman.function_call)
            print()
    elif alg == "small_memo":
        for i in range(1, 12, 2):
            print("lines:", i + 1, "| cols:", i + 1)
            memo_smith_waterman.basic_operations = 0
            memo_smith_waterman.function_call = 0
            memo_smith_waterman.smith_waterman("".join(random.choice(["A", "C", "G", "T"]) for i in range(i)),
                                               "".join(random.choice(["A", "C", "G", "T"]) for i in range(i)))
            print("bo:", memo_smith_waterman.basic_operations, "fc:", memo_smith_waterman.function_call)
            print()
