bidders = {}

def max_bid(bidders_dict):
    max_element = -1
    for value in bidders_dict.values():
        if value > max_element:
            max_element = value

    for key, value in bidders_dict.items():
        if max_element == value:
            return key, value


while True:
    name = str(input("What is your name?: "))
    bid_price = int(input("Whats your bid? : $ "))
    bidders[name] = bid_price
    yes_no = str(input("Is there anyone else in the room (yes/no): "))
    if yes_no.lower() == 'no':
        break
    else:
        print("\n" * 100)

print(f"The max bidder is : {max_bid(bidders)[0]} and amount is {max_bid(bidders)[1]}")
