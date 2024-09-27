# Task 4

from main import connect_database
from mysql.connector import Error

# Asking user for the member id and session id
member_id = input("What is the member id of the member: ")
session_id = input("What is the session id of the workout: ")

def delete_workout_session(member_id, session_id):
    # Connecting to database
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            # Setting up tuple for execution
            selected_session = (member_id, session_id)

            # Query that will delete the workout session if the member id and session id match
            query = "DELETE FROM WorkoutSessions WHERE members_id = %s AND session_id = %s"

            # Executes query with the placeholders
            cursor.execute(query, selected_session)
            conn.commit()
            # Tells user the workout session has been deleted if it exists
            print("Workout session has been deleted in the database!")

        # Error Handling
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

delete_workout_session(member_id, session_id)