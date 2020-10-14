matrix = [[6, 7, 12, 5], [5, 3, 11, 18], [7, 17, 3, 3], [8, 10, 14, 9]]


def matrixPath():
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if (i == 0 and j == 0):
                a = matrix[i][j]
                print(a, '1')
            elif (i == 0):
                a = matrix[i][j]
                print(a, '2')
            elif (j == 0):
                a = matrix[i][j]
                print(a, '3')
            else:
                a = matrix[i][j] + min([matrix[i-1][j], matrix[i][j-1]])
                print(a, '4')
    return a


print(matrixPath())
