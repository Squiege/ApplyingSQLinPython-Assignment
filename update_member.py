# Task 3

from main import connect_database
from mysql.connector import Error

age = 40
id = 3

def update_member(age, id):
    conn = connect_database()
    if conn is not None:
        try:
            updated_member = (age, id)
            cursor = conn.cursor()


            query = "UPDATE Members SET age = %s WHERE id = %s"

            cursor.execute(query, updated_member)
            conn.commit()
            print("Member has been updated in the database!")

        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

update_member(age, id)