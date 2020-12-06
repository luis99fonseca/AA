import sys
from constants import *


def smith_waterman(word01, word02, x, y):
    if x == 0 or y == 0:
        return 0, 0

    eq = (MATCH_BONUS if (word02[y - 1] == word01[x - 1]) else MISMATCH_PENALTY)

    v_up = smith_waterman(word01, word02, x - 1, y)
    v_left = smith_waterman(word01, word02, x, y - 1)
    v_diagonal = smith_waterman(word01, word02, x - 1, y - 1)

    local_max_score = max(0, v_up[0] + GAP_PENALTY, v_left[0] + GAP_PENALTY, v_diagonal[0] + eq)
    return local_max_score, max(local_max_score, v_up[1], v_left[1], v_diagonal[1])


if __name__ == "__main__":
    # Args
    arg_word01, arg_word02 = sys.argv[1].upper(), sys.argv[2].upper()
    print(" 1st element - score of element at len(arg1),len(arg2) \n 2nd element - max score of algorithm")
    print(smith_waterman(arg_word01, arg_word02, len(arg_word01), len(arg_word02)))

