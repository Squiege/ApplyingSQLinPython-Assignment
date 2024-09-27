# Part 2, Task 1

from main import connect_database
from mysql.connector import Error

# Setting the ages we want to search
start_age = '24'
end_age = '30'

def get_members_in_age_range(start_age, end_age):
    # Connecting to database
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            # Setting up the tuple for the execute function
            selected_session = (start_age, end_age)

            # Query getting the members between the ages we set
            query = """
            SELECT * FROM members
            WHERE age BETWEEN %s AND %s;
            """

            # Executing the query
            cursor.execute(query, selected_session)
            print("Here are the members between the ages you entered: ")

            # Printing the results we get from the query
            for select in cursor.fetchall():
                print(select)

        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

get_members_in_age_range(start_age, end_age)