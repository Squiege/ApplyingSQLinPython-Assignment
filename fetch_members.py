from main import connect_database

# Connects to database
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # Query that selects all members
        query = "SELECT * FROM Members"

        # Executes the query
        cursor.execute(query)

        # Prints all the rows in the database
        for row in cursor.fetchall():
            print(row)
    finally:
        cursor.close()
        conn.close()