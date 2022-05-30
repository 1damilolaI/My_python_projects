import os
def names(dict_):
   
   bidder_name = input('Hello bidder, whats your name?: ').title()
   bid = int(input(f' {bidder_name} enter your amount in $: '))
   dict_.setdefault(bidder_name, bid)
   return dict_

print('Welcome to Silent Auction 🤫🤫')
print('\n')
bidders ={}
bidders = names(bidders)

choices = ['Y', 'N']

decision = input('Would anyone else like to make a bid? Y/N: ').upper()
while decision not in choices:
    decision = input('Please choose a valid answer Y/N: ').upper()

while decision == 'Y':
    os.system('cls')
    bidders = names(bidders)      
    decision = input('Would anyone else like to make a bid? Y/N: ').upper()

winning_bid = 0
for key,value in bidders.items():
    if value > winning_bid:
        winning_bid = value
        name = key
os.system('cls')
   
print(f'Winner of the silent auction is {name}, with a winning bid of ${winning_bid} 🤑🤑') 

