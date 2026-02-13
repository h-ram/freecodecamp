def space_jam(s):

    jam = [char.upper() for char in s if char != ' ']
    return "  ".join(jam)


test1 = space_jam("freeCodeCamp")
test2 = space_jam("   free   Code   Camp   ")
test3 = space_jam("Hello World?!")
test4 = space_jam("C@t$ & D0g$")
test5 = space_jam("allyourbase")

check1 = "F  R  E  E  C  O  D  E  C  A  M  P"
check2 = "F  R  E  E  C  O  D  E  C  A  M  P"
check3 = "H  E  L  L  O  W  O  R  L  D  ?  !"
check4 = "C  @  T  $  &  D  0  G  $"
check5 = "A  L  L  Y  O  U  R  B  A  S  E"

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")