def get_mood(genre, bpm):
    if 60 <= bpm <= 109 and genre == "classical":
        return "focus"
    elif 60 <= bpm <= 89 and genre == "electronic":
        return "focus"
    elif 60 <= bpm <= 180 and genre == "pop":
        return "happy"
    elif 110 <= bpm <= 180 and genre == "classical":
        return "happy"
    elif 60 <= bpm <= 129 and genre == "rock":
        return "happy"
    elif 90 <= bpm <= 134 and genre == "electronic":
        return "happy"
    elif 130 <= bpm <= 180 and genre == "rock":
        return "hype"
    elif 135 <= bpm <= 180 and genre == "electronic":
        return "hype"
    return "Unknown"


print(get_mood("rock", 111))
print(get_mood("electronic", 74))
print(get_mood("classical", 180))
print(get_mood("rock", 155))
print(get_mood("electronic", 90))
print(get_mood("classical", 67))
print(get_mood("pop", 100))
print(get_mood("electronic", 135))
