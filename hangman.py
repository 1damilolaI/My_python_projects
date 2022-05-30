def hang():
    import random


    hangman = {
        0: ''' 
        ________
        |      |
        |
        |
        |
        |
        -----''',
        
        1: ''' 
        ________
        |      |
        |      O
        |
        |
        |
        -----''',
        
        2: ''' 
        ________
        |      |
        |      O
        |      |
        |
        |
        -----''',
        3:''' 
        ________
        |      | 
        |      O
        |      |/
        |
        |
        -----''',
        4:''' 
        ________
        |      | 
        |      O
        |     \|/
        |
        |
        -----''',
        5:''' 
        ________
        |      | 
        |      O
        |     \|/
        |      |
        |
        -----''',
    6:''' 
        ________
        |      | 
        |      O
        |     \|/
        |      |
        |       \\
        -----''',
        7:''' 
        ________
        |      | 
        |      O
        |     \|/
        |      |
        |     / \\
        -----''',

    }

    def f_hangman(c, fails):
        while fails <= c:
            print(hangman[fails + 1])
            fails +=1
            break
        return fails

    
    print('Welcome to HangMan Game 🕺')

    domestic_pets = ['monkey','cat', 'dog', 'fish', 'bird', 'snake', 'guniea pig', 'duck', 'goat', 'sheep', 'cattle', 'chicken', 'horse', 'goose', 'ferret','goldfish', 'rabbit', 'mouse',]
    colors = ['brown', 'orange', 'yellow','pink', 'blue', 'white', 'grey', 'black', 'purple', 'red', 'green']
    movies = ['Army of the Dead', 'Mortal Kombat', 'Infinite','Black Widow','The Suicide Squad', 'Shang-Chi and the Legend of the Ten Rings', 'No Time to Die', 'Venom2', 'Dune', 'Eternals', 'Spider Man No Way Home',"The King's Man"]
    african_countries = 'Nigeria,Ethiopia,Egypt,Tanzania,South Africa,Kenya,Uganda,Algeria,Sudan,Morocco,Angola,Mozambique,Ghana,Madagascar,Cameroon,ivory coast,Niger,Burkina Faso,Mali,Malawi,Zambia,Senegal,Chad,Somalia,Zimbabwe,Guinea,Rwanda,Benin,	Tunisia,Togo,Libya,Liberia,Seychelles,Botswana,Namibia,Gambia'.split(',')

    chosen_pet = random.choice(domestic_pets)
    chosen_color = random.choice(colors)
    chosen_movie = random.choice(movies).lower()
    chosen_country= random.choice(african_countries).lower()

    modes = ['easy', 'medium','hard']

    answer = input('Choose a mode: Easy, Medium, Hard> ').lower()

    while answer not in modes:
        answer = input('Wrong choice! Choose a mode: Easy, Medium, Hard> ').lower()

    if answer == 'easy':
        chosen = chosen_color
    elif answer == 'medium':
        chosen = chosen_pet
    else:
        options = [chosen_country,chosen_movie]
        chosen = random.choice(options)

    print('Guess the Word 🤔🤔')
    print('\n')
    if chosen in domestic_pets:
        print('💡💡Hint: Domestic Animal')
    elif chosen in colors:
        print('💡💡Hint: Name of a Color')
    else:
        print('HARD MODE 💪💪')
        if chosen == chosen_movie:
            print('💡💡Hint: Movie; A 2021 Action Blockbuster')
        else:
            print('💡💡Hint: African Country')
    # print(chosen)
    print(hangman[0])

    spaces = '_' * len(chosen)
    tries = 0

    if ' ' in chosen:
        dash = chosen.index(' ')
        spaces = spaces[:dash] + ' ' + spaces[dash+1:]
    print(spaces)

    count = 0
    while count >= 0:
        if tries == 7:
            print('\n')
            print(f'The correct word is {chosen.title()}')
            print('Game over❗❗ 😵😵, You are 💀')
            print('\n')
            restart = input('Play again? Y/N: ').upper()
            if restart == 'Y':
                print('\n')
                hang()
            else:
                print('Goodbye 👋👋')
                break
        print('\n')
        test = input('Enter a letter : ').lower()
        if test in chosen and test != '':
            for char in range(len(chosen)):
                if spaces[char] == test:
                    print('Letter already there')
                if chosen[char] == test:
                    spaces = spaces[:char] + test + spaces[char+1:]
                    
                elif chosen[char] == ' ':
                    spaces = spaces[:char] + ' ' + spaces[char+1:]

            print(spaces)
                    
        else:
            print(spaces)
            tries = f_hangman(count, tries)
            print(f' {test} is not in the word, ❗❗')
            
        count +=1
        if '_' not in spaces:
            print('Congratulations you guessed right 🎉🎉🎆🎆')
            break
        
hang()