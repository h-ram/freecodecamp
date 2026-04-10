def get_next_bingo_number(n):
    b_num = int(n[1:])% 75 + 1
    if b_num < 16:
        return f"B{b_num}"
    if b_num < 31:
        return f"I{b_num}"
    if b_num < 46:
        return f"N{b_num}"
    if b_num < 61:
        return f"G{b_num}"
    if b_num < 75:
        return f"O{b_num}"
    return "Invalid"

print(get_next_bingo_number("B10"))
print(get_next_bingo_number("O75"))