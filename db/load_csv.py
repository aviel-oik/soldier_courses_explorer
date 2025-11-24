import db.connection
import csv
# import data

def load_csv():
    row_loaded = 0

    cnx = db.connection.get_connection()
    cursor = cnx.cursor()

    with open('C:\\Users\\COMPUTER\\Desktop\\soldier_courses_explorer\\data\\courses.csv', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
            cursor.execute("INSERT INTO courses(institution, city, address, course, district, telephone, email) VALUES (%s, %s, %s, %s, %s, %s, %s);", row)
            row_loaded += 1

    cnx.commit()
    print(f"{row_loaded} rows inserted.")

load_csv()