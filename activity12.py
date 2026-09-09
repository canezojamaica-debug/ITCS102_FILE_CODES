#Multiple if anf elif conditions 

#Create a python program that would capture age group 

Name = input("Please put your name --->")

age = int(input("Please put your age --->"))

if age >= 0 and age <= 5 :

	print("That age is considered an INFANT")

elif age >= 6 and age <= 12 : 

	print("That age is considered a KID")

elif age >= 13 and age <= 15 :
 
	print("That age is considered a PRE-TEEN")

elif age >= 16 and age <= 19 :

	print("That age is considered a TEENAGER")

elif age >= 20 and age <= 29 :
	print("That age is considered an EARLY ADULT")

elif age >= 30 and age <= 58 :
	print("That age is considered an ADULT")

elif age >= 58 :
	print("That age is considered a SENIOR")

else:
	print("age invalid")