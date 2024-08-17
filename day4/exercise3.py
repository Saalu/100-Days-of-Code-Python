print("Welcome to your Exciting Rollercoster")
height = int(input("What is your height? "))


if height > 120:
    print("Great! You can ride")
    age = int(input("What is your age?"))
    bill = 0
    if age < 12:
        bill = 5
        print("Please pay $5")
    if 12 <= age  < 18:
        bill = 7
        print("Please pay $7")
    if age >= 18:
        bill = 12
        print("Please pay $12")
    want_photo = input("Do you want a photo take? Y for yes and N for No: 134")
    if want_photo == "Y":
        # print("Please add $3")
        print(f"Okay. Your total bill is {bill + 3}")
else:
    print("Please you cannot ride with us")