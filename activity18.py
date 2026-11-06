yesali = True

while yesali == True:
    ask = input("Do you wish to continue this program (yes/no) ---> ")

    if ask.lower() == "yes":
        print("program continuing")
        continue
    else: 
        print("stopping now")
        break
