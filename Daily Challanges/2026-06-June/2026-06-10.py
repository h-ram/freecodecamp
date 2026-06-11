from math import factorial


def getItineraryCount(stops):
    n = len(stops)
    return (2 * n - 3) * factorial(n)


print(getItineraryCount(["library", "park"]))
print(getItineraryCount(["library", "park", "arcade"]))
print(getItineraryCount(["library", "park", "arcade", "store"]))
print(getItineraryCount(["library", "park", "arcade", "store", "cafe"]))
print(
    getItineraryCount(
        ["library", "park", "arcade", "store", "cafe", "market", "museum"]
    )
)
