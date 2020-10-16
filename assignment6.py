matrix = [[6, 7, 12, 5], [5, 3, 11, 18], [7, 17, 3, 3], [8, 10, 14, 9]]
distance = [[0]*4]*4


def matrixPath():
    n = len(matrix) - 1
    for i in range(n+1):
        for j in range(n+1):
            if (i == 0 and j == 0):
                distance[i][j] = matrix[0][0]
            elif (i == 0):
                distance[i][j] = distance[0][j-1] + matrix[i][j]
            elif (j == 0):
                distance[i][j] = distance[i-1][0] + matrix[i][j]
            else:
                distance[i][j] = matrix[i][j] + \
                    min([distance[i-1][j], distance[i][j-1]])
    return distance[n][n]


print(matrixPath())


# def matrixPath(i, j):
#     if (distance[i][j] != -1):
#         return distance[i][j]
#     if(i == 0 and j == 0):
#         distance[i][j] = matrix[i][j]
#     elif (i == 0):
#         distance[i][j] = matrixPath(i, j-1) + matrix[i][j]
#     elif (j == 0):
#         distance[i][j] = matrixPath(i-1, j) + matrix[i][j]
#     else:
#         distance[i][j] = min(matrix[i-1][j], matrix[i][j-1]) + matrix[i][j]
#     return distance[i][j]


# print(matrixPath(3, 3))
