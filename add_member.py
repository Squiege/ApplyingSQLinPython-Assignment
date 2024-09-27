# Task 1
# Database is set up so that when a new member is added to the database it will auto increment
from main import connect_database
from mysql.connector import Error

# Asks user for the information they would like to add to the database
first_name = input("What is the first name of the member you would like to add? ")
last_name = input("What is the last name of the member you would like to add? ")
age = input("What is the age of the member you would like to add? ")

def add_member(first_name, last_name, age):
    # Connects to the database
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            # Setting up tuple for the execution
            new_member = (first_name, last_name, age)

            # Query that will add the inputted values above into the database
            query = "INSERT INTO Members (first_name, last_name, age) VALUES (%s, %s, %s)"

            # Executes query with the data from user
            cursor.execute(query, new_member)
            conn.commit()
            # Tells the user that the data has been submitted
            print("New member has been added to the database!")

        # Error Handling
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

add_member(first_name, last_name, age)