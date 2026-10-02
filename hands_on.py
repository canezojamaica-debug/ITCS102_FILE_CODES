

age = int(input("Input age -->"))
monthly_rev = float(input("Input monthly revenue --> "))
credit_score = int(input("Input credit score --> "))
yrs_business = float(input("Input Years in Business -->"))
has_defaults = input("Default History --> ")

if has_defaults.lower == "yes" or "true":
    print("Default history --> rejected")
elif has_defaults.lower == "no" or "false":
    print("Default history --> accepted")



collateral = input("Input Collateral Name --> ")
collateral_value = float(input("Input collateral value --> "))

max_loan = 0
base_rate = 0.0
#baseline
if age >= 21 and yrs_business >= 2.0 and has_defaults == False:
    print("Baseline Eligibility Passed")
    #tier1
    if credit_score >= 720:
        max_loan = monthly_rev * 3
        print("Credit Score is High")

        if monthly_rev >= 50000:
            base_rate = max_loan * 0.015
            print("Base fee rate is -->", base_rate)
            print("Approved Loan -->",max_loan)
        else:
            base_rate = max_loan * 0.025
            print("Base fee rate is -->", base_rate)
            print("Approved Loan -->",max_loan)

        #collateral conditions 
        if collateral_value >= max_loan: 
            print("Collateral", collateral, "---> Accepted")
        else:
            print("Collateral not accepted")

        #surcharge conditions
        surcharge = max_loan * base_rate
        if (int(collateral_value) % 5000 != 0):
            surcharge = 250
            print("a", surcharge, "surcharge is added")
        else:
            surcharge = 0        
    elif 620 <= credit_score < 720: #tier2
        max_loan = monthly_rev * 1.5
        print("Maximum Loan limit is -->", max_loan)
        if yrs_business >= 5.0:
            base_rate = max_loan * 0.02
            print("Base fee rate is -->", base_rate)
            print("Approved Loan -->",max_loan)
        else:
            base_rate = monthly_rev * 0.035
            print("Base fee rate is -->", base_rate)
            print("Approved Loan -->", max_loan)

        #collateral conditions  
        if collateral >= max_loan:
            print("Collateral", collateral, "---Accepted")
        else:
            print("Collateral not accepted")

        #surcharge conditions 
        surcharge = max_loan * base_rate
        if (int(collateral_value) % 5000 != 0):
            surcharge = 250
            print("a", surcharge, "surcharge is added")
        else:
            surcharge = 0                    
    elif credit_score < 620: #tier3
        print("Rejected: Credit score below requirement")       
    else:
        print("Rejected")   
else:
    print("Rejected: High risk application or ineligible owner")   

    
