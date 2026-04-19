def find_sum(arr, target):
    n = len(arr)

    def dfs(i, current_sum, path):
        if current_sum == target and len(path) >= 2:
            return path
        if i == n:
            return None
        res = dfs(i + 1, current_sum + arr[i], path + [arr[i]])
        if res:
            return res
        return dfs(i + 1, current_sum, path)

    result = dfs(0, 0, [])
    return result if result else "Sum not found"

print(find_sum([1, 3, 5, 7], 6))