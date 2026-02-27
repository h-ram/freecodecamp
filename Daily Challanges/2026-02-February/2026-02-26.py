def count_letters_and_numbers(s):
    letter_count = 0
    number_count = 0
    for character in s:
        if character.isalpha():
            letter_count += 1
        elif character.isdigit():
            number_count += 1

    adj1 = "letter" if letter_count == 1 else "letters"
    adj2 = "number" if number_count == 1 else "numbers"

    result = f"The string has {letter_count} {adj1} and {number_count} {adj2}."
    return result

test1 = count_letters_and_numbers("helloworld123")
test2 = count_letters_and_numbers("Catch 22")
test3 = count_letters_and_numbers("A1!")
test4 = count_letters_and_numbers("12345")
test5 = count_letters_and_numbers("password")

check1 = "The string has 10 letters and 3 numbers."
check2 = "The string has 5 letters and 2 numbers."
check3 = "The string has 1 letter and 1 number."
check4 = "The string has 0 letters and 5 numbers."
check5 = "The string has 8 letters and 0 numbers."

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")