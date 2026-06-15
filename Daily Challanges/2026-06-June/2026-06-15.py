def sort_numbers(s):
    return sorted(list(map(int, s.split(','))))

print(sort_numbers("3,1,2"))
print(sort_numbers("5,3,8,1,9,2"))
print(sort_numbers("12,61,49,80,19,50,77,38"))
print(sort_numbers("0,6,-19,44,-2,7,0"))