#import demo 
import getpass

username = "Xividi"
password = "xivxyvy"

u = input("Input USERNAME ---> ")
p = getpass.getpass("Input PASSWORD ---> ")



if u == username and p == password:
	print("Hello",username,"!")
else: 
	print("access denied")
	print("incorrect username or password")
