#Author:Win_Li   23147
#Date:2018-01-08 14:34

with open('用户密码.txt','r+') as user:
    user.write('win:123\n'
               'lemon:124')

def login():
    user = open('用户密码.txt','r')
    print(user.readlines())

login()

def home():
    print('welcome to home page!')

def finance():
    print('welcome to finance!')

def book():
    print('welcome to book!')
