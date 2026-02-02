def groundhog_day_prediction(appearance):
    if appearance == True:
        return "Looks like we'll have six more weeks of winter."
    if appearance == False:
        return "It's going to be an early spring."
    return "No prediction this year."

test1 = groundhog_day_prediction(True)
test2 = groundhog_day_prediction(False)
test3 = groundhog_day_prediction(None)
test4 = groundhog_day_prediction(" ")
test5 = groundhog_day_prediction("True")

check1 = "Looks like we'll have six more weeks of winter."
check2 = "It's going to be an early spring."
check3 = "No prediction this year."
check4 = "No prediction this year."
check5 = "No prediction this year."

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")