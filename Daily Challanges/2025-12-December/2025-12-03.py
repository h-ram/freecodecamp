def convert_list_item(markdown):
    markdown = markdown.strip()
    if markdown[0].isdigit() and markdown[1] == '.':
        return f"<li>{markdown[2:].strip()}</li>"
    else:
        return "Invalid format"


test1 = convert_list_item("1. My item")
test2 = convert_list_item(" 1.  Another item")
test3 = convert_list_item("1 . invalid item")
test4 = convert_list_item("2. list item text")
test5 = convert_list_item(". invalid again")
test6 = convert_list_item("A. last invalid")

check1 = "<li>My item</li>"
check2 = "<li>Another item</li>"
check3 = "Invalid format"
check4 = "<li>list item text</li>"
check5 = "Invalid format"
check6 = "Invalid format"

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
print(f"Test6: {test6==check6}")