import mysql.connector
a=mysql.connector.connect(host='localhost', user= 'root',passwd='****',database='game_shop')
m=a.cursor()


def admin():


        user = input("Username ") 
        
        while True:
            if user =='Admin':
                password = input('Password  ')
                if password =='udsa':


                


                    def addgame():
                        sno=int(input("Enter serial Number "))
                        name=input('Enter Name of the Game ')
                        price=int(input('Enter the Price of Game '))
                        rating=int(input('Enter the rating of Game '))
                        gen=input('Enter Genres ')
                        dev=input('Enter the name of the Developer ')
                        fea=input('Enter the Features ')
                        mysql="INSERT INTO addgame values ("+ str(sno)+",'"+name+"',"+ str(price)+","+ str(rating)+",'"+gen+"','"+dev+"','"+fea+"')"
                        m.execute(mysql)
                        print()
                        print('Game Added Successfully!!')
                        a.commit()

                    




                    def removegame():


                        
                        sn=int(input('Enter serial number of game to be deleted '))

                        sql='delete from addgame where sno=' + str(sn) + ';'
                        m.execute(sql)
                        a.commit()
                    

                    print ('Succesfull')

                    

                    print('''****MENU****
                    1. Add a Game
                    2. Remove a Game
                   
                    ''')
                    print("-----------------------------------------------------------------")
                    print("####################### GAMES ###################################")
                    print("-----------------------------------------------------------------")
                    sql='select * from addgame;'
                    m.execute(sql)               
                    for x in m:
                        print(x)
                    
                    
                    
                    
                    


                    ch=int(input("Enter your Choice '1' OR '2' "))

                    while True:

                        if ch==1:

                            c=input(" To add more Press ' Y OR N' ")
                            

                            if c=='y' or 'Y':
                                addgame()
                            elif c=='n'or 'N':
                                break    
                            else:
                                break


                        elif  ch==2:

                            c=input(" To remove more Press ' y ' ")
                            if c=='y' or 'Y':
                                removegame()
                                print('Game removed successfully')
                            elif c=='n'or 'N':
                                break    
                            else:
                                break
                        
                        else:
                            print("wrong input")
                            break
                        






                else:
                    print("Wrong password")
                    break

            else: 
                print("Invalid user")
                break

        
admin()
