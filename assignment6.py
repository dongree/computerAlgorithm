matrix = [[6, 7, 12, 5], [5, 3, 11, 18], [7, 17, 3, 3], [8, 10, 14, 9]]
min_dist = [[0]*4]*4


def matrixPath():
    n = len(matrix) - 1
    for i in range(n+1):
        for j in range(n+1):
            if (i == 0 and j == 0):
                min_dist[i][j] = matrix[0][0]
            elif (i == 0):
                min_dist[i][j] = min_dist[0][j-1] + matrix[i][j]
            elif (j == 0):
                min_dist[i][j] = min_dist[i-1][0] + matrix[i][j]
            else:
                min_dist[i][j] = matrix[i][j] + \
                    min([min_dist[i-1][j], min_dist[i][j-1]])
    return min_dist[n][n]


print(matrixPath())
