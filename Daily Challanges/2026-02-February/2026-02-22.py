def count_medals(winners):
    csv = "Country,Gold,Silver,Bronze,Total\n"
    countries = {}
    for event in winners:
        g,s,b = event
        if g not in countries:
            countries[g] = [0,0,0];
        if s not in countries:
            countries[s] = [0,0,0];
        if b not in countries:
            countries[b] = [0,0,0];
        countries[g][0] += 1
        countries[s][1] += 1
        countries[b][2] += 1
    
    countries = dict(sorted(countries.items(), key=lambda k: (-k[1][0],k[0])))

    for country, medals in countries.items():
        g,s,b = medals
        total = g+s+b
        csv += f"{country},{g},{s},{b},{total}\n"
    csv = csv.strip('\n')
    return csv

test1 = count_medals([
    ["USA", "CAN", "NOR"],
    ["NOR", "USA", "CAN"],
    ["USA", "NOR", "SWE"]
])

test2 = count_medals([
    ["NOR","SWE","FIN"]
])

test3 = count_medals([
    ["ITA", "CHN", "CHN"],
    ["JPN", "ITA", "JPN"]
])

test4 = count_medals([
    ["USA","CAN","NOR"],
    ["GER","FRA","ITA"],
    ["JPN","KOR","CHN"],
    ["SWE","FIN","NOR"],
    ["CAN","USA","SWE"],
    ["FRA","GER","ITA"]
])

test5 = count_medals([
    ["ESP","ITA","FRA"],
    ["ITA","ESP","GER"],
    ["NOR","SWE","FIN"],
    ["FIN","NOR","SWE"],
    ["USA","CAN","MEX"],
    ["CAN","USA","MEX"],
    ["JPN","KOR","CHN"],
    ["CHN","JPN","KOR"]
])

test6 = count_medals([
    ["USA","CAN","GER"],
    ["NOR","SWE","FIN"],
    ["USA","NOR","SWE"],
    ["GER","FRA","ITA"],
    ["JPN","KOR","CHN"],
    ["USA","GER","CAN"],
    ["SWE","NOR","FIN"],
    ["CAN","USA","NOR"],
    ["FRA","GER","ITA"],
    ["JPN","CHN","KOR"],
    ["SWE","FIN","NOR"],
    ["GER","ITA","FRA"]
])

check1 = "Country,Gold,Silver,Bronze,Total\nUSA,2,1,0,3\nNOR,1,1,1,3\nCAN,0,1,1,2\nSWE,0,0,1,1"
check2 = "Country,Gold,Silver,Bronze,Total\nNOR,1,0,0,1\nFIN,0,0,1,1\nSWE,0,1,0,1"
check3 = "Country,Gold,Silver,Bronze,Total\nITA,1,1,0,2\nJPN,1,0,1,2\nCHN,0,1,1,2"
check4 = "Country,Gold,Silver,Bronze,Total\nCAN,1,1,0,2\nFRA,1,1,0,2\nGER,1,1,0,2\nJPN,1,0,0,1\nSWE,1,0,1,2\nUSA,1,1,0,2\nCHN,0,0,1,1\nFIN,0,1,0,1\nITA,0,0,2,2\nKOR,0,1,0,1\nNOR,0,0,2,2"
check5 = "Country,Gold,Silver,Bronze,Total\nCAN,1,1,0,2\nCHN,1,0,1,2\nESP,1,1,0,2\nFIN,1,0,1,2\nITA,1,1,0,2\nJPN,1,1,0,2\nNOR,1,1,0,2\nUSA,1,1,0,2\nFRA,0,0,1,1\nGER,0,0,1,1\nKOR,0,1,1,2\nMEX,0,0,2,2\nSWE,0,1,1,2"
check6 = "Country,Gold,Silver,Bronze,Total\nUSA,3,1,0,4\nGER,2,2,1,5\nJPN,2,0,0,2\nSWE,2,1,1,4\nCAN,1,1,1,3\nFRA,1,1,1,3\nNOR,1,2,2,5\nCHN,0,1,1,2\nFIN,0,1,2,3\nITA,0,1,2,3\nKOR,0,1,1,2"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")

