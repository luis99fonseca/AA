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
matrix = np.ones((len(word01) + 1, len(word02) + 1)) * -1
matrix[0, :] = 0
matrix[:, 0] = 0
directions_matrix = np.zeros((len(word01) + 1, len(word02) + 1))


# TODO: mudar nome no futuro pa melhor
def recursive_call(x, y):
    eq = (match_bonus if (word02[y - 1] == word01[x - 1]) else mismatch_penalty)
    if x == 0 or y == 0:
        return 0, 0

    v_up = recursive_call(x - 1, y)  # + gap_penalty
    v_left = recursive_call(x, y - 1)  # + gap_penalty
    v_diagonal = recursive_call(x - 1, y - 1)  # + eq
    # print("(", x, ",", y, ") = ", max(0, v_up[0] + gap_penalty, v_left[0] + gap_penalty, v_diagonal[0] + eq), ";",
    #       max(0, v_up[0], v_left[0], v_diagonal[0], v_up[1], v_left[1], v_diagonal[1]))
    max_score = max(0, v_up[0] + gap_penalty, v_left[0] + gap_penalty, v_diagonal[0] + eq)
    return max_score, max(max_score, v_up[1], v_left[1], v_diagonal[1])

print("MAX SCORE TOTAL é o 2o")
print(recursive_call(len(word01), len(word02)))
