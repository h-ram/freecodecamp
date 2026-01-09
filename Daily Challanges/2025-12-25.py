def generate_snowflake(crystals):
    lines = crystals.split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i] + lines[i][::-1]
    return "\n".join(lines)


test1 = generate_snowflake("* \n *\n* ")
test2 = generate_snowflake("X=~")
test3 = generate_snowflake(" X  \n  v \nX--=\n  ^ \n X  ")
test4 = generate_snowflake("*   *\n * * \n* * *\n * * \n*   *")
test5 = generate_snowflake("*  -\n * -\n*  -")

check1 = "*  *\n ** \n*  *"
check2 = "X=~~=X"
check3 = " X    X \n  v  v  \nX--==--X\n  ^  ^  \n X    X "
check4 = "*   **   *\n * *  * * \n* * ** * *\n * *  * * \n*   **   *"
check5 = "*  --  *\n * -- * \n*  --  *"


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")