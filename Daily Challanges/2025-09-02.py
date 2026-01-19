def rgb_to_hex(rgb):
    colors = rgb[4:-1].split(',')

    red = int(colors[0])
    green = int(colors[1])
    blue = int(colors[2])


    red_hex = format(red, '02x')
    green_hex = format(green, '02x')
    blue_hex = format(blue, '02x')

    return f"#{red_hex}{green_hex}{blue_hex}"


test1 = rgb_to_hex("rgb(255, 255, 255)")
test2 = rgb_to_hex("rgb(1, 11, 111)")
test3 = rgb_to_hex("rgb(173, 216, 230)")
test4 = rgb_to_hex("rgb(79, 123, 201)")

check1 = "#ffffff"
check2 = "#010b6f"
check3 = "#add8e6"
check4 = "#4f7bc9"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")