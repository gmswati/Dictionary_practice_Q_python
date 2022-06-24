# from vscode import clear()
## hint: you can call clear() to clear the output in the console.

# from art import logo
# print(logo)


bids={}
bidding_finished=False


def find_highest_bidder(biddig_record):
    highest_bid=0
    # Winner=''
    for bidder in biddig_record:
        bid_amount=biddig_record[bidder]
    if bid_amount> highest_bid:
        highest_bid=bid_amount
        Winner=bidder
    print(f'the winner is {Winner} with the bid of {highest_bid}.')



while not bidding_finished :

    name=input('enter your name:')
    price=int(input('enter your bid amount:$'))
    bids[name]=price
    should_continue=input("are there any other bidders? Type 'yes' or 'no'.")
    if should_continue=='no':
        bidding_finished=True
    elif should_continue=='yes':
        # clear()
        pass

find_highest_bidder(bids)