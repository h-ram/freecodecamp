def add_punctuation(sentences):
    result = [sentences[0]]
    for i in range(1, len(sentences)):
        if sentences[i].isupper() and sentences[i-1] == ' ':
            result[-1] = '.'
            result.append(' ')
        result.append(sentences[i])
    result.append(".")
    result = "".join(result)
    return result

test1 = add_punctuation("Hello world")
test2 = add_punctuation("Hello world It's nice today")
test3 = add_punctuation("JavaScript is great Sometimes")
test4 = add_punctuation("A b c D e F g h I J k L m n o P Q r S t U v w X Y Z")
test5 = add_punctuation("Wait.. For it")

check1 = "Hello world."
check2 = "Hello world. It's nice today."
check3 = "JavaScript is great. Sometimes."
check4 = "A b c. D e. F g h. I. J k. L m n o. P. Q r. S t. U v w. X. Y. Z."
check5 = "Wait... For it."

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")