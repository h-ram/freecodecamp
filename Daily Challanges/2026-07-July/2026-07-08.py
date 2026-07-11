def triage_issue(milliseconds, last_message):
    if milliseconds < 604800000:
        return "leave it"
    if "bump" in last_message.lower():
        return "close it"
    return "bump it"


print(triage_issue(86400000, "Lets fix it"))
print(triage_issue(1209600000, "still waiting"))
print(triage_issue(864000000, "bump"))
print(triage_issue(604800000, "Do we still want this?"))
print(triage_issue(604800000, "Bumping this"))
print(triage_issue(345600000, "I'll make a PR"))