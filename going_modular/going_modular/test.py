import mysql.connector

# GLOBAL VARIABLES DECLARATION
myConnnection = ""
cursor = ""
userName = ""
password = ""
roomrent = 0
restaurantbill = 0
gamingbill = 0
fashionbill = 0
totalAmount = 0
cid = ""


# MODULE TO CHECK MYSQL CONNECTIVITY
def MYSQLconnectionCheck():
    global myConnection
    global userName
    global password
    userName = input("\nENTER MYSQL SERVER'S USERNAME : ")
    password = input("\nENTER MYSQL SERVER'S PASSWORD : ")

    myConnection = mysql.connector.connect(host="localhost", user=userName, passwd=password, database='HOTEL',
                                           auth_plugin='mysql_native_password')
    if myConnection:
        print("\nCONGRATULATIONS! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED!")
        cursor = myConnection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS HOTEL")
        myConnection.commit()
        cursor.close()
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION. CHECK USERNAME AND PASSWORD!")


# MODULE TO ESTABLISH MYSQL CONNECTION
def MYSQLconnection():
    global userName
    global password
    global myConnection
    global cid

    my_connection = mysql.connector.connect(host='localhost', user=userName, passwd=password, database='HOTEL',
                                            auth_plugin='mysql_native_password')
    if my_connection:
        return my_connection
    else:
        print('\nERROR ESTABLISHING MYSQL CONNECTION !')
        my_connection.close()


# MODULE TO ENTER CUSTOMER DATA
def userEntry():
    global cid
    if myConnection:
        cursor = myConnection.cursor()
        createTable = 'CREATE TABLE IF NOT EXISTS userentry(CID VARCHAR(20), C_NAME VARCHAR(30),C_ADDRESS VARCHAR(30),C_AGE VARCHAR(30),C_COUNTRY VARCHAR(30) ,P_NO VARCHAR(30),C_EMAIL VARCHAR(30))'
        cursor.execute(createTable)
        cid = input("Enter Customer Identication Number : ")
        name = input("Enter Customer Name : ")
        address = input("Enter Customer Address : ")
        age = input("Enter Customer Age : ")
        nationality = input("Enter Customer Country : ")
        phoneno = input("Enter Customer Contact Number : ")
        email = input("Enter Customer Email : ")
        sql = "INSERT INTO userentry  VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values = (cid, name, address, age, nationality, phoneno, email)
        cursor.execute(sql, values)
        myConnection.commit()
        print("\nNew Customer Entered In The System Successfully !")
        cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")


# MODULE FOR BOOKING RECORD
def bookingRecord():
    global cid
    customer = searchCustomer()
    if customer:
        if myConnection:
            cursor = myConnection.cursor()

            # Corrected the CREATE TABLE query to define the data types for CHECKIN_DATE and CHECKOUT_DATE
            createTable = '''CREATE TABLE IF NOT EXISTS bookingrecord (CID VARCHAR(20), CHECKIN_DATE DATE, CHECKOUT_DATE DATE)'''
            cursor.execute(createTable)

            checkin = input("\nEnter Customer CheckIN Date [YYYY-MM-DD]: ")
            checkout = input("\nEnter Customer CheckOUT Date [YYYY-MM-DD]: ")

            # Insert statement corrected to match the number of columns in the table
            sql = "INSERT INTO bookingrecord (CID, CHECKIN_DATE, CHECKOUT_DATE) VALUES (%s, %s, %s)"
            values = (cid, checkin, checkout)

            cursor.execute(sql, values)
            myConnection.commit()

            print("\nCHECK-IN AND CHECK-OUT ENTRY MADE SUCCESSFULLY!")
            cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION!")


# MODULE FOR ROOMS
def roomRent():
    global cid
    global roomrent
    customer = searchCustomer()
    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            createTable = '''CREATE TABLE IF NOT EXISTS roomrent (CID VARCHAR(20),ROOM_CHOICE INT,NO_OF_DAYS INT,ROOMNO INT,ROOMRENT INT )'''
            cursor.execute(createTable)
            print("\n##### We have The Following Rooms For You #####")
            print("1. Ultra Royal -----> 10000 Rs.")
            print("2. Royal -----> 6000 Rs.")
            print("3. Elite -----> 4500 Rs.")
            print("4. Budget -----> 3500 Rs.")

            roomchoice = int(input("Enter Your Option: "))
            roomno = int(input("Enter Customer Room No: "))
            noofdays = int(input("Enter No. Of Days: "))

            if roomchoice == 1:
                roomrent = noofdays * 10000
                print("\nUltra Royal Room Rent:", roomrent)
            elif roomchoice == 2:
                roomrent = noofdays * 6000
                print("\nRoyal Room Rent:", roomrent)
            elif roomchoice == 3:
                roomrent = noofdays * 4500
                print("\nElite Room Rent:", roomrent)
            elif roomchoice == 4:
                roomrent = noofdays * 3500
                print("\nBudget Room Rent:", roomrent)
            else:
                print("Sorry, Maybe You Are Giving Me Wrong Input. Please Try Again!")
                return

            sql = "INSERT INTO roomrent VALUES (%s, %s, %s, %s, %s)"
            values = (cid, roomchoice, noofdays, roomno, roomrent)
            cursor.execute(sql, values)
            myConnection.commit()
            print("\nThank You,Your Room Has Been Booked For:", noofdays, "Days")
            print("\nYour Total Room Rent is:Rs.", roomrent)
            cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")


# MODULE FOR RESTAURANT
def Restaurant():
    global cid
    customer = searchCustomer()
    if customer:
        global restaurantbill

        if myConnection:
            cursor = myConnection.cursor()

            createTable = '''CREATE TABLE IF NOT EXISTS restaurant(CID VARCHAR(20),CUISINE VARCHAR(30),QUANTITY INT,BILL INT)'''
            cursor.execute(createTable)

            print("1. Indian Platter -----> 500 Rs.")
            print("2. Mexican Platter -----> 700 Rs.")
            print("3. Italian Platter -----> 800 Rs.")

            choice_dish = int(input("Enter Your Cuisine Choice(1-3): "))
            quantity = int(input("Enter Quantity: "))

            if choice_dish == 1:
                print("\nSO YOU HAVE ORDERED: Italian Platter")
                restaurantbill = quantity * 500
            elif choice_dish == 2:
                print("\nSO YOU HAVE ORDERED: Non-Vegetarian Combo")
                restaurantbill = quantity * 700
            elif choice_dish == 3:
                print("\nSO YOU HAVE ORDERED: Vegetarian & Non-Vegetarian Combo")
                restaurantbill = quantity * 800
            else:
                print("\nSorry, Maybe You Are Giving Me Wrong Input. Please Try Again!")
                return
            sql = "INSERT INTO restaurant VALUES (%s, %s, %s, %s)"
            values = (cid, choice_dish, quantity, restaurantbill)
            cursor.execute(sql, values)
            myConnection.commit()
            print("\nYour Total Bill Amount Is: Rs.", restaurantbill)
            print("\nWE HOPE YOU WILL ENJOY YOUR MEAL")
            cursor.close()  # Ensure the cursor is closed
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION!")


# MODULE FOR GAMING
def gaming():
    global cid
    customer = searchCustomer()
    if customer:
        global gamingbill
        if myConnection:
            cursor = myConnection.cursor()
            # Corrected the CREATE TABLE query with a closing parenthesis
            create_table_query = """CREATE TABLE IF NOT EXISTS gaming (CID VARCHAR(20), GAMES VARCHAR(30), HOURS INT, GAMING_BILL INT)"""
            cursor.execute(create_table_query)
            print("\n We Have Following Gaming Options For You:")
            print("1. Table Tennis -----> 150 Rs.")
            print("2. Bowling -----> 100 Rs.")
            print("3. Snooker -----> 250 Rs.")
            print("4. VR World Gaming -----> 400 Rs.")
            print("5. Video Games -----> 300 Rs.")
            print("6. Swimming Pool Games -----> 350 Rs.")

            game = int(input("Enter The Game You Want To Play (1-6): "))
            hour = int(input("Enter No Of Hours You Want To Play: "))

            # Create a dictionary to map game choices to their names and prices
            game_options = {
                1: ("Table Tennis", 150),
                2: ("Bowling", 100),
                3: ("Snooker", 250),
                4: ("VR World Gaming", 400),
                5: ("Video Games", 300),
                6: ("Swimming Pool Games", 350)
            }

            if game in game_options:
                game_name, price_per_hour = game_options[game]
                gamingbill = hour * price_per_hour
            else:
                print("Invalid game selection. Please try again!")
                return

            # Now we can safely print the selection and bill
            print("\nYou Have Selected To Play ", game_name, "For", hour, "Hours.")
            print("\nYour Total Gaming Bill Is Rs.", gamingbill)

            # Insert into the database
            sql = "INSERT INTO gaming (CID, GAMES, HOURS, GAMING_BILL) VALUES (%s, %s, %s, %s)"
            values = (cid, game_name, hour, gamingbill)

            cursor.execute(sql, values)
            myConnection.commit()

            print('\nYour Total Gaming Bill Is Rs.', gamingbill)

            cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION!")


# MODULE FOR BILLING
def totalAmount():
    global cid
    customer = searchCustomer()
    if customer:
        global grandTotal
        global roomrent
        global restaurantbill
        global gamingbill
        if myConnection:
            cursor = myConnection.cursor()

            # Create table structure if it doesn't exist
            '''
            createTable = CREATE TABLE IF NOT EXISTS whole(
                CID VARCHAR(100), 
                C_NAME VARCHAR(30), 
                ROOMRENTBILL INT,  
                RESTAURANTBILL INT, 
                GAMINGBILL INT, 
                TOTALAMOUNT INT)'''
            cursor.execute(createTable)

            # Ask for customer name
            name = input("Enter Customer Name: ")

            # Calculate grand total
            grandTotal = roomrent + restaurantbill + gamingbill

            # Prepare values for insertion
            values = (cid, name, roomrentbill, restaurantbill, gamingbill, grandTotal)

            # SQL insert statement
            sql = "INSERT INTO whole (CID, C_NAME, ROOMRENTBILL, RESTAURANTBILL, GAMINGBILL, TOTALAMOUNT) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, values)

            # Commit the transaction
            myConnection.commit()

            cursor.close()

            # Print billing details
            print("\n_________________________________________________________________")
            print("\n **** HOTEL CRISTAL DE LUNA **** CUSTOMER BILLING ****")
            print("\n_________________________________________________________________")
            print("\n CUSTOMER NAME:", name)
            print("\n ROOM RENT: Rs.", roomrent)
            print("\n RESTAURANT BILL: Rs.", restaurantbill)
            print("\n GAMING BILL: Rs.", gamingbill)
            print("\n_________________________________________________________________")
            print("\n TOTAL AMOUNT: Rs.", grandTotal)
            print("\n_________________________________________________________________")
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION!")


# MODULE FOR SEARCHING CUSTOMER
def searchCustomer():
    global cid
    if myConnection:
        cursor = myConnection.cursor()
        cid = input('ENTER CUSTOMER ID : ')
        sql = 'SELECT * FROM userentry WHERE CID= %s'
        cursor.execute(sql, (cid,))
        data = cursor.fetchall()
        if data:
            print(data)
            return True
        else:
            print('Record Not Found Try Again !')
            cursor.close()
            return False
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")


print('''\n**********WELCOME TO HOTEL CRISTAL DE LUNA**********
********MANAGED BY VEDIC ARYA & ANANYA SINGH********''')

myConnection = MYSQLconnectionCheck()
if myConnection:
    MYSQLconnection()
    while True:
        print('''1. Enter Customer Details\n
                  2. Display Customer Details\n
                  3. Calculate Room Rent\n
                  4. Calculate Restaurant Bill\n
                  5. Calculate Gaming Bill\n
                  6. Booking Record\n
                  7. Generate TOTAL BILL\n
                  8. EXIT''')
        choice = int(input('Enter Your Choice: '))
        if choice == 1:
            userEntry()
        elif choice == 2:
            searchCustomer()
        elif choice == 3:
            roomRent()
        elif choice == 4:
            Restaurant()
        elif choice == 5:
            gaming()
        elif choice == 6:
            bookingRecord()
        elif choice == 7:
            totalAmount()
        elif choice == 8:
            break
        else:
            print("Sorry, May Be You Are Giving Me Wrong Input. Please Try Again !!!")
else:
    print("\nERROR ESTABLISHING MYSQL CONNECTION!")



