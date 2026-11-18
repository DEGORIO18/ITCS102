amnt = float(input("Enter your loan amount ---> ?"))
years = int(input("Enter years to pay --->"))
month = years * 12

rem_bal = amnt
principal = amnt  / month


#for loop 
print(" | MONTH\t|\tPAYMENT\t\t|\tINTEREST\t|\tPRINCIPAL\t|\tBALANCE\t|")
for count in range(1,month + 1):
    rem_bal -=principal
    interest = rem_bal *0.00256
    pay = interest + principal 
    #print(count,round(pay,2),round(interest, 2,round(principal,2),round(rem_bal,2))
    print(f"| {count}\t|t\{round(pay,2)}\t\t|\t{round(interest, 2)}\t\t|\t{round(principal,2)}\t\t|\t{round(rem_bal,2)}\t\t|")
    
    
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 