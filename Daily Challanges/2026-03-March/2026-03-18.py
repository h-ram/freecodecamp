def largest_number(s):
    seperators = ",;:!?"
    numbers = []
    current = ""
    for char in s:
        if char in seperators:
            numbers.append(float(current))
            current = ""
        else:
            current += char
    numbers.append(float(current))
    return max(numbers)

print(largest_number("1,2"))
print(largest_number("12;-50,99.9,49.1!-10.1?88?16") )