balance = 1000
done = False
while done == False:   
    dow = input("Deposit or withdrawal: ")
    amount = int(input("Enter amount: "))
    if dow == "withdrawal":
        balance = balance - amount
        if balance < 0:
            print("You cannot have a negative balance!")
        else:
            print( "Final balance: " + str(balance))
    elif dow == "deposit":
        balance = balance + amount
        if balance < 0:
            print("You cannot have a negative balance!")
        else:
            print( "Final balance: " + str(balance))
    else:
        print("Invalid transaction. (did you spell correctly?)")
    done = bool(input("are you done? (True or False): "))
