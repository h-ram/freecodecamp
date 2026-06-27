from collections import Counter

def triage_blood(inventory, requests):
    blood = Counter(inventory)
    served = 0

    for t in ["O", "A", "B", "AB"]:
        while blood["O"] > 0 and requests.count(t) > 0:
            break

    need = Counter(requests)

    x = min(blood["O"], need["O"])
    served += x
    blood["O"] -= x
    need["O"] -= x

    x = min(blood["A"], need["A"])
    served += x
    blood["A"] -= x
    need["A"] -= x

    x = min(blood["O"], need["A"])
    served += x
    blood["O"] -= x
    need["A"] -= x

    x = min(blood["B"], need["B"])
    served += x
    blood["B"] -= x
    need["B"] -= x

    x = min(blood["O"], need["B"])
    served += x
    blood["O"] -= x
    need["B"] -= x

    for d in ["AB", "A", "B", "O"]:
        x = min(blood[d], need["AB"])
        served += x
        blood[d] -= x
        need["AB"] -= x

    return f"{served} of {len(requests)} patients served"


print(triage_blood(["O", "A", "B", "AB"], ["O", "A", "B", "AB"]))
print(triage_blood(["A", "A", "B", "B", "AB"], ["O", "A", "B", "B", "B"]))
print(triage_blood(["O", "A", "B", "AB"], ["AB", "AB", "AB", "AB", "AB"]))
print(triage_blood(["O", "O", "O", "O", "O"], ["O", "A", "B", "AB"]))
print(triage_blood(["A", "O", "B", "AB", "B", "AB", "O", "A", "A"], ["O", "A", "B", "AB", "A", "B", "A", "A", "B", "A", "B"]))
print(triage_blood(["O", "B", "AB", "AB", "O", "A", "A", "AB", "O", "B", "B", "AB", "A", "B", "AB"], ["O", "A", "B", "B", "A", "B", "AB", "A", "B", "A", "O", "AB", "AB", "O"]))