def get_movie_night_cost(day, showtime, number_of_tickets):
    total_cost = 0
    ticket_cost = 12.00 if day in {"Friday", "Saturday", "Sunday"} else 10.00
    hour, _ = map(int, showtime[:-2].split(':'))
    meridiem = showtime[-2:]
    if not (hour >= 5 and meridiem == "pm") and day != "Tuesday":
        ticket_cost -= 2.00
    if day == "Tuesday":
        total_cost = number_of_tickets * 5.00
    else:
        total_cost = ticket_cost * number_of_tickets
    return f"${total_cost:.2f}"

print(get_movie_night_cost("Saturday", "10:00pm", 1))
print(get_movie_night_cost("Tuesday", "7:20pm", 2))
print(get_movie_night_cost("Wednesday", "5:40pm", 3))