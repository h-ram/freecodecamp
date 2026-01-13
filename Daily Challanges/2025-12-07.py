def compress_string(sentence):
    compressed = ""
    words = sentence.split(" ")
    previous_word = words[0]
    count = 1
    for i in range(1, len(words)):
        if words[i] == previous_word:
            count += 1
        else:
            if count > 1:
                compressed += f"{previous_word}({count}) "
            else:
                compressed += f"{previous_word} " 
            count = 1
        previous_word = words[i]
    
    if count == 1:
        compressed += f"{previous_word}" 
    else:
        compressed += f"{previous_word}({count})"
        
    return compressed


test1 = compress_string("yes yes yes please")
test2 = compress_string("I have have have apples")
test3 = compress_string("one one three and to the the the the")
test4 = compress_string("route route route route route route tee tee tee tee tee tee")


check1 = "yes(3) please"
check2 = "I have(3) apples"
check3 = "one(2) three and to the(4)"
check4 = "route(6) tee(6)"

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")