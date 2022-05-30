def game():
    ###################################################################################
    '''TicTacToe Game'''
    ###################################################################################
    '''Importing libraries'''
    import  random
    ###################################################################################

    print('WELCOME TO TIC TAC TOE GAME!')

    row1 = ["❌","❌","⭕"]
    row2 = ["❌","⭕","⭕"]
    row3 = ["⭕","⭕","❌"]
    all = [row1, row2, row3]
    print('', *row1, '\n', *row2, '\n', *row3)
    print('\n')
    print(
    '''
    Rules:
    To win, player must get their letters to match either:
    - Horizontally
    - Vertically
    - Diagonally

    After players choose his/her letter, who ever goes first would be chosen at random

    Possible moves are:
    For Top Row
    - TL (Top left)
    - TM (Top Middle)
    - TR (Top right)

    For Middle Row
    - ML (Middle left)
    - C (Center)
    - MR (Middle right)

    For bottom Row
    - BL (Bottom left)
    - BM (Bottom middle)
    - BR (Bottom right)

    ENJOY!😁
    '''
    )

    input('Start ▶ (Press Enter): ')
    ###################################################################################
    '''My functions'''
    ###################################################################################

    '''This function checks which move a player chose and if it is valid'''
    '''
    t- turn
    x_o_move - player x or o's move
    dict1_t - top moves
    dict1_m - middle moves
    dict1_b - botttom moves
    c - possible characters

    '''
    # char = '❌⭕❔'

    def play_move(t,x_o_move, dict1_t,dict1_m,dict1_b,c):
        if x_o_move in dict1_t.keys() and dict1_t[x_o_move] == c[2]:
            dict1_t[x_o_move] = t
        elif x_o_move in dict1_m.keys() and dict1_m[x_o_move] == c[2]:
            dict1_m[x_o_move] = t
        elif x_o_move in dict1_b.keys() and dict1_b[x_o_move] == c[2]:
            dict1_b[x_o_move] = t
        else:
            print('Invalid move')
            x_o_move = input(f' Please {t} Try elsewhere: ').lower()
            play_move(t,x_o_move, dict1_t,dict1_m,dict1_b,c)



    '''This function takes in the players move and changes turn to ❌ or ⭕'''
    def play(t,c,dict1_t, dict1_m,dict1_b):
        if t == c[0]:

            x = input(f' {t} Choose where: ').lower()
            play_move(t, x, dict1_t, dict1_m, dict1_b,c)
            t = c[1]
            print('\n')
            print(f' turn is {t}')
        elif t == c[1]:
            o = input(f'{t} Choose where: ').lower()
            play_move(t, o, dict1_t, dict1_m, dict1_b,c)
            t = c[0]
            print('\n')
            print(f' turn is {t}')
        print('',*dict1_t.values(), '\n', *dict1_m.values(),'\n',*dict1_b.values() )
        return t


    '''This function checks possible winning moves'''
    def check_win(c):
        checks = [[moves['top_moves']['tl'], moves['top_moves']['tm'], moves['top_moves']['tr']], 
        [moves['middle_moves']['ml'], moves['middle_moves']['c'], moves['middle_moves']['mr']], 
        [moves['bottom_moves']['bl'], moves['bottom_moves']['bm'], moves['bottom_moves']['br']], 
        [moves['top_moves']['tl'], moves['middle_moves']['ml'], moves['bottom_moves']['bl']], 
        [moves['top_moves']['tm'], moves['middle_moves']['c'], moves['bottom_moves']['bm']], 
        [moves['top_moves']['tr'], moves['middle_moves']['mr'], moves['bottom_moves']['br']], 
        [moves['top_moves']['tl'], moves['middle_moves']['c'], moves['bottom_moves']['br']], 
        [moves['top_moves']['tr'], moves['middle_moves']['c'], moves['bottom_moves']['bl']]]

        if list(c[0]) * 3 in checks:
            print(f'Congratulations!! {c[0]} wins 🎉🎉🎇🎇🎆')
            return c[0]
        elif list(c[1]) * 3 in checks:
            print(f'Congratulations!! {c[1]} wins 🎉🎉🎇🎇🎆')
            return c[1]

    ###################################################################################
    '''Main game'''
    ###################################################################################


    char = '❌⭕❔'
    
    r1 = ["❔",'|',"❔", '|', "❔"]
    r2 = ["❔",'|',"❔", '|', "❔"]
    r3 = ["❔",'|',"❔", '|', "❔"]
    


    moves = {
    'top_moves':  {
    'tl': r1[0],
    'tm': r1[2],
    'tr': r1[4],
    },

    'middle_moves': {
    'ml': r2[0],
    'c': r2[2],
    'mr': r2[4],
    },
    'bottom_moves':  {
    'bl': r3[0],
    'bm': r3[2],
    'br': r3[4]
    }}



    count = 0
    choices = {0: '❌', 1: '⭕'}
    turn = choices[random.randint(0,1)]

    print(f'{turn} plays first')
    print('\n')
    print('',*moves['top_moves'].values(), '\n', *moves['middle_moves'].values(),'\n',*moves['bottom_moves'].values() )



    while count < 9:
        turn = play(turn, char, moves['top_moves'], moves['middle_moves'], moves['bottom_moves'])
            
        count += 1
        if count == 9:
            print('DRAW! Game over! 😒😒')
            break
        winner = check_win(char)
        if winner == char[0]:
            break
        elif winner == char[1]:
            break
    answer = input('Would you like to play again?: Y/N: ').upper()
    if answer == 'Y':
        game()
    elif  answer =='N':
        print('Goodbye 👋👋👋')


from datetime import datetime
start_time = datetime.now()
game()
end_time = datetime.now()
print("--- %s microseconds ---" % (int(start_time.strftime("%f")) - int(end_time.strftime("%f"))))

