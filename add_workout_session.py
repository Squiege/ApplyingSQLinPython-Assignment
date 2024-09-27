# Task 2
# The database is set up so that the sessions will auto increment whenever a new session is added
from main import connect_database
from mysql.connector import Error

id = 2
session_date = "2024-10-06"
session_time = "0600"
activity = "Lifting"

def add_workout_session(id, session_date, session_time, activity):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()


            query = "INSERT INTO WorkoutSessions (members_id, session_date, session_time, activity) VALUES (%s, %s, %s, %s)"

            cursor.execute(query, (id, session_date, session_time, activity))
            conn.commit()
            print("New session has been added to the database!")

        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

add_workout_session(id, session_date, session_time, activity)