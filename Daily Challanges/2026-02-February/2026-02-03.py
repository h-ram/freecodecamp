def mirror(s):
    return s + s[::-1]

test1 = mirror("freeCodeCamp")
test2 = mirror("RaceCar")
test3 = mirror("helloworld")
test4 = mirror("The quick brown fox...")

check1 = "freeCodeCamppmaCedoCeerf"
check2 = "RaceCarraCecaR"
check3 = "helloworlddlrowolleh"
check4 = "The quick brown fox......xof nworb kciuq ehT"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
