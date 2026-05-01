checker = [
    # rows
    '01000001',
    '01101111',
    '01000100',
    '01100101',
    '01010010',
    '01010100',
    '01101000',
    '10101110',

    # columns
    '00000001',
    '11111110',
    '01011011',
    '00001100',
    '01000011',
    '01111001',
    '01000100',
    '11010000'
]

def is_in_crossword(char):
    bin_str = format(ord(char), '08b')
    rev = bin_str[::-1]
    
    for bstr in checker:
        if bin_str in bstr or rev in bstr:
            return True
    return char == 'I'


print(is_in_crossword("I"))
print(is_in_crossword("D"))
print(is_in_crossword("0"))
print(is_in_crossword("u"))
print(is_in_crossword("Y"))
print(is_in_crossword("p"))
print(is_in_crossword("1"))
print(is_in_crossword("Q"))