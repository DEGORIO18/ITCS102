
name = input("Input NAME ---> ")
age = int(input("Input AGE ---> "))

print("Hi,", name, "That age is considered as:")

if 1 <= age <= 5:
    print("infant")
elif 6 <= age <= 12:
    print("kid")
elif 13 <= age <= 19:
    print("teenager")
elif 20 <= age <= 29:
    print("early adult")
elif 30 <= age <= 48:
    print("adult")
elif 49 <= age <= 59:
    print("advance adult")
elif 60 <= age <= 150:
    print("senior")
else:
    print("invalid")