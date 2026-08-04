def get_contrast_rating(light, dark, large):
    ratio = (light + 0.05) / (dark + 0.05)

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


print(get_contrast_rating(1.0, 0.0, False))
print(get_contrast_rating(0.9015, 0.1364, False))
print(get_contrast_rating(0.8965, 0.1628, False))
print(get_contrast_rating(0.7469, 0.0957, True))
print(get_contrast_rating(0.7489, 0.2018, True))
print(get_contrast_rating(0.6571, 0.1974, True))