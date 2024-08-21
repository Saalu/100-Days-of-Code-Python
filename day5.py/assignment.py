print("Welcome to Pizza Special\nWe have Small(S)-15 Medium(M)-$20 or Large(L)-$25 ")


size = input("What pizza size do you prefer? S, M, or L: ")
cheese = input("Do you want extra cheese? Y or N: ")
pepperoni = input("Do you want pepperoni?  Y or N: ")
  
bill = 0
# How much to pay base on sizes
if size == "S":
    bill += 15
    print("Please pay $15")
elif size == "M":
    bill += 20
    print("Please pay $20")
elif size == "L":
    bill += 25
    print("Please pay $25")
else:
    print("You typed a wrong pizza size: S-Small, M-Medium or L-Large ")

 


