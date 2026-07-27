def play_game(p1, p2):
    score1 = 0
    score2 = 0

    for i in range(len(p1)):
        if p1[i] == "C" and p2[i] == "C":
            score1 += 3
            score2 += 3
        elif p1[i] == "D" and p2[i] == "D":
            score1 += 1
            score2 += 1
        elif p1[i] == "D":
            score1 += 5
        else:
            score2 += 5

    return [score1, score2]


print(play_game("CCCC", "CCCC"))
print(play_game("DDDD", "DDDD"))
print(play_game("CCDD", "CDDD"))
print(play_game("CCCDCDCCCDDC", "CCDDCDCDDCCD"))
print(play_game("DDCCDDDDCDDCDDDCDD", "CCDCCCDCCCDCCCCDCC"))