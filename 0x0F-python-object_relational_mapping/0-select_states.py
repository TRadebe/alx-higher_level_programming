import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database_name,
            port=3306
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to retrieve states sorted by states.id
        cursor.execute("SELECT * FROM states ORDER BY states.id")

        # Fetch all the results
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

        # Close the cursor and the database connection
        cursor.close()
        db.close()
