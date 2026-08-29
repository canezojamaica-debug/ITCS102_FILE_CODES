money_to_deposit = 11935

ath = money_to_deposit // 1000
afh = money_to_deposit % 1000 // 500
atwh = money_to_deposit %1000 %500 // 200
aoh = money_to_deposit % 1000 % 500 % 200 // 100
aft = money_to_deposit %1000 % 500 % 200 % 100 //50	
atw = money_to_deposit %1000 %500 %200 %100 %50 // 20
at = money_to_deposit %1000 %500 %200 %100 %50 % 20 // 10
af = money_to_deposit % 1000 % 500 % 200 %100 % 50 % 20 % 10 // 5
ao = money_to_deposit % 1000 % 500 % 200 % 100 % 50 % 20 % 10 % 5 // 1


print("The amount of",money_to_deposit,"pesos consists of",ath,"one-thousand peso bills",afh,"five-hundred peso bill",atwh,"two-hundred peso bills",aoh,"one-hundred peso bill",aft,"fifty peso bill",atw,"twenty peso bill",at,"peso coin",af,"peso coin",ao,"peso coin.")