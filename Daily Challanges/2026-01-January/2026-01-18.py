def gets_free_shipping(cart, minimum):
    prices = {
        "shirt": 34.25,
        "jeans": 48.50,
        "shoes": 75.00,
        "hat": 19.95,
        "socks": 15.00,
        "jacket": 109.95
    }
    
    total = 0
    for item in cart:
        total += prices.get(item, 0)
    
    return total > minimum

test1 = gets_free_shipping(["shoes"], 50)
test2 = gets_free_shipping(["hat", "socks"], 50)
test3 = gets_free_shipping(["jeans", "shirt", "jacket"], 75)
test4 = gets_free_shipping(["socks", "socks", "hat"], 75)
test5 = gets_free_shipping(["shirt", "shirt", "jeans", "socks"], 100)
test6 =  gets_free_shipping(["hat", "socks", "hat", "jeans", "shoes", "hat"], 200)

check1 = True
check2 = False
check3 = True
check4 = False
check5 = True
check6 = False

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
print(f"Test6: {test6==check6}")