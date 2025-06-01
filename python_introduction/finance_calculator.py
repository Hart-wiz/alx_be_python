# Everything here is monthly
userMonthlyIncome = float(input("Enter your monthly income: "))
userTotalMonthlyExpenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthlySavings = userMonthlyIncome - userTotalMonthlyExpenses

# Calculate projected savings after one year with 5% interest
annualSavings = monthlySavings * 12
projectedSavings = annualSavings + (annualSavings * 0.05)

# Print results
print("Your monthly savings are: ₦" + str(round(monthlySavings, 2)))
print("Projected savings after one year, with interest, is:" + str(round(projectedSavings, 2)))
