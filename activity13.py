name = input("Please input name:", "/n""First name:", "/n", "Last name:"
job = input("Please input job description:")


age = int(input("How old are you?---->   "))
is_employed = bool(input("Are you currently employed? (True/False)---->   "))
credit_score = int(input("What is your credit score?---->   "))
annual_income = float(input("What is your annual income?---->   "))
has_collateral = bool(input("Do you have Collateral?  (True/False)---->   ")) == "True"

#Baseline eligibilty criteria for loan approval and Tier 1
if age >= 21 and is_employed == True:
    print("You passed baseline eligibility")
    if credit_score >= 750:
        print("Your credit score is above 750")
        if annual_income >= 100000:
            print("You have a high annual income")
            base_rate = 4.5
            print("Hello", user, "you are eligible for a loan with an interest rate of", base_rate,"%")
        else:
            base_rate = 5.0
            print("Hi", user, "you are eligible for a loan with an interest rate of", base_rate,"%")
        
#Tier 2    
    elif  credit_score >= 600 and credit_score < 750:
        if has_collateral == True:
        base_rate = 7.0
        print("Hi", user, "you are eligible for a loan with an interest rate of", base_rate,"%")
        elif annual_income < 40000:
        base_interest_rate = 9.5
        print("Hi",user,"you are eligible for a loan with an interest rate of", base_rate,"%")
        else:
            base_rate = 8.0
            print("Hi", user, "you are eligible for a loan with an interest rate of", base_rate,"%")
     
#Tier 3 
if credit_score < 600:
  print("You are not eligible for a loan at this time. Rejected: Credit score too low.")    
