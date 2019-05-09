
def lcs (first, second):
    #number first: number of columns
    #number second: number of rows
    col=len(first)
    row=len(second)
    L=[[0 for x in range (col+1)]for y in range(row+1)]
    for i in range (1,row+1,1):
        for j in range (1,col+1,1):
            if first [j-1]==second[i-1]:
                L[i][j]=L[i-1][j-1]+1
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])
    print (L[row][col])

    #Traceback

    i=row
    j=col
    LCS=" "
    while i>0 and j>0:
        up =L[i-1][j]
        left=L[i][j-1]
        if first[j-1] == second[i-1]:
            LCS=first[j-1]+LCS
            i-=1
            j-=1
        elif L[i][j] == up:
            i-=1
        else:
            j-=1

    print (LCS)

X="AGGTAB"
Y="GXTXAYB"

lcs(X,Y)
