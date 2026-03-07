def get_element_size(window_size, element_vw, element_vh):
    width, height = map(int,window_size.split('x'))
    vw = int(element_vw[:-2])
    vh = int(element_vh[:-2])
    new_width = width * (vw / 100)
    new_height = height * (vh / 100)
    return f"{new_width:.0f} x {new_height:.0f}"

test1 = get_element_size("1200 x 800", "50vw", "50vh")
test2 = get_element_size("320 x 480", "25vw", "50vh")
test3 = get_element_size("1000 x 500", "7vw", "3vh")
test4 = get_element_size("1920 x 1080", "95vw", "100vh")
test5 = get_element_size("1200 x 800", "0vw", "0vh")
test6 = get_element_size("1440 x 900", "100vw", "114vh")

check1 = "600 x 400"
check2 = "80 x 240"
check3 = "70 x 15"
check4 = "1824 x 1080"
check5 = "0 x 0"
check6 = "1440 x 1026"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")