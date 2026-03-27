def truncate_text(s):
    def char_width(c):
        if c in "ilI":
            return 1
        elif c in "fjrt":
            return 2
        elif c in "abcdeghkmnopqrstuvwxyzJL":
            return 3
        elif c in "ABCDEFGHKMNOPQRSTUVWXYZ":
            return 4
        elif c == " ":
            return 2
        elif c == ".":
            return 1
        return 0

    total = sum(char_width(c) for c in s)
    if total <= 50:
        return s

    max_text_width = 47  # 50 - 3 (for "...")
    running = 0
    cutoff = 0
    for i, c in enumerate(s):
        w = char_width(c)
        if running + w > max_text_width:
            break
        running += w
        cutoff = i + 1
    return s[:cutoff] + "..."

print(truncate_text("The quick brown fox"))
print(truncate_text("The fast striped zebra"))