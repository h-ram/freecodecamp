def explode_fizzbuzz(target_z_count):
    letters = list("fizzbuzz")
    steps = 0
    while letters.count('z') < target_z_count:
        steps += 1
        new_letters = []
        for i, letter in enumerate(letters, start=1):
            if i % 15 == 0:
                new_letters.extend("fizzbuzz")
            elif i % 3 == 0:
                new_letters.extend("fizz")
            elif i % 5 == 0:
                new_letters.extend("buzz")
            else:
                new_letters.append(letter)
        letters = new_letters
    return steps

print(explode_fizzbuzz(9))
print(explode_fizzbuzz(15))
print(explode_fizzbuzz(51))
print(explode_fizzbuzz(52))