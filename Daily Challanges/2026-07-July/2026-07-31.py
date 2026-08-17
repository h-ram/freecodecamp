def decode_morse(code):
    morse = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
        "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
        "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
        ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
        "--..": "Z"
    }

    words = code.split("   ")
    output = []

    for word in words:
        text = ""
        for letter in word.split():
            text += morse[letter]
        output.append(text)

    return " ".join(output)


print(decode_morse("--.."))
print(decode_morse("... --- ..."))
print(decode_morse("..-. .-. . . -.-. --- -.. . -.-. .- -- .--."))
print(decode_morse(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."))
print(decode_morse("- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. . -..   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --."))