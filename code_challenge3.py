Sender_name = str(input("Enter the sender's name: "))

type_of_item = str(input("Enter the type of item: "))

is_fragile = input("Is the item fragile? (yes/no): "))

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
    print(\t,"Your item will be shipped with a Standard Rate") 
    print("Sender Name:", Sender_name, \n, "Type of Item:", type_of_item,\n,"Is the item fragile?", is_fragile,\n, "Item weight is:", weight, \n, "will be shipped in", distance, "km"
    print("The total shipping cost is: $", free_shipping)

elif is_express.lower() == "yes" or is_international.lower() == "yes" and weight > 20:
    print(\t, "Your item will be shipped as Express or Heavy International")
    print("Sender Name:", Sender_name, \n, "Type of Item:", type_of_item,\n,"Is the item fragile?", is_fragile,\n, "Item weight is:", weight, \n, "will be shipped in", distance, "km"
    print("Express or Heavy International")
    print("The total shipping cost is: $", Express_or_Heavy_international)

elif weight > 30 or distance > 1000:
    print()
    print("Sender Name:", Sender_name, \n, "Type of Item:", type_of_item,\n,"Is the item fragile?", is_fragile,\n, "Item weight is:", weight, \n, "will be shipped in", distance, "km"
    print("Oversized")
    print("The total shipping cost is: $", Oversized)

elif is_international.lower() == "yes" and is_express.lower() == "yes":
    print()
     print("Sender Name:", Sender_name, \n, "Type of Item:", type_of_item,\n,"Is the item fragile?", is_fragile,\n, "Item weight is:", weight, \n, "will be shipped in", distance, "km"
    print("International Express")
    print("The total shipping cost is: $", International_express)

else:
    print("Sender Name:", Sender_name, \n, "Type of Item:", type_of_item,\n,"Is the item fragile?", is_fragile,\n, "Item weight is:", weight, \n, "will be shipped in", distance, "km"
    print("Standard Rate")
    print("The total shipping cost is: $", base_cost) 
