def invert_matrix(matrix):
    values = set()
    for row in matrix:
        for elem in row:
            values.add(elem)
    vals = tuple(values)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = vals[0] if matrix[i][j] == vals[1] else vals[1]
    return matrix


print(invert_matrix([["a", "b"], ["a", "a"]]))
