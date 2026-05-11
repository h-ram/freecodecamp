def is_valid_isbn_13(s):
    digit_sum = 0
    digit_count = 0
    for char in s:
        if char == "-":
            continue
        if not char.isdigit():
            print("not digit")
            return False
        digit_count += 1
        digit_sum += int(char) * (1 if digit_count % 2 == 1 else 3)
    return digit_count == 13 and digit_sum % 10 == 0


print(is_valid_isbn_13("9780306406157"))
print(is_valid_isbn_13("97803064061570"))
print(is_valid_isbn_13("978-0-13-595705-9"))
