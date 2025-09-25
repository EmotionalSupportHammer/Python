import mysql.connector
import tkinter 
try:
    school_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        port = '3306',
        database = "school_db",
        password = "DataFish2025!"
    )

    if school_db.is_connected():
        print("hi")
    else:
        print('not connected')
except mysql.connector.Error as err:
    print("somthing whent wrong: + {err}") 

x = ("Select * from student_favorit_videogames;")
little_helper = school_db.cursor()
little_helper.execute("SET SQL_SAFE_UPDATES = 0;" )
little_helper.execute(x)
R = little_helper.fetchall()
for row in R:
    print(row)
#defining tables
def add_shit():
    inputed_data = "insert into student_favorit_videogames(first_name,last_inital,fav_game,Developet_by,Time_of_delcration) values(%s,%s, %s,%s, now());" 

    name = input("What is your first name?")
    L_N = input("What is the first letter of your last name?")


    FAV_Game = input("What is your favorit game?")
    Dev= input("Who made that game?")
    little_helper.execute(inputed_data,(str(name ) ,str(L_N),str(FAV_Game ),(Dev)))
    school_db.commit()
    little_helper.execute(x)
    R = little_helper.fetchall()
def see_shit():
    little_helper.execute("Select * from student_favorit_videogames")
active = True 
while active == True:
    DO_What = input("What whould you like to do? A=add to table, S=See table").upper()
    match DO_What:
        case "A":
            add_shit()
        case "S":
            see_shit()

for row in R:
    print(row)