def email_chain_count(subject):

    subject = subject.lower()

    fw = subject.count("fw:")
    fwd = subject.count("fwd:")
    re = subject.count("re:")

    return fw + fwd + re


test1 = email_chain_count("Re: Meeting Notes")
test2 = email_chain_count("Meeting Notes")
test3 = email_chain_count("Re: re: RE: rE: Meeting Notes")
test4 = email_chain_count("Re: Fwd: Re: Fw: Re: Meeting Notes")
test5 = email_chain_count("re:Ref:fw:re:review:FW:Re:fw:report:Re:FW:followup:re:summary:Fwd:Re:fw:NextStep:RE:FW:re:Project:Fwd:Re:fw:Notes:RE:re:Update:FWD:Re:fw:Summary")

check1 = 1
check2 = 0
check3 = 4
check4 = 5
check5 = 23


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")