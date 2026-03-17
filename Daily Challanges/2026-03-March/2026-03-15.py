STARTING_POINTS = 8 * 1 + 5 * 2 + 3 * 2 + 3 * 2 + 9 * 1
PIECE_POINTS = {"K": 0, "P": 1, "N": 3, "B": 3, "R": 5, "Q": 9}


def get_captured_value(pieces):
    if "K" not in pieces:
        return "Checkmate"
    current_points = sum(PIECE_POINTS[piece] for piece in pieces)
    return STARTING_POINTS - current_points


print(get_captured_value(["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"]))
