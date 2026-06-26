def calculate_bmi(weight, height):
    return round(weight / (height * height) * 703, 1)


print(calculate_bmi(180, 70))
print(calculate_bmi(140, 64))
print(calculate_bmi(160, 76))
print(calculate_bmi(200, 60))
print(calculate_bmi(150, 68))
