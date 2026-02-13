def fibonacci_sequence(start_sequence, length):
    if length == 0:
        return []

    seq = start_sequence[:length]

    while len(seq) < length:
        seq.append(seq[-1] + seq[-2])

    return seq


test1 = fibonacci_sequence([0, 1], 20)
test2 = fibonacci_sequence([21, 32], 1)
test3 = fibonacci_sequence([0, 1], 0)
test4 = fibonacci_sequence([10, 20], 2)
test5 = fibonacci_sequence([123456789, 987654321], 5)

check1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
check2 = [21]
check3 = []
check4 = [10, 20]
check5 = [123456789, 987654321, 1111111110, 2098765431, 3209876541]

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")