import numpy as np
import sys
from constants import *
from backtrace import backtrace
import time

basic_operations = 0
function_call = 0

def smith_waterman(word01, word02):
    print("lines:", len(word01) + 1, "| cols:", len(word02) + 1)
    matrix = np.ones((len(word01) + 1, len(word02) + 1)) * -1
    matrix[0, :] = 0
    matrix[:, 0] = 0
    directions_matrix = np.zeros((len(word01) + 1, len(word02) + 1))
    initial_time = time.time()
    calc_matrix_scores(matrix, directions_matrix, word01, word02, len(word01), len(word02))
    mid_time = time.time()
    val = backtrace(matrix, directions_matrix, word01, word02)
    final_time = time.time()
    print("Scoring:", mid_time - initial_time, "backtrace:", final_time - mid_time, "total:", final_time - initial_time)
    return val


def calc_matrix_scores(matrix, directions_matrix, word01, word02, x, y):
    global function_call
    function_call += 1
    if matrix[x, y] != -1:
        return matrix[x, y]

    global basic_operations
    basic_operations += 3

    eq = (MATCH_BONUS if (word02[y - 1] == word01[x - 1]) else MISMATCH_PENALTY)
    v_diagonal = calc_matrix_scores(matrix, directions_matrix, word01, word02, x - 1, y - 1) + eq
    v_up = calc_matrix_scores(matrix, directions_matrix, word01, word02, x - 1, y) + GAP_PENALTY
    v_left = calc_matrix_scores(matrix, directions_matrix, word01, word02, x, y - 1) + GAP_PENALTY

    directions_matrix[x, y] = np.argmax([0, v_up, v_left, v_diagonal])
    matrix[x, y] = max(0, v_up, v_left, v_diagonal)
    return matrix[x, y]


if __name__ == "__main__":
    # Args
    arg_word01, arg_word02 = sys.argv[1].upper(), sys.argv[2].upper()
    print(smith_waterman(arg_word01, arg_word02))
    print(basic_operations, function_call)
