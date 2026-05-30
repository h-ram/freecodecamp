from math import gcd


def get_wider_aspect_ratio(dim1, dim2):
    w1, h1 = map(int, dim1.split("x"))
    w2, h2 = map(int, dim2.split("x"))

    if w1 * h2 >= w2 * h1:
        w, h = w1, h1
    else:
        w, h = w2, h2

    g = gcd(w, h)
    return f"{w // g}:{h // g}"


print(get_wider_aspect_ratio("1920x1080", "800x600"))
print(get_wider_aspect_ratio("1080x1350", "2048x1536"))
print(get_wider_aspect_ratio("640x480", "2440x1220"))
