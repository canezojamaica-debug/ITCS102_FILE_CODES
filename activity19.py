import getpass

islogin = False
loginattempts = 0

username = "Xividui" 
password = "Xivxyvy"

while not islogin:
    uname = input("Enter your username: ")
    passw = getpass.getpass("Enter your password: ")
    if uname == username and passw == password:
        islogin = True
        print("Login successful!")
    else:
        loginattempts += 1
        print("Invalid username or password. Please try again.")
        if loginattempts >= 3:
            print("Too many failed login attempts. Please try again later.")
            break
