#Task 1

loanA = float(input("Enter the loan amount: $"))
loanP = int(input("Enter the loan period in years: "))

interest_rate = 0.0025
principal = loanA / (12 * loanP)
remaining_balance = loanA

print("\nPayment Schedule")
print("Month\t | Monthly Payment\t | Interest\t | Principal\t | Remaining Loan")
print("-" * 100)

for x in range(1, 12 * loanP + 1):
    interest = remaining_balance * interest_rate
    monthly_payment = principal + interest
    remaining_balance = remaining_balance - principal

    if remaining_balance < 0.01:
        remaining_balance = 0

    print(f"{x}\t | ${monthly_payment:.2f}\t\t | ${interest:.2f}\t | ${principal:.2f}\t | ${remaining_balance:.2f}")

   
