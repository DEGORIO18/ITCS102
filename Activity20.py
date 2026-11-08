from getpass import getpass

isLogin = True

while isLogin == True:
    username = input("Input username ")
    password = getpass("Input password ")

    if username == "Andoy" and password == "ikaw lang sapat na":
        print("Access Granted")
        isLogin = True 
    else:
        print("Access Denied. Try Again.")