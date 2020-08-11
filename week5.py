items_to_convert = {
    "Travel Costs": 0,
    "Hotel Costs": 0,
    "Rental Car Costs": 0,
    "Labor Costs": 0
}
def costs():
#Travel Cost
    while True:
        try:
            travelCost = float(input("Travel Cost: $ "))
            #print("$" + (format(travelCost, '.2f')))
            travelCostAUD = travelCost * 1.394
            items_to_convert["Travel Costs"] = travelCostAUD
            break
        except ValueError:
            print("Try again")
#Hotel Cost
    while True:
        try:
            hotelCost = float(input("Hotel Cost: $ "))
            #print("$" + (format(hotelCost, '.2f')))
            hotelCostAUD = hotelCost * 1.394
            items_to_convert["Hotel Costs"] = hotelCostAUD
            break
        except ValueError:
            print("Try again")
#Rental Car Cost
    while True:
        try:
            rentalCarCost = float(input("Rental Car Cost: $ "))
            #print("$" + (format(rentalCarCost, '.2f')))
            rentalCarCostAUD = rentalCarCost * 1.394
            items_to_convert["Rental Car Costs"] = rentalCarCostAUD
            break
        except ValueError:
            print("Try again")
#Labor Cost
    while True:
            try:
                laborCost = float(input("Labor Cost: $ "))
                #print("$" + (format(laborCost, '.2f')))
                laborCostAUD = laborCost * 1.394
                items_to_convert["Labor Costs"] = laborCostAUD
                break
            except ValueError:
                print("Try again")


costs()
print(" ")
print(" ")

for x, y in items_to_convert.items():
  print("Your " + x + " exchanged to AUD are: $" + format(y, '.2f'))

