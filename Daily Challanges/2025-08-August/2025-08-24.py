def strength(c):
    if 'a' <= c <= 'z':
        return ord(c) - 96
    if 'A' <= c <= 'Z':
        return ord(c) - 64 + 26
    if c.isdigit():
        return int(c)
    return 0


def battle(my_army, opposing_army):

    if len(my_army) > len(opposing_army):
        return "Opponent retreated"
    if len(my_army) < len(opposing_army):
        return "We retreated"

    my_wins = 0
    opp_wins = 0

    for m, o in zip(my_army, opposing_army):
        m_s = strength(m)
        o_s = strength(o)

        if m_s > o_s:
            my_wins += 1
        elif o_s > m_s:
            opp_wins += 1

    if my_wins > opp_wins:
        return "We won"
    if opp_wins > my_wins:
        return "We lost"
    return "It was a tie"


test1 = battle("Hello", "World")
test2 = battle("pizza", "salad")
test3 = battle("C@T5", "D0G$")
test4 = battle("kn!ght", "orc")
test5 = battle("PC", "Mac")
test6 = battle("Wizards", "Dragons")
test7 = battle("Mr. Smith", "Dr. Jones")

check1 = "We lost"
check2 = "We won"
check3 = "We won"
check4 = "Opponent retreated"
check5 = "We retreated"
check6 = "It was a tie"
check7 = "It was a tie"

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
print(f"Test6: {test6==check6}")
print(f"Test7: {test7==check7}")

