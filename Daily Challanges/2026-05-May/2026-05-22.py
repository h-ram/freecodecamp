def get_meeting_time(availability):
    common = [[0, 24]]
    for person in availability:
        new_common = []
        for c_start, c_end in common:
            for p_start, p_end in person:
                start = max(c_start, p_start)
                end = min(c_end, p_end)
                if end - start >= 1:
                    new_common.append([start, end])
        common = new_common
        if not common:  
            return "None"
    return common[0][0] if common else "None"

print(get_meeting_time([[[7, 8], [10, 12], [13, 15]], [[8, 11], [12, 13], [14, 15]], [[6, 7], [8, 9], [12, 13]]]))