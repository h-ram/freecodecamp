def fizz_buzz(num):
    answer = ""
    if num % 3 == 0:
        answer += "Fizz"
    if num % 5 == 0:
        answer += "Buzz"
    return answer or num


def is_fizz_buzz(arr):
    start = None
    n = len(arr)
    for i in range(n):
        if type(arr[i]) == int:
            start = arr[i] - i
            break

    for i in range(n):
        if arr[i] != fizz_buzz(start):
            return False
        start += 1
    return True


print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz"]))
print(is_fizz_buzz([13, 14, "FizzBuzz", 16, 17]))
print(is_fizz_buzz([1, 2, "Fizz", 4, 5]))
