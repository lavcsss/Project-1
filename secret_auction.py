# Secret aution 
from replit import clear

flag = True

while flag:
    name = input("What is your name")
    bid_value = int(input("Enter your bid: ₹"))
    bidder_information = {}
    bidder_information[name] = bid_value
    next_bid = input("Are there any other bidders? Type 'yes' or 'no' ")
    clear()
    if next_bid == "no":
        flag = False
max_bid = max(bidder_information)
print(f"The winner is {max_bid} with a bid of ₹{bidder_information[max_bid]}")
