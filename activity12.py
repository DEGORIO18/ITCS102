import getpass

username = 'degorio1'
password = 'iwankosayo'

u = input("Enter username ----> ")
p = getpass.getpass("Enter password ----> ")

if username == u and password == p:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")

