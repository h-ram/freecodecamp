def truncate_text(text):
    if len(text) < 21:
        return text
    return text[:17] + "..."

test1 = truncate_text("Hello, world!")
test2 = truncate_text("This string should get truncated.")
test3 = truncate_text("Exactly twenty chars")
test4 = truncate_text(".....................")

check1 = "Hello, world!"
check2 = "This string shoul..."
check3 = "Exactly twenty chars"
check4 = "...................."

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
