
def get_contrast_rating(light, dark, large):
    def luminance(rgb):
        values = []

        for channel in rgb:
            channel /= 255

            if channel <= 0.04045:
                channel /= 12.92
            else:
                channel = ((channel + 0.055) / 1.055) ** 2.4

            values.append(channel)

        return (
            0.2126 * values[0]
            + 0.7152 * values[1]
            + 0.0722 * values[2]
        )

    ratio = (luminance(light) + 0.05) / (luminance(dark) + 0.05)

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


print(get_contrast_rating([255, 255, 255], [0, 0, 0], False))
print(get_contrast_rating([215, 188, 188], [55, 55, 55], False))
print(get_contrast_rating([143, 144, 210], [46, 47, 61], False))
print(get_contrast_rating([167, 167, 210], [53, 10, 53], True))
print(get_contrast_rating([135, 147, 155], [60, 70, 90], True))
print(get_contrast_rating([125, 210, 195], [105, 130, 90], True))