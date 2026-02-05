def count_change(change):
    total_cents = sum(change)
    dollars = total_cents // 100
    cents = total_cents % 100
    return f"${dollars}.{cents:02d}"

test1 = count_change([25, 10, 5, 1])
test2 = count_change([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25])
test3 = count_change([100, 25, 100, 1000, 5, 500, 2000, 25])
test4 = count_change([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10])
test5 = count_change([1])
test6 = count_change([25, 25, 25, 25])

check1 = "$0.41"
check2 = "$1.43"
check3 = "$37.55"
check4 = "$0.70"
check5 = "$0.01"
check6 = "$1.00"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")