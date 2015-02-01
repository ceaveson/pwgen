from sys import argv
from random import choice


low = ['1234567890qwertyuiopasdfghjklzxcvbnm',9]
medium = [low[0]+'QWERTYUIOPASDFGHJKLZXCVBNM!@=$%^&*()_',9]
high = [medium[0],17]
password = ''
    
if argv[1] == 'low' or argv[1] == 'l':
    while password.count('') < low[1]:
        password += choice(low[0])
    print password
elif argv[1] == 'medium' or argv[1] == 'm':
    while password.count('') < medium[1]:
        password += choice(medium[0])
    print password
elif argv[1] == 'high' or argv[1] == 'h':
    while password.count('') < high[1]:
        password += choice(high[0])
    print password
else:
    print "please type either 'low', 'medium', 'high' after the initial command"

    print password