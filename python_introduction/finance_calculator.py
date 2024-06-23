

monthly_income = input("Enter your monthly income: ")
tx_monthly_expenses = input("Enter your total monthly expenses: ")
monthly_savings = int(monthly_income) - int(tx_monthly_expenses)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly savings are ${}.".format(monthly_savings))
print("Projected savings after one year, with interest, is: ${:.0f}.".format(
    projected_savings))
