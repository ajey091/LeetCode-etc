def ZeroMatrix(matrix1):
    flag = 0
    rowtrack = []
    columntrack = []

    for i in range(0,len(matrix1)):
        for j in range(0,len(matrix1[0])):
            if matrix1[i][j] == 0:
                flag = 1
                rowtrack.append(i)
                columntrack.append(j)

    for i in range(0,len(matrix1)):
        for j in range(0,len(matrix1[0])):
            if (i in rowtrack) or (j in columntrack):
                matrix1[i][j] = 0

    return matrix1

print (ZeroMatrix([[1,2,3,4],
[4,5,6,5],
[7,0,9,10]]))
