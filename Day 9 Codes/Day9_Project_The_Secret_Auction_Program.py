logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("\nWelcome to the Secret Auction Program.")


auction={}
bidding=True

def maxbid(bidvalue):
    highbid=0
    for i in bidvalue:
        bid_amt=bidvalue[i]
        if bid_amt > highbid:
            highbid=bid_amt
            winner=i
    print(f"The winner is {winner} and the highest bid is ${highbid}")

def bidteller(bidvalue):
    highbid=0
    for i in bidvalue:
        bid_amt=bidvalue[i]
        if bid_amt > highbid:
            highbid=bid_amt
    print(f"Current Highest Bid is ${highbid}")



while bidding:
    name=input("What is your name?: ")
    bid=int(input("What is your bid?: $"))
    auction[name]=bid
    bidteller(auction)
    a=input("Are there any other bidders? Type yes or no: ")
    if a=="no":
        bidding=False
        maxbid(auction)
    else:
        bidding=True

