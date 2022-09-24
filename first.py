import mysql.connector
from datetime import date

# To get the exact date
today = date.today()


# Base
db = mysql.connector.connect(user='user_name', password='password', host='Host_Name', database="Database_Name")
mycursor = db.cursor()
mycursor.execute("select * from entry")
fetch = mycursor.fetchall()


# To learn what user wants
print("Please tell if you want to \n 1)Fetch \n 2)Create \n 3)Delete \n 4)Dues \n 5)Updating dues")
val1 = int(input("please enter the value = "))

# To fetch data
if(val1 == 1): 
    print("Please enter the name = ")
    nam = str(input())
    # To fetch all data
    if(nam == "all"):
        mycursor.execute('select * from entry')
        for i in mycursor:
            print(i)
    # To fetch specific data
    else:
        mycursor.execute(f"select * from entry where name = '{nam}';")
        for i in mycursor:
            print(i)
# To create a new entry
elif(val1 == 2):
    print("Enter the name = ")
    name = input()
    first_lowercase = name[0].lower() + name[1:]
    print("Enter the class = ")
    grade = int(input())
    print("Enter the amount = ")
    amount = int(input())
    mycursor.execute(f"insert into entry values ('{first_lowercase}', {grade}, {amount}, '{today}');")
    db.commit()
# To delete a entry
elif(val1 == 3):
    print("Please enter the name = ")
    nam = str(input())
    mycursor.execute(f"delete from entry where name = '{nam}';")
    db.commit()
    mycursor.execute(f"select * from entry;")
    for i in mycursor:
        print(i)
# To fetch dues of a specific entry
elif(val1 == 4):
    print("Please enter the name = ")
    nam = str(input())
    mycursor.execute(f"select item_price from entry where name = '{nam}'")
    for i in mycursor:
        print(i)
# To change/update Dues
elif(val1 == 5):
    print("Please enter the name = ")
    nam = str(input())
    print("Please enter the amount = ")
    due = (input())
    # To check if a specific amount is needed to be changed or all the dues are being cleared.
    if(due == "clear"):
        due = "item_price"
        sign = str("-")
    # If there is a specific amount
    else:
        print("Is amount being? =\n 1)added \nor\n 2)removed")
        num = int(input())
        # To determine if the value needs to be added or removed.
        if(num == 1):
            sign = str("+")
        elif(num == 2):
            sign = str("-")
        # In case of invalid input from user 
        else:
            print("Invalid input entered")
    mycursor.execute(f"update entry set item_price = item_price{sign}{due} where name = '{nam}';")
    db.commit()
    mycursor.execute(f"select * from entry where name = '{nam}';")
    for i in mycursor:
        print(i)
# In case of invalid input from user 
else:
    print("Invalid input entered")



# To delete entries which have cleared their dues, run if required.
# mycursor.execute(f"delete from entry where item_price <= 0;")
# db.commit()
