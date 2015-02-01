from sys import argv
from random import choice

def pwgen(strength):
    low = ['1234567890qwertyuiopasdfghjklzxcvbnm','9']
    medium = [low[0]+'!@£$%^&*()_+QWERTYUIOP{}ASDFGHJKL:|~ZXCVBNM<>?','9']
    high = [medium[0],'17']
    count = '0'
    password = ''
    
    if argv[1] == 'low':
        while count < low[1]:
            password += choice(low)
            count + 1
