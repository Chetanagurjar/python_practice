print("Welcome To ATM......")
set_pin=12345
pin=int(input("Enter the pin:- "))
if(set_pin==pin):
    print("Correct Pin")
    balance=10000
    amt=int(input("Entre the withdraw Amount:- "))
    if(amt<=balance):
       if(amt<=balance-500):
           print(amt,"Is succesfully Transfer") 
           print("Remaining balance is:- ",balance-amt)
       else:
            print("Minimum 500rs")
    else:
         print("Insuf. Balance")
else:
   print("Incorrect pin")