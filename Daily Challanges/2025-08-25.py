def to_camel_case(s):
    camelCase = ""
    upper_next = False

    for c in s:
        if c in "-_ ":
            upper_next = True
        else:
            if upper_next:
                camelCase += c.upper()
                upper_next = False
            else:
                camelCase += c.lower()
                
    return camelCase


test1 = to_camel_case("hello world")
test2 = to_camel_case("HELLO WORLD")
test3 = to_camel_case("secret agent-X")
test4 = to_camel_case("FREE cODE cAMP")
test5 = to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk")

check1 = "helloWorld"
check2 = "helloWorld"
check3 = "secretAgentX"
check4 = "freeCodeCamp"
check5 = "yeOldSeaFaringBuccaneerWithAPegLegAndAParrotNamedSquawk"

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")