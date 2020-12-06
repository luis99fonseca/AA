import numpy as np
import sys
from constants import *
from backtrace import backtrace


def smith_waterman(word01, word02):
    print("lines:", len(word01) + 1, "| cols:", len(word02) + 1)
    matrix = np.zeros((len(word01) + 1, len(word02) + 1))
    directions_matrix = np.zeros((len(word01) + 1, len(word02) + 1))

    calc_matrix_scores(matrix, directions_matrix, word01, word02)
    return backtrace(matrix, directions_matrix, word01, word02)


# DP
def calc_matrix_scores(matrix, directions_matrix, word01, word02):
    for col in range(1, len(word02) + 1):
        for lin in range(1, len(word01) + 1):
            equality = MATCH_BONUS if (word02[col - 1] == word01[lin - 1]) else MISMATCH_PENALTY
            v_up = matrix[lin - 1, col] + GAP_PENALTY
            v_left = matrix[lin, col - 1] + GAP_PENALTY
            v_diagonal = matrix[lin - 1, col - 1] + equality

            matrix[lin, col] = max([0, v_up, v_left, v_diagonal])
            directions_matrix[lin, col] = np.argmax([0, v_up, v_left, v_diagonal])


if __name__ == "__main__":
    # Args
    arg_word01, arg_word02 = sys.argv[1].upper(), sys.argv[2].upper()
    print(smith_waterman(arg_word01, arg_word02))