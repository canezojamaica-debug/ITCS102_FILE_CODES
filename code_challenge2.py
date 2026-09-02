money = eval(input("Enter Money to DEPOSIT ----->>>"))
print(type(money))
print("================================= PH BANK DENOMINATION ====================================== ")
print("MONEY TO DEPOSIT ---------------------> ", money, "php")


oth = money // 1000
oth_change = money % 1000

fvh = oth_change // 500
fvh_change = oth_change % 500

twh = fvh_change // 200
twh_change = fvh_change % 200 

oneh = twh_change // 100
oneh_change = twh_change % 100

fty = oneh_change // 50
fty_change = oneh_change % 50 

tty = fty_change // 20
tty_change = fty_change % 20

ten = tty_change // 10
ten_change = tty_change % 10

five = ten_change // 5
five_change = ten_change % 5

piso = five_change 

print()
print("\n\t1000 -", oth)
print("\t500 -",fvh)
print("\t200 -",twh)
print("\t100 -",oneh)
print("\t50 -",fty)
print("\t20 -",tty)
print("\t10 -",ten)
print("\t5 -" , five)
print("\t1 -", piso)


print("===================================== END OF DENOMINATION =======================================")
