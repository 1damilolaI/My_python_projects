def ceaser_cypher():
    def cypher(alpha, val):
        '''This function creates encrypted alphabets based on shift value. Returns a list'''
        encryption_alpha = []
        count = val
        for i in range(len(alpha)):
            encryption_alpha.append(alpha[count])
            count +=1
            if count == 26:
                count = 0
            
        return (encryption_alpha)

    def d_cypher(e_alpha, val):
        '''This function takes encrypted alphabets and decrypts it based on shift value'''
        decryption_alpha = []
        '''Returns count to rightful place'''
        count = 26-val
        for i in range(len(e_alpha)):
            decryption_alpha.append(e_alpha[count])
            count +=1
            if count == 26:
                count = 0
            
        return (decryption_alpha)



    def encryption(alpha, text, p,encrypt,num):
        '''This function encrypts a string'''
        encryption = ''
        for i in range(len(text)):
            '''if the letter in the text is a space or punctuation, replace it in the string at thesame position'''
            if text[i] == ' ':
                encryption = encryption[: i] + ' ' +encryption[i +1 : ]
            elif text[i] in p:
                encryption = encryption[: i] + text[i] +encryption[i +1 : ]
            elif text[i] in num:
                encryption = encryption[: i] + text[i] +encryption[i +1 : ]

            else:
                '''Get the index value of the letter in the alphabets and use the position to get the equivalent letter in encrypted alphabets'''
                index_i = alpha.index(text[i])
                
                encryption += encrypt[index_i]
        print(f'Your encrypted message = {encryption} 🤫')



    def decryption(e_alpha,text,p,decrypt,num):
        '''This function returns a decrypted string'''
        decryption = ''
        for i in range(len(text)):
            '''if the letter in the text is a space or punctuation, replace it in the string at thesame position'''
            if text[i] == ' ':
                decryption = decryption[: i] + ' ' + decryption[i +1 : ]
            elif text[i] in p:
                decryption = decryption[: i] + text[i] + decryption[i +1 : ]
            elif text[i] in num:
                decryption = decryption[: i] + text[i] +decryption[i +1 : ] 
            else:
                '''Get the index value of the letter in the encrypted alphabets and use the position to get the equivalent letter in decrypted alphabets'''
                index_i = e_alpha.index(text[i])
                decryption += decrypt[(index_i)]
        print(f'Your decrypted message = {decryption} 🧐')


    alphabets = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')
    punct = "./,/?/!/;/:/'/ \"/".split('/')
    numbers = '1,2,3,4,5,6,7,8,9,0'.split(',')

    print('''Welcome 🤠🤠! 
    - Encode or Decode any text you want.
    - No limit to characters
    - Please note than numbers would not be encripted ''')
    print('\n')

    text_message = input('Enter your text here: ').lower()
    task = int(input('Would you like to 1: Encode, 2: Decode: '))
    choices = [1,2]

    while task not in choices:
        task = int(input('Please choose correctly 1: Encode, 2: Decode: '))
        

    shift = int(input('Enter a shift Number: '))
    encripted = cypher(alphabets,shift)
    decripted = d_cypher(encripted,shift)

    if task == 1:
        encryption(alphabets,text_message, punct, encripted, numbers)
    else:
        decryption(encripted, text_message, punct, decripted,numbers)

    choices = ['Y', 'N']
    decision = input('Would you like to perform another task? Y/N: ').upper()
    while decision not in choices:
        decision = input('Please give a correct answer Y/N: ').upper()
    if decision == 'Y':
        ceaser_cypher()
    else:
        print('Have a nice day 😁')
ceaser_cypher()
