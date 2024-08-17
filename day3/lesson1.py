# conditionals - if/else, elif
# conditionals - if/else nested if/else
print("Rollercosta Event")
height = int(input("Please enter your height "))
if height >= 100:
    print("You can ride the rollercosta")
    age = int(input("What is your age? "))
    if age <= 12 :
        print("Please pay $5.")
    elif age <= 18 :
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you need to grow taller to ride")