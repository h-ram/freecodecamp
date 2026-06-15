def is_valid_card(card_number):
    total = 0
    for i, char in enumerate(reversed(card_number)):
        digit = int(char)
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return total % 10 == 0


print(is_valid_card("4532015112830366"))
print(is_valid_card("5425233430109903"))
print(is_valid_card("371449635398431"))
print(is_valid_card("6011111111111117"))
print(is_valid_card("4532015112830367"))
print(is_valid_card("1234567890123456"))
print(is_valid_card("4532015112830368"))
