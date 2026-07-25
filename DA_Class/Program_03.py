pin = 2324
balance = 19023343434

print("""What services you want to use:
        1. Withdraw
        2. Deposit
        3. See Balace
        """)

enteredoption = int(input("Choose an option: "))

if enteredoption == 1:
    enterpin = int(input("Enter your pin: "))
    if enterpin == pin:
        howmuch = int(input("How much amount you want to withdraw: "))
        if balance < howmuch:
            print("You don't have enough money to withdraw")
        else:
            balance = balance - howmuch
            print(f"""Thank you for Visiting
                    Withdrawn amount : {howmuch} Rs.
                    Remaining balance: {balance} Rs.
                    """)
    else:
        print("You Pin is wrong, your account is blocked!!")
        
elif enteredoption == 2:
    enterpin = int(input("Enter your pin: "))
    if enterpin == pin:
        howmuch = int(input("How much amount you want to deposit: "))
        if howmuch > 0:
            balance = balance + howmuch
            print(f"""Thank you for Visiting
                            Deposited amount : {howmuch} Rs.
                            Updated balance: {balance} Rs.
                            """)
    else:
        print("You Pin is wrong, your account is blocked!!")

elif enteredoption == 3:
    enterpin = int(input("Enter your pin: "))
    if enterpin == pin:
     print(f"""Thank you for Visiting
             Your Balace is : {balance} Rs
                    """)
    else:
            print("You Pin is wrong, your account is blocked!!")

     
    

        
    
                
    