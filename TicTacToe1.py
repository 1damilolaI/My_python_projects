import random
# print('WELCOME TO TIC TAC TOE GAME!')

# row1 = ["❌","❌","⭕"]
# row2 = ["❌","⭕","⭕"]
# row3 = ["⭕","⭕","❌"]
# all = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# print('\n')
# print(
# '''
# Rules:
# To win, player must get their letters to match either:
# - Horizontally
# - Vertically
# - Diagonally

# After players choose his/her letter, who ever goes first would be chosen at random

# Possible moves are:
# For Top Row
# - TL (Top left)
# - TM (Top Middle)
# - TR (Top right)

# For Middle Row
# - ML (Middle left)
# - C (Center)
# - MR (Middle right)

# For bottom Row
# - BL (Bottom left)
# - BM (Bottom middle)
# - BR (Bottom right)

# ENJOY!😁
# '''
# )

# input('Start ▶ (Press Enter): ')

#################################################################################
'''This function checks if the player made a valid choice'''
#################################################################################

def check_choice(choice):
    choices = ['X','O']
    if choice not in choices:
        choice = input('Please choose either X or O: ').upper()        
        choice = check_choice(choice)
    return choice
###################################################################################################
'''This function assigns either X or O to second player, depending on what first player chooses'''
#######################################################################################################

def new_choice(choice, choice2):
    if choice == 'X':
        # print(choice)
        choice2 ='O' 
    else:
        choice2 = 'X'
       
    return choice2

###########################################################################################
'''This function inputs the move/position
    p - Move
    ct - check_t
    cm -check_m
    cb -check_b
'''
############################################################################################

def play(p,ct,cm,cb,w,turn):
    if p in ct.keys() and ct[p] == '⬜️':
        ct[p] = turn
        
    elif p in cm.keys() and cm[p] == '⬜️':
        cm[p] = turn
        
    elif p in cb.keys() and cb[p] == '⬜️':
        cb[p] = turn
        
    else:
        p = input(f'Wrong move! try else where: ').lower()
        play(p,ct,cm,cb,w,turn)   
    return win(turn,w)

#############################################################################
'''This function checks for a winner using possible winning combinations'''
#############################################################################

def win(p_choice, w):
    
    test = [
    list(check_t.values()), list(check_m.values()), 
    list(check_b.values()), 
    [check_t['tl'], check_m['ml'], check_b['bl']], 
    [check_t['tm'], check_m['c'], check_b['bm']], 
    [check_t['tr'], check_m['mr'], check_b['br']],
    [check_t['tl'], check_m['c'], check_b['br']],
    [check_b['bl'], check_m['c'], check_t['tr']],
    [check_t['tr'], check_m['c'], check_b['bl']]
    ]

    w = None
    
    if [p_choice] *3 in test:
        print(f'{list(check_t.values())}\n{list(check_m.values())}\n{list(check_b.values())}' )
        w = p_choice
        
    else:
        print(f'{list(*check_t.values())}\n{list(check_m.values())}\n{list(check_b.values())}' )
        
    return w


#####################################################################################
'''Main game starts'''
################################################################################


player1 = input('Welcome player, please enter your name: ').title()

player2 = input(f'Who is playing against {player1}: ').title()

player1_choice = input(f'Hello {player1}, please choose, X or O: ').upper()
player1_choice = check_choice(player1_choice)
print(check_choice(player1_choice))

player2_choice = None
player2_choice = new_choice(player1_choice, player2_choice)


print(f'{player2}, you are {player2_choice}')


print('\n')
letters = {0:'X', 1:'O'}
turn = letters[random.randint(0,1)]
print(f'{turn} goes first')
print('\n')


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
all = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
print('', * all[0],'\n',*all[1],'\n',*all[2])

check_t = {
'tl': all[0][0],
'tm': all[0][1],
'tr':all[0][2]
}
check_m = {
'ml' : all[1][0],
'c' : all[1][1],
'mr' : all[1][2]
}
check_b = {
'bl' : all[2][0],
'bm' : all[2][1],
'br' : all[2][2],
}

def rnd(player1_choice, player2_choice,turn):
    count = 0
    winner = None

    while count < 9:
        if winner == player1_choice:
            print(f'Congratulations {player1} 🎉🎉🎇🎇🎆 {player1_choice} wins!')
            break
        elif winner == player2_choice:
            print(f'Congratulations {player2} 🎉🎉🎇🎇🎆 {player2_choice} wins!')
            break
        
        position = input(f'{turn} Choose where to play: ').lower()
        
        print(f'turn is {turn}')
        print(f'player 1 choice is {player1_choice}')
        print(f' player 2 choice is {player2_choice}')

        if turn == player1_choice:
            print()
            winner = play(position, check_t, check_m, check_b, winner,turn)    
            turn = player2_choice      
        
        elif turn == player2_choice:
            winner = play(position, check_t, check_m, check_b, winner, turn)
            turn = player1_choice

        if count >= 8:
            print('DRAW! Game over! 😒😒')
            restart = input('Play again? Y/N ')
            if restart == 'Y':
                print('\n')
                letters = {0:'X', 1:'O'}
                turn = letters[random.randint(0,1)]
                print(f'{turn} goes first')
                print('\n')


               
                rnd(player1_choice, player2_choice,turn)
            elif restart == 'N':
                break
        else:
            count += 1




rnd(player1_choice, player2_choice,turn)



