'''this is the p0 redux translating scala=>python'''

import mysql.connector
import time

def get_database() -> mysql.connector:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password='venusawake',
        database='moviesTest',
        autocommit=True
    )
    return db


def add_movie():
    database = get_database()
    print("Enter a movie title: ")
    title = input()
    cursor = database.cursor()
    insert_statement = "INSERT INTO movies (title) values %s"
    cursor.execute("INSERT INTO movies (title,release_year,run_time,director1,director2,genre,lang,rating,genre2)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (title, 2, 24, 'hi','bye','sky','die','lie', 'try'))
    database.close()

'''Gets user input and calls delete_from_database, passing chosen movie title'''
def delete_movie():
    movie = get_title()
    delete_from_db()

def delete_from_db():
    #movie = get_title()
    #cursor = database.cursor()
    #cursor.execute("DELETE FROM movies WHERE title = %s", movie)

    print("Movie Deleted!")
    time.sleep(2)

def update_movie(database):
    print("update_database")

def stats_page(database):
    print("stats_page")

def print_menu():
    print("\n\nScroll up to view contents or Choose an option below:\n")
    print("A: Add Movie\nD: Delete Movie\nS: Stat Options\nX: Quit\n")

def main_menu_choice(action):
    if action == "A" or action == "a":
        add_movie()
    elif action == 'D' or action == 'd':
        delete_movie()
    elif action == "U" or action == "u":
        update_movie()
    elif action == "S" or action == "s":
        stats_page()

def get_title() -> str:
    print("Which movie would you like to delete?: ")
    movie = input()
    return movie


mydb = get_database()

mycursor = mydb.cursor()

selectQuery = '''SELECT * FROM movies'''
mycursor.execute(selectQuery)
result = mycursor.fetchall()

for x in result:
    print(x)


choice = None
print_menu()
choice = input()

while choice != "x" and choice != "X":

    main_menu_choice(choice)
    choice=input()
    mycursor = mydb.cursor()
    mycursor.execute('''SELECT * from movies''')
    result = mycursor.fetchall()
    for x in result:
        print(x)
    print_menu()




