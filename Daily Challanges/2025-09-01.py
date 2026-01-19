def tribonacci_sequence(start_sequence, length):

    seq = start_sequence
    
    for i in range(2, length-1):
        seq.append(seq[i-2]+ seq[i-1] + seq[i])
    
    return seq[:length]

test1 = tribonacci_sequence([0, 0, 1], 20)
test2 = tribonacci_sequence([21, 32, 43], 1)
test3 = tribonacci_sequence([0, 0, 1], 0)
test4 = tribonacci_sequence([10, 20, 30], 2)
test5 = tribonacci_sequence([10, 20, 30], 3)
test6 = tribonacci_sequence([123, 456, 789], 8)

check1 = [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513]
check2 = [21]
check3 = []
check4 = [10, 20]
check5 = [10, 20, 30]
check6 = [123, 456, 789, 1368, 2613, 4770, 8751, 16134]

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")