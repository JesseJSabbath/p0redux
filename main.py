'''this is the p0 redux translating scala=>python'''

import mysql.connector
import re

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
    title = input("Enter a movie title: ")
    release_year = input("Enter the movie's release year: ")
    run_time = input("Enter the movie's run time in minutes: ")
    director1 = input("Enter the director's first name: ")
    director2 = input("Enter the director's last name: ")
    genre = input("Enter the movie's genre: ")
    lang = input("Enter the movies language: ")
    rating = input("Enter the movies rating: ")
    genre2 = input("Enter a 2nd genre or Press Enter: ")

    if genre2 == '':
        genre2 = None

    cursor = database.cursor()
    cursor.execute("INSERT INTO movies (title,release_year,run_time,director1,director2,genre,lang,rating,genre2)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (title, release_year, run_time, director1, director2, genre, lang, rating, genre2))
    database.close()


def delete_from_db():
    database = get_database()
    cursor = database.cursor()

    movie = input("Enter the title of the movie you'd like to delete: ")
    cursor.execute("DELETE FROM movies WHERE title LIKE binary %s", (movie,))
    database.close()

    print("Movie Deleted!")

def update_movie():
    print("update_database: to be implemented")

def stats_page():
    print("Stats Menu")
    print("1: Top Directors\n2: Top Years\n3: Top MPAA Ratings\n4: Top Genres\nM: Main Menu\n")
    new_choice = input()
    while new_choice != 'M' and new_choice != 'm':
        if re.match("^[1234mM]$", new_choice):
            get_stat(new_choice)
        else:
            print("Invalid Option. Choose again\n")
            print("1: Top Directors\n2: Top Years\n3: Top MPAA Ratings\n4: Top Genres\nM: Main Menu\n")
        new_choice = input()

def get_stat(choice):
    print(choice)
    database = get_database()
    cursor = database.cursor()
    query = None
    if choice == "1":
        query = "SELECT count(*) as number, director1, director2 from movies group by director2 order by number desc limit 5";
    elif choice == "2":
        query = "SELECT count(*) as number, release_year from movies group by release_year order by number desc limit 5"
    elif choice == "3":
        query = "SELECT count(*) as number, rating from movies group by rating order by number desc limit 5"
    elif choice == "4":
        query = "SELECT count(*) as number, genre from movies group by genre order by number desc limit 5"
    cursor.execute(query)
    result = cursor.fetchall()
    for movie in result:
        print(movie)


def print_menu():
    print("\n\nScroll up to view contents or Choose an option below:\n")
    print("A: Add Movie\nD: Delete Movie\nS: Stat Options\nQ: Quit\n")

def main_menu_choice(action):
    if action == "A" or action == "a":
        add_movie()
    elif action == 'D' or action == 'd':
        delete_from_db()
    elif action == "U" or action == "u":
        update_movie()
    elif action == "S" or action == "s":
        stats_page()

def get_title() -> str:
    print("Which movie would you like to delete?: ")
    movie = input()
    return movie


database = get_database()
my_cursor = database.cursor()
selectQuery = '''SELECT * FROM movies'''
my_cursor.execute(selectQuery)
result = my_cursor.fetchall()

for x in result:
    print(x)


choice = None
print_menu()
choice = input()

while choice != "Q" and choice != "q":

    main_menu_choice(choice)
    my_cursor = database.cursor()
    my_cursor.execute('''SELECT * from movies''')
    result = my_cursor.fetchall()
    for x in result:
        print(x)
    print_menu()
    choice = input()




