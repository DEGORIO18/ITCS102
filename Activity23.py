#jeepney simulator 
route = ("SM1","Palengke","Perez Park") 
passenger = []
SEATS = 6 
FARE = 13 
total = 0 


while True:
    print()
    print("Sakay:", passenger)
    print(len(passenger), "of", SEATS, "seats")
    print( "1 Sakay 2 priority seat 3 para po !")
    print("5 Baba harap  4 Baba pinto")
    print("6 Seats Cheak 7 Balikan 8 Exit ")
    choice = input ("Choice:")
    
    if choice == "1" :
        if len(passenger) == SEATS :
            print("Puno na po !") 
        else:
            name = input ("Name:")  
            passenger.append(name)
            total = total + FARE
            print(name, "boarded at the back")
            
            
    elif choice == "2":
        if len(passenger) == SEATS :
            print("Puno na po !")
        else:
            name = input ("Name:")
            passenger.insert (0,name)
            total = total + FARE
            print(name,"took priority seat")
            
            
    elif choice == "3"  :
            name = input("who is getting of ?")
            if name in passenger:
                passenger.remove (name )
                print(name,"got off  ingat po kayo ! ")
            else:
                print(name, "is not on jeep ")
                
                
    elif choice == "4"   :
              if len(passenger ) == 0 :
                  print("The jeep is empty ")
              else:
                  left = passenger.pop(0)
                  print(left,"got of the door ")
                  
    elif choice == "5"  :
               if len(passenger) == 0 :
                  print("The jeep is empty")
               else:
                   front = passenger.pop(0)
                   print("front,got off the front")
                   
                   
                   
    elif choice == "6" :
                 for i  in range(len(passenger )):
                     print("Seats", 1 + 1, passenger[1])
                     
                     
    elif choice == "7" :
                 route.reverse()
                 print("route:",route)
                
    elif choice == "8" :
                     print("Total fare today :",total)
                     break
                     
    else:
                     print("invalid choice")
                     
                     
                     
                 
                   
                   
              
                  
                  
              
            
            
          
            
            
            
        
      
        
        