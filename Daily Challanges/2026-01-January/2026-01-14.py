import re

def parse_link(markdown):
    link_url = re.search(r'\(([^)]+)\)', markdown).group(1)
    link_text = re.search(r'\[([^)]+)\]', markdown).group(1)

    return f"<a href=\"{link_url}\">{link_text}</a>"

test1 = parse_link("[freeCodeCamp](https://freecodecamp.org/)")
test2 = parse_link("[Donate to our charity.](https://www.freecodecamp.org/donate/)")
test3 = parse_link("[Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.](https://github.com/freeCodeCamp/freeCodeCamp/)")

check1 = '<a href="https://freecodecamp.org/">freeCodeCamp</a>'
check2 = '<a href="https://www.freecodecamp.org/donate/">Donate to our charity.</a>'
check3 = '<a href="https://github.com/freeCodeCamp/freeCodeCamp/">Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.</a>'

print(test1)

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")