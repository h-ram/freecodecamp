def get_milestone(years):
    if years < 1:
        return "Newlyweds"
    elif years < 5:
        return "Paper"
    elif years < 10:
        return "Wood"
    elif years < 25:
        return "Tin"
    elif years < 40:
        return "Silver"
    elif years < 50:
        return "Ruby"
    elif years < 60:
        return "Gold"
    elif years < 70:
        return "Diamond"
    else:
        return "Platinum"