def parse_unordered_list(markdown):
    lines = markdown.split("\n")

    html = []
    for line in lines:
        html.append(f"<li>{line[1:].strip()}</li>")
        
    return f"<ul>{''.join(html)}</ul>"


test1 = parse_unordered_list("- Item A\n- Item B")
test2 = parse_unordered_list("-  JavaScript\n-  Python")
test3 = parse_unordered_list("- 2 C Flour\n- 1/2 C Sugar\n- 1 Tsp Vanilla")
test4 = parse_unordered_list("- A-1\n- A-2\n- B-1")

check1 = "<ul><li>Item A</li><li>Item B</li></ul>"
check2 = "<ul><li>JavaScript</li><li>Python</li></ul>"
check3 = "<ul><li>2 C Flour</li><li>1/2 C Sugar</li><li>1 Tsp Vanilla</li></ul>"
check4 = "<ul><li>A-1</li><li>A-2</li><li>B-1</li></ul>"

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
