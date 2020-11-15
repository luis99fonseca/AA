import numpy as np
import sys

# Consts
NONE = 0
UP = 1
LEFT = 2
DIAGONAL = 3
DIRS = [NONE, UP, LEFT, DIAGONAL]

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

## DP (?)
for col in range(1, len(word02) + 1):
    for lin in range(1, len(word01) + 1):
        inq = match_bonus if (word02[col - 1] == word01[lin - 1]) else mismatch_penalty
        # equality = (word02[col - 1] == word01[lin - 1]) * match_bonus
        # inequality = (word02[col - 1] != word01[lin - 1]) * mismatch_penalty # can't be in function of previous as
        # symmetric values from the expected could be possible

        # equality = match_bonus if (word02[col - 1] == word01[lin - 1]) else mismatch_penalty
        # temp_gap_penalty = 0 if (word02[col - 1] == word01[lin - 1]) else gap_penalty
        matrix[lin, col] = (max(
            [0, matrix[lin - 1, col] + gap_penalty, matrix[lin, col - 1] + gap_penalty, matrix[lin - 1, col - 1] + inq])
        )
        directions_matrix[lin, col] = np.argmax([0, matrix[lin - 1, col] + gap_penalty, matrix[lin, col - 1] + gap_penalty, matrix[lin - 1, col - 1] + inq])
## TraceBack
print(matrix)
print(directions_matrix)
final_lin, final_col = np.argmax(matrix) // (len(word02) + 1), np.argmax(matrix) % (len(word02) + 1)

intersection_string = ""
actual_dir = directions_matrix[final_lin, final_col]
while actual_dir != NONE:
    print(final_lin, final_col)
    if actual_dir == UP:
        final_lin -= 1
        intersection_string += "_"
    elif actual_dir == LEFT:
        final_col -= 1
        intersection_string += "_"
    elif actual_dir == DIAGONAL:
        intersection_string += word01[final_lin - 1]
        final_lin -= 1
        final_col -= 1
    actual_dir = directions_matrix[final_lin, final_col]

print(intersection_string[::-1])
