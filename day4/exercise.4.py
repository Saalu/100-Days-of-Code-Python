print("Welcome to Pizza Special")
size = int(input("What pizza size do you prefer? choose 1-small($15) 2-medium($20) or 3-larger($25)\n"))
price = 0
small = 15
if size == 1:
    price = 15
    print("Please pay $15")
    pepperoni = input("Do you want pepperoni?  yes or no")
    if pepperoni == "yes":
        print(f"Please your total bill is: ${price + 2}")
    else:
        print(f"Please your total bill is: ${price}")

    
elif size == 2:
    price = 20
    print("Please pay $20")
    pepperoni = input("Do you want pepperoni?  yes or no")
    if pepperoni == "yes":
        print(f"Please your total bill is: ${price + 2}")
    else:
        print(f"Please your total bill is: ${price}")

elif size == 3:
    price = 25
    print("Please pay $25")
    pepperoni = input("Do you want pepperoni?  yes or no")
    if pepperoni == "yes":
        print(f"Please your total bill is: ${price + 2}")
    else:
        print(f"Please your total bill is: ${price}")
