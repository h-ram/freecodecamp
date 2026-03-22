ROAST_LEVEL = {
    "'": 1,
    "-": 2,
    ".": 3
}
def detect_roast(beans):
    points = 0
    for bean in beans:
        points += ROAST_LEVEL[bean]
    avg_points = points/len(beans)
    if avg_points < 1.75:
        return "Light"
    elif avg_points <= 2.5:
        return "Medium"
    else:
        return "Dark"
    return beans

print(detect_roast("''-''''''-'-''--''''"))
print(detect_roast(".--.-..-......----.'"))