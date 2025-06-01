# Everything here is monthly
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses



# Calculate projected savings after one year with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Print results
print("Your monthly savings are:" + str(round(monthly_savings, 2)))
print("Projected savings after one year, with interest, is:" + str(round(projected_savings, 2)))
