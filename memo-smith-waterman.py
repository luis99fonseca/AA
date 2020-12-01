import numpy as np
import sys

# Consts
## Directions
NONE = 0
UP = 1
LEFT = 2
DIAGONAL = 3

## Points
GAP_PENALTY = -2
MATCH_BONUS = 2
MISMATCH_PENALTY = -1


def smith_waterman(word01, word02):
    print("lines:", len(word01) + 1, "| cols:", len(word02) + 1)
    matrix = np.ones((len(word01) + 1, len(word02) + 1)) * -1
    matrix[0, :] = 0
    matrix[:, 0] = 0
    directions_matrix = np.zeros((len(word01) + 1, len(word02) + 1))

    def matrix_score(x, y):
        if matrix[x, y] != -1:
            return matrix[x, y]

        eq = (MATCH_BONUS if (word02[y - 1] == word01[x - 1]) else MISMATCH_PENALTY)

        v_up = matrix_score(x - 1, y) + GAP_PENALTY
        v_left = matrix_score(x, y - 1) + GAP_PENALTY
        v_diagonal = matrix_score(x - 1, y - 1) + eq

        directions_matrix[x, y] = np.argmax([0, v_up, v_left, v_diagonal])
        matrix[x, y] = max(0, v_up, v_left, v_diagonal)
        return matrix[x, y]

    # TraceBack
    def backtrace():
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
        return intersection_word01[::-1], intersection_word02[::-1]

    matrix_score(len(word01), len(word02))
    return backtrace()

if __name__ == "__main__":
    # Args
    arg_word01, arg_word02 = sys.argv[1].upper(), sys.argv[2].upper()
    print(smith_waterman(arg_word01, arg_word02))
