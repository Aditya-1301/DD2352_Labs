"""
M(i,j) -> max payoff from (i,j) -> TOP
L(i,j) = M(i-1, j-1) + P((i,j), (i-1, j-1))
A(i,j) = M(i-1, j) + P((i,j), (i-1, j))
R(i,j) = M(i-1, j+1) + P((i,j), (i-1, j-1))

M(i,j) = {
    if i == 0 -> 0
    if j == 1 -> MAX{A(i,j), R(i,j)} 
    if j == n -> MAX{A(i,j), L(i,j)} 
    else MAX{A(i,j), L(i,j), R(i,j)} 
}

M <- N x N Matrix

for l <- 1 .. N do
    M[1, l] <- 0
for i <- 2 .. N do
    M[i,1] <- MAX{A(i,j), R(i,j)}
    for j <- 2 .. N-1 do
        M[i,j] <- MAX{A(i,j), L(i,j), R(i,j)}
    M[i, n] <- MAX{Ai,1 .. Li,1}
return MAX{M[N,l]} (1<=l<=n)
"""

