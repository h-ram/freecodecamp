from collections import defaultdict
def get_frequency(s):
    counter = defaultdict(int)
    for char in s:
        counter[char] += 1
    return dict(counter)

print(get_frequency("test"))
print(get_frequency("mississippi"))