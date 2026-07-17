def get_tally_count(s):
    return s.count("|") + s.count("/")


print(get_tally_count("||||"))
print(get_tally_count("||||/"))
print(get_tally_count("||||/ |||"))
print(get_tally_count("||||/ ||||/ ||||/ ||"))
print(get_tally_count("||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ |"))
