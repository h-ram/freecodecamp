
def parse_blockquote(markdown):
    markdown = markdown.strip()
    markdown = markdown.strip('>')
    markdown = markdown.strip()

    return f"<blockquote>{markdown}</blockquote>"


test1 = parse_blockquote("> This is a quote")
test2 = parse_blockquote(" > This is also a quote")
test3 = parse_blockquote("  >    So  Is  This")

check1 = "<blockquote>This is a quote</blockquote>"
check2 = "<blockquote>This is also a quote</blockquote>"
check3 = "<blockquote>So  Is  This</blockquote>"

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")