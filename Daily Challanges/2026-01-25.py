def scale_image(size, scale):
    w, h = size.split('x')

    scaled_w = int(int(w) * scale)
    scaled_h = int(int(h) * scale)

    scaled_size = f"{scaled_w}x{scaled_h}"
    return scaled_size

test1 = scale_image("800x600", 2)
test2 = scale_image("100x100", 10)
test3 = scale_image("1024x768", 0.5)
test4 = scale_image("300x200", 1.5)

check1 = "1600x1200"
check2 = "1000x1000"
check3 = "512x384"
check4 = "450x300"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
