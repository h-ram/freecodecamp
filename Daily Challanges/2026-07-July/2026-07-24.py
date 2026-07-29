def get_loan_schedule(amount, annual_rate, monthly_payment):
    balance = amount
    schedule = [round(balance)]
    monthly_rate = annual_rate / 100 / 12

    while balance > 0:
        balance += balance * monthly_rate
        balance -= monthly_payment

        if balance < 0:
            balance = 0

        schedule.append(round(balance))

    return schedule


print(get_loan_schedule(1000, 0, 200))
print(get_loan_schedule(1000, 5, 200))
print(get_loan_schedule(10, 50, 1))
print(get_loan_schedule(5500, 8, 400))
print(get_loan_schedule(50000, 5.2, 1650))