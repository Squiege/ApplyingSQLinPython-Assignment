# Task 4

from main import connect_database
from mysql.connector import Error

member_id = 2
session_id = 2

def delete_workout_session(member_id, session_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            selected_session = (member_id, session_id)

            query = "DELETE FROM WorkoutSessions WHERE members_id = %s AND session_id = %s"

            cursor.execute(query, selected_session)
            conn.commit()
            print("Workout session has been deleted in the database!")

        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

delete_workout_session(member_id, session_id)