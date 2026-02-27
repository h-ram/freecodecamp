def shift_matrix(matrix, shift):
    rows = len(matrix)
    cols = len(matrix[0])
    total = rows * cols

    # flatten
    flat = []
    for row in matrix:
        flat.extend(row)

    shift %= total
    flat = flat[-shift:] + flat[:-shift]

    # rebuild matrix
    result = []
    for i in range(rows):
        result.append(flat[i * cols:(i + 1) * cols])

    return result

test1 = shift_matrix([[1, 2, 3], [4, 5, 6]], 1)
test2 = shift_matrix([[1, 2, 3], [4, 5, 6]], -1)
test3 = shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5)
test4 = shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -6)
test5 = shift_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 7)
test6 = shift_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], -54)

check1 = [[6, 1, 2], [3, 4, 5]]
check2 = [[2, 3, 4], [5, 6, 1]]
check3 = [[5, 6, 7], [8, 9, 1], [2, 3, 4]]
check4 = [[7, 8, 9], [1, 2, 3], [4, 5, 6]]
check5 = [[10, 11, 12, 13], [14, 15, 16, 1], [2, 3, 4, 5], [6, 7, 8, 9]]
check6 = [[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 1, 2], [3, 4, 5, 6]]

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")