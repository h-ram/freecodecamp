def get_longest_chain(dominoes):
    def search(last, used):
        best = []
        for i, d in enumerate(dominoes):
            if i not in used:
                for tile in [d, d[::-1]]:
                    if tile[0] == last:
                        rest = search(tile[1], used | {i})
                        if len(rest) + 1 > len(best):
                            best = [tile] + rest
        return best

    best = []
    for i, d in enumerate(dominoes):
        for tile in [d, d[::-1]]:
            result = [tile] + search(tile[1], {i})
            if len(result) > len(best):
                best = result
    return best

print(get_longest_chain([[1, 2], [4, 5], [2, 3]]))
print(get_longest_chain([[2, 1], [4, 3], [5, 3]]))