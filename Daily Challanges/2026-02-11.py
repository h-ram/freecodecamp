def compute_score(judge_scores, *penalties):
    sorted_scores = sorted(judge_scores)
    base_score = sum(sorted_scores[1:-1])
    for penalty in penalties:
        base_score -= penalty
    return base_score

test1 = compute_score([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1)
test2 = compute_score([10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
test3 = compute_score([10, 8, 9, 10, 9, 8, 8, 9, 10, 7], 1, 2, 1)
test4 = compute_score([8.0, 8.5, 9.0, 8.5, 9.0, 8.0, 9.0, 8.5, 9.0, 8.5], 0.5, 1.0)
test5 = compute_score([6.0, 8.5, 7.0, 9.0, 7.5, 8.0, 6.5, 9.5, 7.0, 8.0], 1.5, 0.5, 0.5)

check1 = 64
check2 = 80
check3 = 67
check4 = 67.5
check5 = 59

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")