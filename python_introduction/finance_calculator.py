
# everything here is monthly
userMonthlyIncome =int(input("Enter your monthly income:"))
userTotalMonthlyExpenses =int(input("Enter your total monthly expenses: "))

monthlySavings = userMonthlyIncome - userTotalMonthlyExpenses



projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)


print("Your monthly savings are "+str(monthlySavings))
print("Projected savings after one year, with interest, is: "+str(projectedSavings))