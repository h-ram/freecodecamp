def most_frequent(arr):
    counter = {}

    for item in arr:
        if item in counter.keys():
            counter[item] += 1
        else:
            counter[item] = 1

    counter = sorted(counter.items(), key=lambda item: item[1])
    most_freq = counter[-1][0]
    return most_freq

test1 = most_frequent(["a", "b", "a", "c"])
test2 = most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]) 
test3 = most_frequent([True, False, "False", "True", False])
test4 = most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60])

check1 = "a"
check2 = 2
check3 = False
check4 = 40 

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
