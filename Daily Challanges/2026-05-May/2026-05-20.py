def zip_strings(a, b):
    result = []
    min_len = min(len(a), len(b))
    for i in range(min_len):
        result.append(a[i])
        result.append(b[i])
    result.append(a[min_len:])
    result.append(b[min_len:])
    return ''.join(result)

print(zip_strings("abc", "123"))
print(zip_strings("day", "night"))