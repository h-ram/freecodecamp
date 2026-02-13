import re

def parse_image(markdown):

    src = re.search(r"\((.*?)\)", markdown).group(1)
    alt = re.search(r"\[(.*?)\]", markdown).group(1)

    return f'<img src="{src}" alt="{alt}">'


test1 = parse_image("![Cute cat](cat.png)")
test2 = parse_image("![Rocket Ship](https://freecodecamp.org/cdn/rocket-ship.jpg)")
test3 = parse_image("![Cute cats!](https://freecodecamp.org/cats.jpeg)")

check1 = '<img src="cat.png" alt="Cute cat">'
check2 = '<img src="https://freecodecamp.org/cdn/rocket-ship.jpg" alt="Rocket Ship">'
check3 = '<img src="https://freecodecamp.org/cats.jpeg" alt="Cute cats!">'


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
