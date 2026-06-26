def parse_frontmatter(frontmatter_string: str) -> dict:
    parsed_data = {}
    lines = frontmatter_string.strip().split("\n")

    for line in lines:
        if line == "---" or not line.strip():
            continue

        if ": " in line:
            key, value_str = line.split(": ", 1)

            if value_str == "true":
                parsed_data[key] = True
            elif value_str == "false":
                parsed_data[key] = False
            else:
                try:
                    parsed_data[key] = int(value_str)
                except ValueError:
                    try:
                        parsed_data[key] = float(value_str)
                    except ValueError:
                        parsed_data[key] = value_str

    return parsed_data


print("Test 1:")
test_1 = parse_frontmatter("---\ntitle: My Post\ndraft: false\nviews: 100\n---")
print(test_1)
print(f"Passed: {test_1 == {'title': 'My Post', 'draft': False, 'views': 100}}\n")

print("Test 2:")
test_2 = parse_frontmatter(
    "---\nid: 6a174db57256a112f932195c\ntitle: My Book\nlocale: en\nwordCount: 10000\npublished: false\n---"
)
print(test_2)
print(
    f"Passed: {test_2 == {'id': '6a174db57256a112f932195c', 'title': 'My Book', 'locale': 'en', 'wordCount': 10000, 'published': False}}\n"
)

print("Test 3:")
test_3 = parse_frontmatter(
    "---\nversion: 1.0.0\nurl: https://example.com\nprivate: true\n---"
)
print(test_3)
print(
    f"Passed: {test_3 == {'version': '1.0.0', 'url': 'https://example.com', 'private': True}}\n"
)

print("Test 4:")
test_4 = parse_frontmatter("---\nrating: 4.5\nprice: 9.99\n---")
print(test_4)
print(f"Passed: {test_4 == {'rating': 4.5, 'price': 9.99}}")
