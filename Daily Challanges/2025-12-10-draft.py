import re
def parse_bold(markdown):
    
    sentences = re.split(r'\*\*|__', markdown)
    print(sentences)
    html = ""
    for i in range(0, len(sentences)):
        if i % 2 == 0:
            html += sentences[i]
        else:
            html += f"<b>{sentences[i]}</b>"
    print(html)
    content = markdown[2:-2]
    print()
    # print(content)
    return html


test1 = parse_bold("**This is bold**")
test2 = parse_bold("__This is also bold__")
test3 = parse_bold("**This is not bold **")
test4 = parse_bold("__ This is also not bold__")
test5 = parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog.")


check1 = "<b>This is bold</b>"
check2 = "<b>This is also bold</b>"
check3 = "**This is not bold **"
check4 = "__ This is also not bold__"
check5 = "The <b>quick</b> brown fox <b>jumps</b> over the <b>lazy</b> dog."


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")