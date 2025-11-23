from db.load_csv import load_csv
from db.queries import *




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

cnx = connection.get_connection()
cursor = cnx.cursor()

while True:
    choice = print_menu()
    match choice:
        case "1":
            load_csv()
        case "2":
            keyword = input("Enter the institution name: ")
            search_by_institution( ,keyword)
        case "3":

        case "4":

        case "5":

        case "6":

        case "7":

        case "8":
            break
        case _ :
            break






