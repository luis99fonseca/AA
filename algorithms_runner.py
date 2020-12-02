import sys
import random
import dp_smith_waterman
import memo_smith_waterman
import recur_smith_waterman

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
