from art import logo

print(logo)


def highest_bid (bidding_dictionary):
    winner= ""
    highestbid_tillnow= 0

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highestbid_tillnow:
            highestbid_tillnow = bid_amount
            winner = bidder

    print(f"the winner is {winner} with a bid of {highestbid_tillnow}")


bids={}
biding_ends= True


while biding_ends:
    name = input(print("enter your Name : \n"))
    bid_amount = int(input(print("Enter your bid amount: $\n")))
    bids[name] = bid_amount
    should_continue = input(print("do you want to continue 'yes' or 'No' \n")).lower()
    if should_continue == "no":
        biding_ends= False
        highest_bid(bids)
    elif should_continue == "yes":
        print("\n" *55)



def highest_bid (bidding_dictionary):
    winner= ""
    highestbid_tillnow= 0

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highestbid_tillnow:
            highestbid_tillnow = bid_amount
            winner = bidder


    print(f"the winner is {winner} with a bid of {highestbid_tillnow}")
