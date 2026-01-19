def rotate(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

test1 = rotate([[1]])
test2 = rotate([[1, 2], [3, 4]])
test3 = rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
test4 = rotate([[0, 1, 0], [1, 0, 1], [0, 0, 0]])

check1 = [[1]]
check2 = [[3, 1], [4, 2]]
check3 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
check4 = [[0, 1, 0], [0, 0, 1], [0, 1, 0]]

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")