def get_semifinal_matchups(teams):
    scores = []
    for team in teams:
        name, record = team.split(":")
        points = record.split("-")
        scores.append((name,int(points[0]) * 3 + int(points[1]) * 2 + int(points[2])))
    scores.sort(key=lambda item: item[1], reverse=True)

    result = f"The semi-final games will be {scores[0][0]} vs {scores[3][0]} and {scores[1][0]} vs {scores[2][0]}."

    return result

test1 = get_semifinal_matchups(["CAN: 2-2-0-1", "FIN: 2-2-1-0", "GER: 1-0-1-3", "SUI: 0-1-3-1", "SWE: 1-1-2-1", "USA: 2-1-0-2"])
test2 = get_semifinal_matchups(["CAN: 2-1-1-1", "CZE: 1-1-1-2", "FIN: 1-2-1-1", "NOR: 0-1-1-3", "SLO: 1-0-1-3", "USA: 5-0-0-0"])
test3 = get_semifinal_matchups(["CAN: 3-2-0-0", "CZE: 2-1-2-0", "LAT: 0-0-1-4", "ITA: 1-1-1-2", "DEN: 1-0-0-4", "USA: 3-1-1-0"])
test4 = get_semifinal_matchups(["AUT: 2-2-1-0", "DEN: 1-0-0-4", "ITA: 1-1-1-2", "JPN: 3-2-0-0", "KOR: 2-1-2-0", "LAT: 0-0-1-4"])

check1 = "The semi-final games will be FIN vs SWE and CAN vs USA."
check2 = "The semi-final games will be USA vs CZE and CAN vs FIN."
check3 = "The semi-final games will be CAN vs ITA and USA vs CZE."
check4 = "The semi-final games will be JPN vs ITA and AUT vs KOR."

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")