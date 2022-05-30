
def rockpapersci():
    #############################################################################
    #checks both options

    def check(p_1, p_2,option1, option2):
        if option1 == option2:
            print('Draw! Play again')
        elif (option1 == 'Rock' and option2 == 'Scissors') or (option1 == 'Paper' and option2 == 'Rock') or (option1 == 'Scissors' and option2 == 'Paper') :
            print(f'{option1} wins!')
            print(f'Congrats {p_1}')
            return p_1
        else:
            print(f'{option2} wins!')
            print(f'Congrats {p_2}') 
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




rockpapersci()