from db.load_csv import load_csv
from db.queries import *
from db.connection import *




def print_menu():
    return input("""    === MENU ===    
    1- Load CSV into DB
    2- Search records by institution name
    3- Search records by course name
    4- Find most common course
    5- Find least common course
    6- Show course count per district
    7- Free SQL query
    8- EXIT 
    Choose option:  """)

cnx = get_connection()
cursor = cnx.cursor()

while True:
    choice = print_menu()
    match choice:
        case "1":
            load_csv()
        case "2":
            keyword = input("Enter the institution name: ")
            print(search_by_institution(cnx ,keyword))
        case "3":
            keyword = input("Enter the course name: ")
            print(search_by_course(cnx, keyword))
        case "4":
            print(get_most_common_course(cnx))
        case "5":
            print(get_least_common_course(cnx))
        case "6":
            print(get_course_count_per_district(cnx))
        case "7":
            query = input("Enter the SQL query: ")
            print(run_free_query(cnx, query))
        case "8":
            break
        case _ :
            print("You need to enter a valid option, Bye !!!")
            continue






