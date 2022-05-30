
##############################################################################################################################
'''Function to check if game continues or not'''
##############################################################################################################################

def game_decision(decision):
    if decision == 'N':
        print('Goodbye, come again soon 👋👋')
        return decision
        
    elif decision == 'Y':
        choose_game(choose_game)
        return decision
    else:
        decision = input('Invlaid response, Would You like to play another game? Y/N: ').upper()
        return game_decision(decision)
    
##############################################################################################################################
'''Rock Paper Scissors Function'''
##############################################################################################################################

def rockpapersci():
    #############################################################################
    #checks both options

    def check(p_1, p_2,option1, option2):
        if option1 == option2:
            print('Draw! Play again')
        elif (option1 == 'Rock' and option2 == 'Scissors') or (option1 == 'Paper' and option2 == 'Rock') or (option1 == 'Scissors' and option2 == 'Paper') :
            print('\n')
            print(f'{option1} wins!')
            print(f'Congratulations {p_1} 🎉🎉')
            return p_1
        else:
            print('\n')
            print(f'{option2} wins!')
            print(f'Congratulations {p_2} 🎉🎉') 
            return p_2   

####################################################################################
    #checks if option chosen is valid

    def check_correct(optn, player):
        options = ['Rock','Paper','Scissors']
        if optn in options:
            return optn
        else:
            optn = input(f'{player} Wrong choice, please choose, Rock, Paper or Scissors?: ').title()
            return check_correct(optn, player)
###############################################################################################            
#GAME STARTS
    print('WELCOME TO ROCK 🗻, PAPER 📃, SCISSORS! ✂️')
    print('''
    Rules:
    Type either Rock, Paper or Scissors to choose
    To win:
    - Rock crushes Scissors
    - Paper covers Rock
    - Scissors cuts Paper
    Enjoy 😉

    ''')
    player1 = input('Hello player, what is your name?: ').title()
    player2 = input(f'Who is playing against {player1}?: ').title()

    count = 0
    while count >=0:
        player1_option = input(f'{player1} Choose, Rock, Paper or Scissors?: ').title()
        player1_option = check_correct(player1_option, player1)
    
        player2_option = input(f'{player2} Choose, Rock, Paper or Scissors?: ').title()
        player2_option = check_correct(player2_option, player2)
        
        winner = check(player1, player2, player1_option, player2_option)

        if winner == player1 and winner != None:
            looser = player2
        else:
            looser = player1

        if player1_option == player2_option:
            count += 1
        else:
            break
        
    return winner, looser

##############################################################################################################################
'''GUESSING GAME FUNCTION'''
##############################################################################################################################

def guessinggame(host,player):
    ######################################################################################################################################
    # Guessing game inner functions

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

    def check_game(c, g_num, hst_num, hst, gst):
        check_dict = {0:50, 1:25, 2:5}
        for key in check_dict.keys():
            if c == key and g_num == hst_num:
                amt = check_dict[key]
                winnings = convert(amt)
                print(f"Congrats, {gst} 🤩, {hst} chose {hst_num}, You have won {guest_currency} {winnings} 🤑")
                break
            else:
                if c >=2 and g_num != hst_num:
                    amt = 75
                    winnings = convert(amt)
                    print(f" Sorry {gst} you lost 😔😔, {hst} chose {hst_num}, please pay {guest_currency} {winnings}")
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
    # Game starts

    print('''Welcome to Guessing Game 🤓🤓
    Rules: 
    - Host gets to pick a number between 1 and 10
    - Guest will have 3 tries to guess the Host's number

    - If Guest guesses right on the first try, Guest wins in his/her preferred currency an equivalent of USD 50
    - If Guest guesses right on the second try, Guest wins in his/her preferred currency an equivalent of USD 25
    - If Guest guesses right on the third try, Guest wins in his/her preferred currency an equivalent of USD 5

    -- If after 3 tires Guest guesses wrong, Host wins in his/her preferred currency an equivalent of USD 75

    Enjoy 😉
    ''')

    input('Press Enter to Start >>')

    usd_exchange_rate = {'USD': 1, 'GBP': 0.76, 'JYP': 123.82, 'NGN': 415.72}

    print('\n')
    host_currency = input(f'Congarts {host}, You are host, please Enter your prefered currency: {list(usd_exchange_rate.keys())} ').upper()
    check_currency(host_currency)
    host_number = int(input(f'{host} Please Enter a number from 1 -10: '))
    num_range(host_number)

  

    guest_currency = input(f'Hello {player}, you are Guest, please Enter your prefered currency: {list(usd_exchange_rate.keys())} ').upper()
    check_currency(guest_currency)

    guest_number = int(input(f"{player} Please guess {host}'s number: "))
    num_range(guest_number)

    count = 0
    while count <= 2:
        check_game(count, guest_number, host_number, host, player)

        if guest_number == host_number:
            break
        elif count >=2:
            break
        else:
            if count == 1:
                guest_number = int(input(f' {player} You have {2 - count} try left, Please take another guess: '))
            else:
                guest_number = int(input(f' {player} You have {2 - count} tries left, Please take another guess: '))
            count+=1      

#######################################################################################################################
'''MAIN GAME FUNCTION'''
#######################################################################################################################

print('WELCOME TO GAME WORLD 🌎🌏🌏')

cont = True
while cont == True:

    games = {1: 'Rock Paper Scissors', 2: 'Guessing Game'}

    chosen_game = int(input(f'Choose a a number for a game: {games}: '))


    def choose_game(game_choice):
            if game_choice == 1:
                rockpapersci()
            elif game_choice == 2:
                print('''To play Guessing game, you must play Rock Paper Scissor
The Winner becomes Host for guessing game''')
                print('\n')
                ans = input('Proceed? Y/N: ').upper()
                if ans == 'Y':
                    print('\n')
                    winner_loser = rockpapersci()
                    print('\n')
                    guessinggame(winner_loser[0], winner_loser[1])
                elif ans == 'N':
                    game_choice = int(input(f'Choose a Game you would like to play: {games}: '))
                    choose_game(game_choice)
                else:
                    game_choice = int(input(f'Invalid choice!, please Choose a Game you would like to play: {games}: '))
                    choose_game(game_choice)


    choose_game(chosen_game)
    gamer_decision = input('Would You like to play another game? Y/N: ').upper()
    gamer_decision = game_decision(gamer_decision)
    print(gamer_decision)
    if gamer_decision == 'N':
        cont = False

    