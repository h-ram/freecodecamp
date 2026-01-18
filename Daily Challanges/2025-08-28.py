def get_laptop_cost(laptops, budget):
    laptops.sort(reverse=True)
    
    for i in range(1, len(laptops)):
        price = laptops[i]
        if budget >= price:
            return price
    return 0


test1 = get_laptop_cost([1500, 2000, 1800, 1400], 1900)
test2 = get_laptop_cost([1500, 2000, 2000, 1800, 1400], 1900)
test3 = get_laptop_cost([2099, 1599, 1899, 1499], 2200)
test4 = get_laptop_cost([2099, 1599, 1899, 1499], 1000)
test5 = get_laptop_cost([1200, 1500, 1600, 1800, 1400, 2000], 1450)

check1 = 1800
check2 = 1800
check3 = 1899
check4 = 0
check5 = 1400

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")