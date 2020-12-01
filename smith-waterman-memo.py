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

def memoize(f):
    def helper(x, y):
        if matrix[x, y] == -1:
            matrix[x, y], directions_matrix[x, y] = f(x, y)
        return matrix[x, y]
    return helper

# @memoize
# def memoization(x, y, dep):
#     global calls
#     calls += 1
#     print("\t" * dep ,"entry: ", x, y)
#     if matrix[x, y] != -1:
#         print("mais cedo")
#         return matrix[x, y]
#     # if x == 0 or y == 0: # Será necessário pa Recursive Only
#     #     print("\t" * dep ,"backing 0")
#     #     return 0
#     # print("\t" * dep ,"x= ", x, ";y= ", y)
#     eq = (match_bonus if (word02[y-1] == word01[x-1]) else mismatch_penalty)
#
#     v_up = memoization(x-1, y, dep + 1) + gap_penalty
#     v_left = memoization(x,y-1, dep + 1) + gap_penalty
#     v_diagonal = memoization(x-1,y-1, dep +1) + eq
#     # print("\t" * dep , "values:", v_up, v_left, v_diagonal)
#     matrix[x, y] = max(0, v_up, v_left, v_diagonal)
#     directions_matrix[x, y] = np.argmax([0, v_up, v_left, v_diagonal])
#     global calls_real
#     calls_real+=1
#     # print("\t" * dep ,"returning ",matrix[x, y])
#     return matrix[x, y]

@memoize
def memoization(x, y):
    eq = (match_bonus if (word02[y - 1] == word01[x - 1]) else mismatch_penalty)

    v_up = memoization(x - 1, y) + gap_penalty
    v_left = memoization(x, y - 1) + gap_penalty
    v_diagonal = memoization(x - 1, y - 1) + eq

    return max(0, v_up, v_left, v_diagonal), np.argmax([0, v_up, v_left, v_diagonal])

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

print(matrix)
memoization(len(word01), len(word02))
print(matrix)
print(directions_matrix)
backtrace()
