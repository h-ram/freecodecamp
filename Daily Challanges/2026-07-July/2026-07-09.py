def triage_issue(title, labels):
    t = title.lower()
    labels = labels[:]

    if not labels:
        if "error" in t or "bug" in t:
            labels.extend(["bug", "needs triage"])
        elif "feature" in t or "add" in t:
            labels.extend(["enhancement", "discussing"])
    else:
        if "needs triage" in labels:
            labels.remove("needs triage")
            if "simple" in t or "easy" in t:
                labels.append("good first issue")
            else:
                labels.append("help wanted")
        elif "discussing" in labels:
            labels.remove("discussing")
            if "planned" in t or "next" in t:
                labels.append("on the roadmap")
            else:
                labels.append("help wanted")

    if "security" in t and "critical" not in labels:
        labels.append("critical")

    return labels


print(triage_issue("app crashes with error", []))
print(triage_issue("app crashes with error", ["bug", "needs triage"]))
print(triage_issue("add dark mode", []))
print(triage_issue("add dark mode", ["enhancement", "discussing"]))
print(triage_issue("xss security bug", []))
print(triage_issue("security vulnerability in auth", []))
print(triage_issue("easy a11y fix", ["bug", "needs triage"]))
print(triage_issue("planned api migration", ["enhancement", "discussing"]))
print(triage_issue("improve security", ["enhancement", "discussing"]))
