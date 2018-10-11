##### Adapted from Hirschberg's algorithm on https://en.wikipedia.org/wiki/Hirschberg%27s_algorithm #####

sequence1 = "AGTACGCA"
sequence2 = "TATGC"

# Placeholder functions in case developer would like to change to complex score system.
def ins(y):
    return -2

def delete(x):
    return -2

def sub(x, y):
    if x == y:
        return 2
    else:
        return -1

def create_grid(sequence1, sequence2):
    grid = [[0 for row in range(len(sequence2))]
                for column in range(len(sequence1))]

    return grid

grid = create_grid(sequence1, sequence2)

def set_position(x, y, value):
    del grid[x][y]
    grid[x].insert(y, value)

def nw_score(sequence1, sequence2):
    set_position(0, 0, 0)

    for j in range(len(sequence2)):
        set_position(0, j, ins(sequence2[j]))

    for i in range(len(sequence1)):
        set_position(i, 0, delete(sequence1[i]))

        for j in range(len(sequence2)):
            sub_score = grid[i][j] + sub(sequence1[i], sequence2[j])
            delete_score = grid[i][j + 1] + delete(sequence1[i])
            ins_score = grid[i + 1][j] + ins(sequence2[j])
            set_position(i, j, max(sub_score, delete_score, ins_score))

        for j in range(len(sequence2)):
         last_line(j + 1) = set_position(len(sequence1), j + 1)
        return last_line

def hirschberg(sequence1, sequence2):
    Z = ""
    W = ""
    if len(sequence1) == 0:
        for i in range(len(sequence2)):
            Z += '-'
            W += sequence2[i + 1]

    elif len(sequence2) == 0:
        for i in range(len(sequence1)):
            Z += sequence1[i + 1]
            W += '-'

    elif len(sequence1) == 1 or len(sequence2) == 1:
        (Z, W) = needleman_wunsch(sequence1, sequence2)

    else:
        sequence1_len = len(sequence1)
        sequence1_mid = len(sequence1)/2
        sequence2_len = len(sequence2)

    score_l = nw_score(sequence1[1:sequence1_mid], sequence2)
    score_r = nw_score(rev(sequence1[sequence1_mid+1:sequence1_len]), rev(sequence2))
    sequence2_mid = max(score_l + rev(score_r))

    (Z, W) = hirschberg(sequence1[1:sequence1_mid], sequence2[1:sequence2_mid]) + hirschberg(sequence1[sequence1_mid+1:xlen], sequence2[sequence2_mid+1:sequence2len])

    return (Z, W)


print(grid)
