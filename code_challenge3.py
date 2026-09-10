Sender_name = str(input("Enter the sender's name: "))

type_of_item = str(input("Enter the type of item: "))

is_fragile = str(input("Is the item fragile? (yes/no): "))

weight = float(input("Enter the weight of the item in kg: "))

distance = float(input("Enter the distance to be shipped in km: ")) 

is_express = str(input("Is express shipping required? (yes/no): "))    

is_international = str(input("Is the shipment international? (yes/no): ")) 

base_cost = (weight * 2.50) + (distance * 0.15) 

free_shipping = 0

International_express = (base_cost * 1.40) + 50

Express_or_Heavy_international = (base_cost * 1.20) + 25

Oversized = (base_cost + 30)

Standard_Rate = base_cost

if weight <= 2.0 and distance <= 100:
    print("Standard Rate")  
    print("The total shipping cost is: $", free_shipping)

elif is_express.lower() == "yes" or is_international.lower() == "yes" and weight > 20:
    print("Express or Heavy International")
    print("The total shipping cost is: $", Express_or_Heavy_international)

elif weight > 30 or distance > 1000:
    print("Oversized")
    print("The total shipping cost is: $", Oversized)

elif is_international.lower() == "yes" and is_express.lower() == "yes":
    print("International Express")
    print("The total shipping cost is: $", International_express)

else:
    print("Standard Rate")
    print("The total shipping cost is: $", base_cost) 
