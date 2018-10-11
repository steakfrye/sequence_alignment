##### Adapted from Hirschberg's algorithm on https://en.wikipedia.org/wiki/Hirschberg%27s_algorithm ####

sequence1 = AGTACGCA
sequence2 = TATGC

def NWScore(sequence1, sequence2):
    Score(0,0) = 0

    for j = 1 to length(sequence2):
        Score(0, j) = Score(0, j - 1) + Ins(sequence2[j])

    for i = 1 to length(sequence1):
        Score(i, 0) = Score(i - 1,0) + Del(sequence1[i])

        for j = 1 to length(sequence2):
            sub_score = Score(i - 1,j - 1) + (sequence1[i] - sequence2[j])
            del_score = Score(i - 1, j) + Del(sequence1[i])
            ins_score = Score( i, j - 1) + Ins(sequence2[j])
            Score(i, j) = max(sub_score, del_score, ins_score)

        for j = 0 to length(sequence2):
         LastLine(j) = Score(length(sequence1),j)
        return LastLine

def Hirschberg(sequence1, sequence2):
    Z = ""
    W = ""
    if length(sequence1) == 0:
        for i = 1 to length(sequence2):
            Z = Z + '-'
            W = W + sequence2i

    else if length(sequence2) == 0:
        for i = 1 to length(sequence1):
            Z = Z + sequence1[i]
            W = W + '-'

    else if length(sequence1) == 1 or length(sequence2) == 1:
        (Z, W) = NeedlemanWunsch(sequence1, sequence2)

    else:
        sequence1_len = length(sequence1)
        sequence1_mid = length(sequence1)/2
        sequence2_len = length(sequence2)

    ScoreL = NWScore(sequence11:sequence1_mid, sequence2)
    ScoreR = NWScore(rev(Xxmid+1:sequencelen), rev(sequence2))
    sequence2_mid = arg max ScoreL + rev(ScoreR)

    (Z, W) = Hirschberg(sequence1:xmid, sequence21:sequence2mid) + Hirschberg(sequencexmid+1:xlen, sequence2sequence2mid+1:sequence2len)

    return (Z, W)
