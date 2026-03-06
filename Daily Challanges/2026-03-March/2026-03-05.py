def smallest_gap(s):
    smallest_substring = s
    for i in range(len(s) - 1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                substring = s[i+1:j]
                n = len(substring)
                m = len(smallest_substring)
                if n < m:
                    smallest_substring = substring
    return smallest_substring

test1 = smallest_gap("ABCDAC")
test2 = smallest_gap("racecar")
test3 = smallest_gap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4")
test4 = smallest_gap("Hello World")
test5 = smallest_gap("The quick brown fox jumps over the lazy dog.")

check1 = "DA"
check2 = "e"
check3 = "#q6e&rkf(p"
check4 = ""
check5 = "fox"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")