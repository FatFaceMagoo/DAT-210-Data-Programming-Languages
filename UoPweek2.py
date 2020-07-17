#int first input
while True:
    try:
        first = int(input("Please enter an integer \n"))
        print("Thank You")
        break
    except ValueError:
        print("Not an integer. Please try again")

#int second input
while True:
    try:
        second = int(input("Please enter another integer: \n"))
        print("Thank You")
        break
    except ValueError:
        print("Not an integer. Please try again")

if first < second:
    x = first
    y = second
else:
    x = second
    y = first


while x < y:
    print("x Value is " + str(x))
    x = x + 2
    z = x + y
    print("Z value is " + str(z) + "\n")