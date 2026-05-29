def fizz_buzz_count(start, end):
    counts = {
        "fizz": 0, 
        "buzz": 0
    }
    for num in range(start, end+1):
        if num%3==0 :
            counts["fizz"] += 1
        if num%5==0 :
            counts["buzz"] += 1
    return counts

print(fizz_buzz_count(1, 11))