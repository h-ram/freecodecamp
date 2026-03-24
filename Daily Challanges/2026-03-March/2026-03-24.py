def passing_count(scores, passing_score):
    count = sum(1 for score in scores if score >= passing_score)
    return count

print(passing_count([90, 85, 75, 60, 50], 70))