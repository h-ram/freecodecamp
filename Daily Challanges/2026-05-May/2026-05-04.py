def convert_parsecs(parsecs):
    return parsecs * 2 if parsecs % 2 == 1 else parsecs * 3

print(convert_parsecs(1))
print(convert_parsecs(2))