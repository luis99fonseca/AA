import numpy as np
from constants import *


# TraceBack
def backtrace(matrix, directions_matrix, word01, word02):
    final_lin, final_col = np.argmax(matrix) // (len(word02) + 1), np.argmax(matrix) % (len(word02) + 1)
    intersection_word01 = ""
    intersection_word02 = ""
    actual_dir = directions_matrix[final_lin, final_col]
    while actual_dir != NONE:
        if actual_dir == UP:
            final_lin -= 1
            intersection_word01 += word01[final_lin]
            intersection_word02 += "_"
        elif actual_dir == LEFT:
            final_col -= 1
            intersection_word01 += "_"
            intersection_word02 += word02[final_col]
        elif actual_dir == DIAGONAL:
            final_lin -= 1
            final_col -= 1
            intersection_word01 += word01[final_lin]
            intersection_word02 += word02[final_col]
        actual_dir = directions_matrix[final_lin, final_col]
    return intersection_word01[::-1], intersection_word02[::-1], np.max(matrix)
