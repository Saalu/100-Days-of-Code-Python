print("Welcome to the Tip Calculator")
# returns a string
total_bill = float(input(("What was the total bill? ")))
tip = int(input(("How much tip would you like to give? 10, 12, or 15? ")))
split_bill = int(input(("How many people to split the bill? ")))
 
# This a float
tip_given = (float(tip )/ 100 ) 

final= (total_bill * tip_given + total_bill)/split_bill 
bill_per_head  = round(final,2)
print(f"Each person should pay: ${bill_per_head}")
