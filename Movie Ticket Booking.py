import random
import mysql.connector as con
password=input("Enter SQL Password: ")
# MODULE TO LOGIN AS AN ADMIN
def adminlogin():
    mydb=con.connect(host="localhost",user="root",password=password,
                 database="program")
    mycursor=mydb.cursor()
    name=input("Enter Username: ")
    pas=input("Enter Password: ")
    mycursor.execute("SELECT * FROM ADMIN_LOGIN")
    for i in mycursor:
        if i[0]==name and i[1]==pas:
            print("---------WELCOME----------")
            admin_menu_display()
            break
    else:
        print("Invalid UserId or Password!")
# MODULE LOGIN AS AN USER
def userlogin():
    mydb=con.connect(host="localhost",user="root",password=password,
                             database="program",)
    mycursor=mydb.cursor()
    name=input("Enter UserName: ")
    pas=input("Enter Password:")
    mycursor.execute("SELECT * FROM USER_LOGIN")
    for i in mycursor:
        if i[0]==name and i[1]==pas:
            print("---------WELCOME----------")
            user_menu_display()
            break
    else:
        print("Invalid UserId or Password!")
# MODULE TO CREATE NEW USER ACCOUNT
def register():
    mydb=con.connect(host="localhost",user="root",password=password,
                 database="program")
    mycursor=mydb.cursor()
    name=input("Enter Username: ")
    pas=input("Enter password: ")
    if len(name)==0 or len(pas)==0:
        if len(name)==0 and len(pas)!=0:
            print("Username cannot be blank!")
        elif len(pas)==0 and len(name)!=0:
            print("Password cannot be blank!")
        elif len(name)==0 and len(pas)==0:
            print('Please Enter valid details!')
    elif len(name)!=0 or len(pas)!=0:
        mycursor.execute("SELECT * FROM USER_LOGIN")
        for i in mycursor:
            if i[0]==name:
                print("Username Already taken!")
                break
        else:    
            mycursor.execute(f"INSERT INTO USER_LOGIN VALUES('{name}','{pas}')")
            mydb.commit()
            print("Account created Succesfully!")
# MODULE USED BY ADMIN TO ADD DETAILS OF MOVIE AVAILABLE
def admin_add():
    mydb=con.connect(host="localhost",user="root",password=password,
                 database="program")
    mycursor=mydb.cursor()
    m_name=input("Enter Movie Name: ").upper()
    dt=input("Enter Date And Time Of The Show(DD/MM/YYY HH:MM:SS): ")
    price=(input("Enter Price:"))
    mycursor.execute("SELECT * FROM ADMIN_TABLE")
    for i in mycursor:
        if i[0]==m_name:
            print("Movie already added!")
            break
    else:
        mycursor.fetchall()
        mycursor.execute(f"INSERT INTO ADMIN_TABLE VALUES('{m_name}','{dt}','{price}')")
        mydb.commit()
        print("Details Added Succesfully")
# MODULE USED BY ADMIN TO REMOVE DETAILS OF THE MOVIE
def admin_remove():
    mydb=con.connect(host="localhost",user="root",password=password,
                 database="program")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM ADMIN_TABLE")
    print('Following Movies are available')
    for j in mycursor:
        print(j)
    name=input("Enter Name Of the movie to be deleted: ")
    mycursor.execute(f"DELETE FROM ADMIN_TABLE WHERE mname='{name}'")
    mydb.commit()
    print("Movie Removed Succesfully!")
# MODULE USED BY ADMIN TO SHOW THE DETAILS OF MOVIES AVAILABLE
def show_details():
    mydb=con.connect(host="localhost",user="root",password=password,
                 database="program")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT count(*) FROM ADMIN_TABLE")
    for i in mycursor:
        if i[0]==0:
            print('No Details Available!')
            break
        else:
            mycursor.execute("SELECT * FROM ADMIN_TABLE")
            for j in mycursor:
                print(j)
# MODULE USED BY ADMIN TO SHOW CUSTOMER DETAILS
def customer_details():
    mydb=con.connect(host="localhost",user="root",password=password,
                 database="program")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT count(*) FROM CUSTOMER")
    for i in mycursor:
        if i[0]==0:
            print('No Details Available!')
            break
        else:
            mycursor.execute("SELECT * FROM CUSTOMER")
            for j in mycursor:
                print(j)
# MODULE FOR CUSTOMER TO BOOK TICKET
def book_ticket():
    mydb=con.connect(host="localhost",user="root",password=password,
                 database="program")
    mycursor=mydb.cursor()
    mycursor.execute('SELECT count(*) FROM ADMIN_TABLE')
    for i in mycursor:
        if i[0]==0:
            print("No Movies are available at this time!")
            break
        else:
            mycursor.execute("SELECT * FROM ADMIN_TABLE")
            print("-------------List of Availabe movies---------------- ")
            for j in mycursor:
                print(f'Movie Name: {j[0]}')
                print(f'Date and time of show: {j[1]}')
                print(f'Price Per Person: Rs.{j[2]}')
                print('--------------------------------------------------')
            mname=input("Enter Movie Name: ").upper()
            ticketno=random.randrange(100000,999999)
            mobile=int(input("Enter Mobile Number: "))
            tickets=int(input("Enter Number Of Tickets to be booked: "))
            showdate=j[1]
            price=j[2]
            mycursor.execute("SELECT * FROM ADMIN_TABLE")
            for i in mycursor:
                if i[0]==mname:
                    print(f"Total price of your ticket will be Rs.{(i[2])*tickets}")
                    option=str(input("Do You Want to Comfirm? YES OR NO: ")).lower()
                    mycursor.fetchall()
                    if option=="yes":          
                        mycursor.execute(f"INSERT INTO CUSTOMER VALUES('{ticketno}','{mname}','{mobile}','{tickets}','{showdate}','{price}')")
                        mydb.commit()
                        print(f"Congratulation!You have successfully booked your Ticket")
                        print(f"Ticket Your Ticket Number is {ticketno}")
                        break
                    elif option=="no":
                        user_menu_display()       
            else:
                print("Please enter Correct Movie Name!")
# MODULE FOR CUSTOMER TO CANCEL TICKET
def cancel_ticket():
    mydb=con.connect(host="localhost",user="root",password=password,
                 database="program")
    mycursor=mydb.cursor()
    ticketno=input("Enter Your Ticket Number: ")
    mycursor.execute("SELECT * FROM CUSTOMER")
    for i in mycursor:
        if i[0]==ticketno:
            mycursor.fetchall()
            option=input("Are you Sure do you want to cancel this ticket? YES OR NO: ").lower()
            if option=="yes":
                mycursor.execute(f"DELETE FROM CUSTOMER WHERE TICKET_NO='{ticketno}'")
                mydb.commit()
                print('Your Ticket has been cancellled!')
                break
            elif option=="no":
                user_menu_display()
    else:
        print("Please Enter correct ticket number!")
# MODULE FOR CUSTOMER TO SEE HIS/HER TICKET DETAILS USING TICKET NO.
def ticket_details():
    mydb=con.connect(host="localhost",user="root",password=password,
                 database="program",)
    mycursor=mydb.cursor()
    ticketno=str(input("Enter Your Ticket Number: "))
    mycursor.execute("SELECT * FROM CUSTOMER")
    for i in mycursor:
        if i[0]==ticketno:
            print("----------TICKET DETAILS-----------")
            print(f"Ticket No: {i[0]}")
            print(f"Movie Name: {i[1]}")
            print(f"Mobile Number: {i[2]}")
            print(f"Number of Tickets Booked: {i[3]}")
            print(f"Date and Time of Show(DD/MM/YYY/HH:MM:SS): {i[4]}")
            print(f"Amount of ticket: {i[5]}")
            print("------------------------------------")
            break
    else:
        print('Enter Correct Ticket Number!')
# MODULE TO DISPLAY ADMIN MENU PAGE
def admin_menu_display():
    while True:
        print("1. Add Details")
        print("2. Show Movie Details")
        print("3. Show Customer Details")
        print("4. Remove Details")
        print("5. LogOut")
        option=int(input("Choose The Desired option: "))
        if option==1:
            admin_add()
        elif option==2:
            show_details()
        elif option==3:
            customer_details()
        elif option==4:
            admin_remove()
        elif option==5:
            break
        else:
            print("Incorrect choice! Please choose the correct option")
# MODULE TO DISPLAY USER MENU PAGE
def user_menu_display():
    while True:
        print("1. Book Ticket")
        print('2. Cancel Ticket')
        print("3. Show Ticket details")
        print("4. LogOut")
        option=int(input("Choose the desired option:"))
        if option==1:
            book_ticket()
        elif option==2:
            cancel_ticket()
        elif option==3:
            ticket_details()
        elif option==4:
            break
        else:
            print("Choose the correct option!")
# HOMEPAGE MODULE
while True:
    print("1. Admin Login")
    print("2. User Login")
    print("3. Sign Up")
    print("4. Exit")
    option=int(input("Select the desired option: "))
    if option==1:
        adminlogin()
    elif option==2:
        userlogin()
    elif option==3:
        register()
    elif option==4:
        break
    else:
        print("Incorrect Choice! Please enter Correct Option ")
