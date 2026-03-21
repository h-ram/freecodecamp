def rotate(g):
    return ["".join(g[5-j][i] for j in range(6)) for i in range(6)]

def valid(g):
    def block(i, j):
        return all(g[i+x][j+y] == '1' for x in range(2) for y in range(2))
    return block(0,0) and block(0,4) and block(4,0)


def decode_qr(qr_code):
    for _ in range(4):
        if valid(qr_code):
            result = []
            for i in range(6):
                for j in range(6):
                    if (i < 2 and j < 2) or (i < 2 and j >= 4) or (i >= 4 and j < 2):
                        continue
                    result.append(qr_code[i][j])
            return "".join(result)
        qr_code = rotate(qr_code)

print(decode_qr(["110011", "110011", "000000", "000000", "110000", "110001"]))