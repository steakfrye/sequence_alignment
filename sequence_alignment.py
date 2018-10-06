def Hirschberg(X,Y):
   Z = ""
   W = ""
   if length(X) == 0:
     for i=1 to length(Y):
       Z = Z + '-'
       W = W + Yi

   else if length(Y) == 0:
     for i=1 to length(X):
       Z = Z + Xi
       W = W + '-'

   else if length(X) == 1 or length(Y) == 1:
     (Z,W) = NeedlemanWunsch(X,Y)
 else:
     xlen = length(X)
     xmid = length(X)/2
     ylen = length(Y)

     ScoreL = NWScore(X1:xmid, Y)
     ScoreR = NWScore(rev(Xxmid+1:xlen), rev(Y))
     ymid = arg max ScoreL + rev(ScoreR)

     (Z,W) = Hirschberg(X1:xmid, y1:ymid) + Hirschberg(Xxmid+1:xlen, Yymid+1:ylen)
     
    return (Z,W)
