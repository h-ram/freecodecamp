def buy_items(funds, items):

    exchange_rates = {
        "USD": 1,
        "EUR": 1.10,
        "GBP": 1.25,
        "JPY": 0.007,
        "CAD": 0.75,
    }
    
    # standarize currencies
    std_funds = float(funds[0])*exchange_rates[funds[1]]
    std_items = []
    for item in items:
        std_item = float(item[0]) * exchange_rates[item[1]]
        std_items.append(std_item)

    # count how many you can buy
    can_buy = 0
    for item in std_items:
        std_funds -= item
        if std_funds <=0 :
            break
        can_buy += 1

    if can_buy == len(items):
        return "Buy them all!"
    else:
        return f"Buy the first {can_buy} items."


test1 = buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]])
test2 = buy_items(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]])
test3 = buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]])
test4 = buy_items(["5000", "JPY"], [["3.00", "USD"], ["1000", "JPY"], ["5.00", "CAD"], ["2.00", "EUR"], ["4.00", "USD"], ["2000", "JPY"]])
test5 = buy_items(["200.00", "USD"], [["50.00", "USD"], ["40.00", "EUR"], ["30.00", "GBP"], ["5000", "JPY"], ["25.00", "CAD"], ["20.00", "USD"]])


check1 = "Buy the first 2 items."
check2 = "Buy them all!"
check3 = "Buy the first 3 items."
check4 = "Buy them all!"
check5 = "Buy the first 5 items."


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")