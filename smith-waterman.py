import numpy as np
import sys

# Consts
NONE = 0
UP = 1
LEFT = 2
DIAGONAL = 3
DIRS = [NONE, UP, LEFT, DIAGONAL] # todo: not used

# Args
word01 = sys.argv[1]
word02 = sys.argv[2]

# Points
gap_penalty = -2
match_bonus = 2
mismatch_penalty = -1

print("lines: ", len(word01) + 1, "; cols: ", len(word02) + 1)
matrix = np.zeros((len(word01) + 1, len(word02) + 1))
directions_matrix = np.zeros((len(word01) + 1, len(word02) + 1))

## DP
def dinamic_programing():
    for col in range(1, len(word02) + 1):
        for lin in range(1, len(word01) + 1):
            equality = match_bonus if (word02[col - 1] == word01[lin - 1]) else mismatch_penalty
            matrix[lin, col] = (max(
                [0, matrix[lin - 1, col] + gap_penalty, matrix[lin, col - 1] + gap_penalty, matrix[lin - 1, col - 1] + equality])
            )
            directions_matrix[lin, col] = np.argmax([0, matrix[lin - 1, col] + gap_penalty, matrix[lin, col - 1] + gap_penalty, matrix[lin - 1, col - 1] + equality])

print(matrix)
print(directions_matrix)

## TraceBack
def backtrace():
    final_lin, final_col = np.argmax(matrix) // (len(word02) + 1), np.argmax(matrix) % (len(word02) + 1)

    intersection_string = ""
    intersection_string2 = ""
    actual_dir = directions_matrix[final_lin, final_col]
    while actual_dir != NONE:
        print(final_lin, final_col)
        if actual_dir == UP:
            intersection_string += word01[final_lin - 1]
            intersection_string2 += "_"
            final_lin -= 1
        elif actual_dir == LEFT:
            intersection_string += "_"
            intersection_string2 += word02[final_col - 1]
            final_col -= 1
        elif actual_dir == DIAGONAL:
            intersection_string += word01[final_lin - 1]
            intersection_string2 += word02[final_col - 1]
            final_lin -= 1
            final_col -= 1
        actual_dir = directions_matrix[final_lin, final_col]

    print(intersection_string[::-1], intersection_string2[::-1])

dinamic_programing()
backtrace()
print("max: ", np.max(matrix))
print(matrix)
print(directions_matrix)