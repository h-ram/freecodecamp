
def to_roman(num):

    m = num // 1000 ; num %= 1000
    d = num // 500 ; num %= 500
    c = num // 100 ; num %= 100
    l = num // 50 ; num %= 100
    x = num // 10 ; num %= 10
    v = num // 5 ; num %= 5
    i = num // 1

    M = "M" * m
    D = "D" * d
    C = "C" * c
    L = "L" * l
    X = "X" * x
    V = "V" * v
    I = "I" * i
    
    roman = M + D + C + L + X + V + I
    print(roman)
    return roman

test1 = to_roman(18)
test2 = to_roman(19)
test3 = to_roman(1464)
test4 = to_roman(2025)
test5 = to_roman(3999)

check1 = "XVIII"
check2 = "XIX"
check3 = "MCDLXIV"
check4 = "MMXXV"
check5 = "MMMCMXCIX"

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
