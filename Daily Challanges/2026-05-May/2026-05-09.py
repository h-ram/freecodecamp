def transpose(matrix):
    m = len(matrix)
    n = len(matrix[0])
    transposed_matrix = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(matrix[j][i])
        transposed_matrix.append(temp)
    return transposed_matrix

print(transpose([[1, 2, 3], [4, 5, 6]]))
print(transpose([[1, 2], [3, 4], [5, 6]]))