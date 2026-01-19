import random

def generate_hex(color):
    hex_colors = {
        "red": "FF0000",
        "green":"00FF00",
        "blue":"0000FF"
    }
    if color not in hex_colors.keys():
        return "Invalid color"

    random_hex = str(random.randint(0,9))
    return random_hex + hex_colors[color][1:]

# kinda cheated by randomizing only one number :)

