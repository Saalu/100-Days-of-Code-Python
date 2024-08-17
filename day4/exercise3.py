print("Welcome to your Exciting Rollercoster")
height = int(input("What is your height? "))


if height > 120:
    print("Great! You can ride")
    age = int(input("What is your age?"))
    bill = 0
    if age < 12:
        print("Please pay $5")
    if 12 <= age  < 18:
        print("Please pay $7")
    if age >= 18:
        print("Please pay $12")
else:
    print("Please you cannot ride with us")