def burn_candles(candles, leftovers_needed):

    leftovers = candles

    while leftovers >= leftovers_needed:
        recycled = leftovers // leftovers_needed
        leftovers = recycled + leftovers % leftovers_needed

        candles += recycled

    return candles

test1 = burn_candles(7, 2)
test2 = burn_candles(10, 5)
test3 = burn_candles(20, 3)
test4 = burn_candles(17, 4)
test5 = burn_candles(2345, 3)

check1 = 13
check2 = 12
check3 = 29
check4 = 22
check5 = 3517

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")