age = int(input("How Old are you?---->   "))
is_employed = bool(input("Are you employed? True or False---->   ")) == "True"
credit_score = eval(input("What is your credit score?---->   "))
annual_income = eval(input("What is your annual income?---->   "))
has_collateral = bool(input("Do you have Collateral? True or False---->   ")) == "True"

#Baseline eligibilty criteria for loan approval and Tier 1
if age >= 21 and is_employed is True:
  if credit_score >= 750:
    baseline_interest_rate = 5
    if annual_income >= 100000:
      baseline_interest_rate = 4.5
      print("You are eligible for a loan with an interest rate of", baseline_interest_rate, "%")
    else:
        print("You are eligible for a loan with an interest rate of", baseline_interest_rate, "%")
else:
  print("You are not eligible for a loan at this time.")

#Tier 2 eligibility criteria for loan approval
if credit_score >= 600 and credit_score < 750:
  base_interest_rate = 8
  if has_collateral == True:
    base_interest_rate = 7
    print("You are eligible for a loan with an interest rate of", base_interest_rate,  "%")
  elif has_collateral == False and annual_income < 40000:
    base_interest_rate = 9.5
    print("You are eligible for a loan with an interest rate of", base_interest_rate,  "%")
  else:
    print("You are eligible for a loan with an interest rate of", base_interest_rate,  "%")


#Tier 3 eligibility criteria for loan approval
if credit_score < 600:
  print("You are not eligible for a loan at this time. Please work on improving your credit score and try again later.")