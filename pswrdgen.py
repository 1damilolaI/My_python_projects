#################################################################
'''Password generator'''
#################################################################

import random
pass_length = int(input('How many letters would you like in your password?: '))
sy_length = int(input('How many symbols would you like in your password?: '))
num_length = int(input('How many numbers would you like in your password?: '))

letters = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')
numbers = '1,2,3,4,5,6,7,8,9,0'.split(',')
symbols = '!,.,£,$,%,^,&,*,@,#,?,/,|,_'.split(',')
password = ''

for char in range(num_length):
    password += numbers[random.randint(0,len(numbers)-1)]
for char in range(sy_length):
    password += symbols[random.randint(0,len(symbols)-1)]
for char in range(pass_length - len(password)):
    password += letters[random.randint(0,len(letters)-1)]
new_pass = set(password)
print(f" Your new password is {''.join(new_pass)}")