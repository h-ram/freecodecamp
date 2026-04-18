def decode(message):
    n = len(message)
    KEY = "VLHCGMDLNH"
    decoded = []
    key_index = 0
    for i in range(n):
        char = message[i]
        if char.isalpha():
            shift_size = ord(KEY[key_index % len(KEY)]) - ord('A') + 1
            decoded_val = (ord(char) - ord('A') - shift_size) % 26
            decoded.append(chr(decoded_val + ord('A')))
            key_index += 1
        else:
            decoded.append(char)
            
    return "".join(decoded)

print(decode("YAVJYNXE"))
print(decode("YALLUT PQUMJP"))
print(decode("UAC DYR EISAKYM"))
print(decode("GQMS NBMZU"))
print(decode("W IQQURV UG I ZDMDTRV IVW JQDHY TMHSA QB"))