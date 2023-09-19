import mysql.connector
a=mysql.connector.connect(host='localhost', user= 'root',passwd='1805',database='game_shop')
m=a.cursor()

def customer():



    def searchname():
    
        
        game=input("Enter the Name of Game to Search - ")
        

    
        
        query=q="select * from addgame where name like '%{}%'".format(game)
        
        
        m.execute(query)
        data=m.fetchall()

        while True:
            if  data :
                for x in data:
                    print(x)
                break
            else:
                print("No Game Unavailable")
                break
        
        id=input("Enter Name ")
        email=input("Enter EmailID")
        age=input("Enter your Age ")
        gam=input("Enter the Name of Game you want to buy - ")

        mysql="INSERT INTO customer values ('"+id+"','"+email+"','"+age+"','"+gam+"')"
        m.execute(mysql)
        print("Purchased Successfully!!")
        a.commit()

    

    def searchfea():
        
            
        gen=input("Enter the Genres You Like - ")

        query=q="select * from addgame where Genres like '%{}%'".format(gen)
            
            
        m.execute(query)
        data=m.fetchall()

        while True:
            if  data :
                for x in data:
                    print(x)
                break
            else:
                print("No Game Unavailable")
                break

        id=input("Enter Name ")
        email=input("Enter EmailID")
        age=input("Enter your Age ")
        gam=input("Enter the Name of Game you want to buy - ")

        mysql="INSERT INTO customer values ('"+id+"','"+email+"','"+age+"','"+gam+"')"
        m.execute(mysql)
        print("Purchased Successfully!!")
        a.commit()

    def  rate():
        print('Rating from 1-5')
        rat=input("Enter Rating - ")
            

        
            
        query=q="select * from addgame where Rating like '%{}%'".format(rat)
            
            
        m.execute(query)
        data=m.fetchall()

        while True:
            if  data :
                for x in data:
                    print(x)
                break
            else:
                print("No Game Unavailable")
                break

        id=input("Enter Name ")
        email=input("Enter EmailID")
        age=input("Enter your age ")
        gam=input("Enter the name of Game you want to buy - ")

        mysql="INSERT INTO customer values ('"+id+"','"+email+"','"+age+"','"+gam+"')"
        m.execute(mysql)
        print("Purchased Successfully!!")
        
        a.commit()

    print('''   ****MENU***
    1. Search by Name
    2. Search by Genres
    3. Search by Rating 
    
    OR 

    PRESS ANY KEY TO EXIT  ''')

    while True:
        
        ch=input('Enter your choice - ')
        if ch == '1':
            searchname()
          
        elif ch=='2':
            searchfea()
            
        elif ch=='3':
            rate()
           
        
            
        else:
            print("Thank You , Have A Nice Day")

            break

customer()