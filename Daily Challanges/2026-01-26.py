def fizz_buzz_mini(n):
    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"

    return result or str(n)
    # python returns the first truthy value in an OR statment


test1 = fizz_buzz_mini(3)
test2 = fizz_buzz_mini(4)
test3 = fizz_buzz_mini(35)
test4 = fizz_buzz_mini(75)
test5 = fizz_buzz_mini(98)

check1 = "Fizz"
check2 = "4"
check3 = "Buzz"
check4 = "FizzBuzz"
check5 = "98"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
