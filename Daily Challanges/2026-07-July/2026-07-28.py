def get_contrast_rating(ratio, large):
    ratio = float(ratio)

    if large:
        if ratio >= 4.5:
            return "AAA"
        if ratio >= 3:
            return "AA"
    else:
        if ratio >= 7:
            return "AAA"
        if ratio >= 4.5:
            return "AA"

    return "Fail"


print(get_contrast_rating("7.5", False))
print(get_contrast_rating("4.8", False))
print(get_contrast_rating("4.2", False))
print(get_contrast_rating("4.5", True))
print(get_contrast_rating("3.0", True))
print(get_contrast_rating("2.7", False))