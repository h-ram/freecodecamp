
def verify_card_number(digits):

    # remove spaces and hyphons
    digits = digits.replace(" ", "")
    digits = digits.replace("-", "")
    digits = [int(digit) for digit in digits]

    # double every second digits from the right
    for i in range(len(digits)-2,-1,-2):
        double = digits[i] * 2
        digits[i] = double - 9 if double > 9 else double

    # sum all digits
    sum_ = sum(digits)
    if sum_ % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"


test1 = '453914889'
test2 = '4111-1111-1111-1111'
test3 = '453914881'
test4 = '1234 5678 9012 3456'

check1 = "VALID!"
check2 = "VALID!"
check3 = "INVALID!"
check4 = "INVALID!"

print(f"{test1} -> {verify_card_number(test1)}")
print(f"{test2} -> {verify_card_number(test2)}")
print(f"{test3} -> {verify_card_number(test3)}")
print(f"{test4} -> {verify_card_number(test4)}")

print("\n=====Tests=====")
print(f"Test1: {verify_card_number(test1) == check1}")
print(f"Test2: {verify_card_number(test2) == check2}")
print(f"Test3: {verify_card_number(test3) == check3}")
print(f"Test4: {verify_card_number(test4) == check4}")
print("===============")