def get_greeting(s):
    h, m = map(int, s.split(':'))
    if  5 <= h < 12:
        return "Good morning"
    if 12 <= h < 18:
        return "Good afternoon"
    if 18 <= h < 22:
        return "Good evening"
    return "Good night"

print(get_greeting("06:30"))
print(get_greeting("12:00"))
print(get_greeting("21:59"))
print(get_greeting("00:01"))
print(get_greeting("11:30"))