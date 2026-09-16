import sys
import getpass

name = input("Input USERNAME ---> ")
password = getpass.getpass("Input PASSWORD ---> ")

username = "Xiv Hiroo"
correct_password = "xividi123"

if name == username and password == correct_password:
  print("Hello", name, "!")
else:
  print("access denied")
  print("incorrect username or password")
  sys.exit()

job = input("Please input job description: ")
collateral = input("Please input name/description of collateral (e.g motorcycle, land, house, etc.): ")
value_of_collateral = float(input("Please input value of collateral: "))

if value_of_collateral < 30000:
  print("Collateral value is too low. You are not eligible for a loan at this time.")
  sys.exit()

age = int(input("How old are you?---->   "))
if age > 65:
  print("You are not eligible for a loan at this time. Rejected: Age exceeds maximum limit.")
  sys.exit()
  
is_employed = input("Are you currently employed? (Yes/No)---->   ").strip().lower() == "yes"
credit_score = int(input("What is your credit score?---->   "))
annual_income = float(input("What is your annual income?---->   "))
has_collateral = bool(input("Do you have Collateral? (Yes/No)---->   ").strip().lower() == "yes") 

# Baseline eligibility criteria for loan approval and tiers.
if age >= 21 and is_employed:
    print("You passed baseline eligibility")

    if credit_score >= 750:
      print("Your credit score is above 750")

      if annual_income >= 100000:
        print("You have a high annual income")
        base_rate = 4.5
      else:
        base_rate = 5.0

      print("Hello", username, "you are eligible for a loan with an interest rate of", base_rate, "%")

    elif credit_score >= 600: #tier 2
      print("Your credit score is between 600 and 749")

      if has_collateral:
        base_rate = 7.0
      elif annual_income < 40000:
        base_rate = 9.5
      else:
        base_rate = 8.0

      print("Hi", username, "you are eligible for a loan with an interest rate of", base_rate, "%")

    else:
      print("You are not eligible for a loan at this time. Rejected: Credit score too low.")

else:
    print("You are not eligible for a loan at this time. Rejected: Fails baseline eligibility criteria.")
