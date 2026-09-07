#basic if else program

username = "Xividi"
password = "xivxyvy"

u = input("Input USERNAME ---> ")
p = input("Input PASSWORD ---> ")



if u == username and p == password:
	print("Hello",username,"!")
else: 
	print("access denied")
	print("incorrect username or password")
