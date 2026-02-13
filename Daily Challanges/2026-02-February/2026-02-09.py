def ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus):
    
    place_1 = 180.0
    place_2 = 175.0
    place_3 = 172.0

    score = distance_points + style_points + wind_comp + k_point_bonus

    if score > place_1:
        return "Gold"
    elif score > place_2:
        return "Silver"
    elif score > place_3:
        return "Bronze"
    else:
        return "No Medal"

test1 = ski_jump_medal(125.0, 58.0, 0.0, 6.0)
test2 = ski_jump_medal(119.0, 50.0, 1.0, 4.0)
test3 = ski_jump_medal(122.0, 52.0, -1.0, 4.0)
test4 = ski_jump_medal(118.0, 50.5, -1.5, 4.0)
test5 = ski_jump_medal(124.0, 50.5, 2.0, 5.0)

check1 = "Gold"
check2 = "Bronze"
check3 = "Silver"
check4 = "No Medal"
check5 = "Gold"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")