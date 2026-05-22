def i_before_e(sentence):
    corrected = []
    i = 0
    while i < len(sentence):
        if i == len(sentence) - 1:
            corrected.append(sentence[i])
            break
        if sentence[i : i + 2] == "ei" and (
            i != 0 and sentence[i - 1] != "c" or i == 0
        ):
            corrected.append("ie")
            i += 1
        elif sentence[i : i + 2] == "ie" and i != 0 and sentence[i - 1] == "c":
            corrected.append("ei")
            i += 1
        else:
            corrected.append(sentence[i])
        i += 1
    return "".join(corrected)


print(i_before_e("beleive"))
print(i_before_e("recieve"))
print("we recieved relief after the theif gave us a breif piece of feirce deceit")
print(
    i_before_e(
        "we recieved relief after the theif gave us a breif piece of feirce deceit"
    )
)
print("we received relief after the thief gave us a brief piece of fierce deceit")
