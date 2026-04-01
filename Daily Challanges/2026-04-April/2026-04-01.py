def fix_prank_number(nums):
    n = len(nums)
    diffs = [nums[i + 1] - nums[i] for i in range(n - 1)]
    step = max(set(diffs), key=diffs.count)

    for i in range(n - 1):
        if diffs[i] != step:
            for bad in [i, i + 1]:
                result = nums[:]
                result[bad] = (
                    result[bad - 1] + step if bad > 0 else result[bad + 1] - step
                )
                if all(result[j + 1] - result[j] == step for j in range(n - 1)):
                    return result

    return nums[:]
