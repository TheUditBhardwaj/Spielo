import mysql.connector
a=mysql.connector.connect(host='localhost', user= 'root',passwd='1805',database='game_shop')
m=a.cursor()

import fontstyle as fs
F=fs.apply('                   WELCOME TO SPIELO                        ','bold / Italic/red/white_bg')
print(F)



def project():
    
    


    print('''       ****Main Menu****
    1. Admin
    2. Customer''')

    m=int(input('Enter Your Choice'))
    while True:
        if m==1:
            p=fs.apply('                   WELCOME TO ADMINISTRATOR                       ','bold / Italic/red/white_bg')
            print(p)
            
            import Admin
            break
        elif m == 2:
            import customer
        else:
            print('Wrong Input ')
            print('Exiting....')
            break

    
project()


