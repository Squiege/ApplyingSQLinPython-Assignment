# Task 1
# Database is set up so that when a new member is added to the database it will auto increment
from main import connect_database
from mysql.connector import Error

first_name = input("What is the first name of the member you would like to add? ")
last_name = input("What is the last name of the member you would like to add? ")
age = input("What is the age of the member you would like to add? ")

def add_member(first_name, last_name, age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            new_member = (first_name, last_name, age)

            query = "INSERT INTO Members (first_name, last_name, age) VALUES (%s, %s, %s)"

            cursor.execute(query, new_member)
            conn.commit()
            print("New member has been added to the database!")

        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

add_member(first_name, last_name, age)