print("Welcome to tip calculator")
bill = round(float(input("What was the total bill ₹")),2)
tip = int(input("What percentage tip would you like to give?10, 12 or 15?"))
persons = int(input("How many people to split the bill?"))
total_bill = (bill * tip / 100) + bill
share = round((total_bill / persons),2)
print(f"Each person should pay: ₹{share}")