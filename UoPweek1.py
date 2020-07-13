#Account number   
while True:
    try:
        acctNum = int(input("Please enter a number: \n"))
        if acctNum > 999999999:
            print("Oops!  That was not a valid number.  Try again...")
            #x = int(input("Please enter a number: "))
        elif acctNum < 100000000:
            print("Oops!  That was not a valid number.  Try again...")
            #x = int(input("Please enter a number: "))
        else:
            print("Success")
            break
    except ValueError:
        print("Oops!  That was not a valid number.  Try again...")


#Balance
while True:
    try:
        balance = float(input("Please enter your balance: "))
        if balance < 0.0:
            print("Sorry. You broke!!")
            balance = 0
            break
        else:
            print("Your balance for account ending in **** is $" + format(balance, '.2f'))
            break
    except ValueError:
        print("Oops!  That was not a valid number.  Try again...")

#Item Cost
while True:
    try:
        cost = float(input("Please enter Item price: "))
        if cost < 0.1:
            print("enter the real price")
        else:
            print("The price of your item is $" + format(cost, '.2f'))
            break
    except ValueError:
        print("Oops!  That was not a valid number.  Try again...")

#Credit Limit
while True:
    try:
        limit = float(input("Please enter your credit limit: "))
        if limit < 0.1:
            print("Enter a positive credit limit")
        else:
            print("Your credit limit is $" + format(limit, '.2f'))
            break
    except ValueError:
        print("Oops!  That was not a valid number.  Try again...")

balanceAfterPurchase = balance + cost

print("Your balance is $" + format(balanceAfterPurchase, '.2f') + (" after making your purchase"))

if limit - balanceAfterPurchase > 0:
    print("Approved")
else:
    print("Denied")
