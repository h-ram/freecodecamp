

def update_inventory(inventory, shipment):
    
    for new_item in shipment:
        does_exit = False
        new_quantity, new_name = new_item
        for item in inventory:
            quantity, name = item
            if name == new_name:
                item[0] += new_quantity
                does_exit = True
        if not does_exit:
            inventory.append(new_item)

    return inventory


test1 = update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]])
test2 = update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"], [4, "oranges"]])
test3 = update_inventory([], [[10, "apples"], [30, "bananas"], [20, "oranges"]])
test4 = update_inventory([[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]])


check1 = [[3, "apples"], [8, "bananas"]]
check2 = [[3, "apples"], [8, "bananas"], [4, "oranges"]]
check3 = [[10, "apples"], [30, "bananas"], [20, "oranges"]]
check4 = [[1, "Bowling Ball"], [0, "Dirty Socks"], [1, "Hair Pin"], [0, "Microphone"], [1, "Half-Eaten Apple"], [1, "Toothpaste"]]


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")