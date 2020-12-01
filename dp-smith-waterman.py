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
    matrix = np.zeros((len(word01) + 1, len(word02) + 1))
    directions_matrix = np.zeros((len(word01) + 1, len(word02) + 1))

    # DP
    def matrix_score():
        for col in range(1, len(word02) + 1):
            for lin in range(1, len(word01) + 1):
                equality = MATCH_BONUS if (word02[col - 1] == word01[lin - 1]) else MISMATCH_PENALTY
                matrix[lin, col] = max(
                    [0, matrix[lin - 1, col] + GAP_PENALTY, matrix[lin, col - 1] + GAP_PENALTY,
                     matrix[lin - 1, col - 1] + equality])

                directions_matrix[lin, col] = np.argmax(
                    [0, matrix[lin - 1, col] + GAP_PENALTY, matrix[lin, col - 1] + GAP_PENALTY,
                     matrix[lin - 1, col - 1] + equality])

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

    matrix_score()
    return backtrace()


if __name__ == "__main__":
    # Args
    arg_word01, arg_word02 = sys.argv[1].upper(), sys.argv[2].upper()
    print(smith_waterman(arg_word01, arg_word02))
