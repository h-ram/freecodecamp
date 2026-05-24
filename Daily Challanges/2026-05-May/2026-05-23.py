def get_open_issues(issues, prs):
    def rotations(s):
        return {s[i:] + s[:i] for i in range(len(s))}
    def closes(issue, pr):
        a = str(issue)
        b = str(pr)
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)
        if a == b:
            return False
        return b in rotations(a)
    open_issues = []
    for issue in issues:
        closed = False
        for pr in prs:
            if closes(issue, pr):
                closed = True
                break
        if not closed:
            open_issues.append(issue)
    return open_issues


print(get_open_issues([123, 234], [231]))
print(get_open_issues([123, 345, 16], [345, 231]))