
######################################################################################################################################
# My functions

#To check for currency
def check_currency(curr):
    if curr in usd_exchange_rate.keys():
        return curr
    else:
        guest_currency = input(f'You have entered an invalid choice; prefered currency: {list(usd_exchange_rate.keys())} ').upper()

###########################################################################################################################################

#To check for number range
def num_range(num):
    if num < 1 or num > 10:
        guest_number = int(input('You are out of range, please choose from 1 -10: '))
    else:
        return num

#################################################################################################################################################################
#check for each count

def check_game(c, g_num, hst):
    check_dict = {0:50, 1:25, 2:5}
    for key in check_dict.keys():
        if c == key and g_num == hst:
            amt = check_dict[key]
            winnings = convert(amt)
            print(f"Congrats, host chose {hst}, You have won {guest_currency} {winnings}")
            break
        else:
            if c >=2 and g_num != hst:
                amt = 75
                winnings = convert(amt)
                print(f"You have lost, host chose {hst}, please pay the host {guest_currency} {winnings}")
                print('Game Over!')
                break


################################################################################################################################################################

#conversion rate
def convert(cost):
    for key in usd_exchange_rate.keys():
        if key == guest_currency:
            winnings = usd_exchange_rate[key] * cost
            return round(winnings)  

        
################################################################################################################################################################33

import random

print('Welcome to guessing game!')
usd_exchange_rate = {'USD': 1, 'GBP': 0.76, 'JYP': 123.82, 'NGN': 415.72}

host = random.randint(1,10)


guest_currency = input(f'Hello player, please Enter your prefered currency: {list(usd_exchange_rate.keys())} ').upper()
check_currency(guest_currency)
print(host)
guest_number = int(input('Please guess a number from 1 -10: '))
num_range(guest_number)

count = 0
while count <= 2:
    check_game(count, guest_number, host)

    if guest_number == host:
        break
    elif count >=2:
        break
    else:
        if count == 1:
            guest_number = int(input(f'You have {2 - count} try left, Please take another guess: '))
        else:
            guest_number = int(input(f'You have {2 - count} tries left, Please take another guess: '))
        count+=1      
