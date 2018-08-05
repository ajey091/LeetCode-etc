def RotateMatrix(matrix1):
    newmat = [[0]*len(matrix1) for i in range(len(matrix1))]
    linenum = len(matrix1) -1
    for i in range(0,len(newmat)):
        for j in range(0,len(newmat)):
            newmat[j][linenum] = matrix1[i][j]

        linenum -= 1

    return newmat

print (RotateMatrix([[1,2,3,4],
[4,5,6,5],
[7,8,9,6],
[7, 8, 9, 10]]
))
