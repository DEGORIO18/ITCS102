#age ("integer")
#is_employed ("boolean")
# credit_score ("float")
# annual_income ("float")
# has_colateral ("boolean")






age =int(input("enter your age >"))
is_employed = bool(input("are your currently employed ----> "))
credit_score = float(input("what is your credit score ---->"))
annual_income = float(input("what is your annual income ---->"))
has_colateral = bool(input("do you have colateral (True/False)>"))

if age >-21 and is_employed == True:
    print("pwede")
    if credit_score >=750 and is_employed == True:
     print("you have high credit score")
     if annual_income >= 100000:
        base_rate = 4.5
    print("your base rate is", base_rate)
    