# Task 3

from main import connect_database
from mysql.connector import Error

# Asking the user what's the age and who the member is
age = input("What is the age that you want to update: ")
id = input("What is the id of the member you would like to update: ")

def update_member(age, id):
    # Connecting to database
    conn = connect_database()
    if conn is not None:
        try:
            # Setting up tuple for execution
            updated_member = (age, id)

            cursor = conn.cursor()

            # Query that will update the age if the id matches
            query = "UPDATE Members SET age = %s WHERE id = %s"

            # Executes the query with our placeholders
            cursor.execute(query, updated_member)
            conn.commit()
            # Prints that the database is updated if the member is in our system
            print("Member has been updated in the database!")
        # Error Handling
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

update_member(age, id)