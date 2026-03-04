def card_values(cards):
    numeric_values = []
    for card in cards:
        if card[0] == "A":
            numeric_values.append(1)
        elif card[0] in "JKQ" or card[0:2] == "10":
            numeric_values.append(10)
        else:
            numeric_values.append(int(card[0]))

    return numeric_values

test1 = card_values(["3H", "4D", "5S"])
test2 = card_values(["AS", "10S", "10H", "6D", "7D"])
test3 = card_values(["8D", "QS", "2H", "JC", "9C"])
test4 = card_values(["AS", "KS"])
test5 = card_values(["10H", "JH", "QH", "KH", "AH"])

check1 = [3, 4, 5]
check2 = [1, 10, 10, 6, 7]
check3 = [8, 10, 2, 10, 9]
check4 = [1, 10]
check5 = [10, 10, 10, 10, 1]

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")