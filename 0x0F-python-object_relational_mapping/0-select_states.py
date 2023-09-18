#!/usr/bin/python3

"""states from a provided databse"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    results = cursor.fetchall()

    for record in results:
        print(record)

    cursor.close()
    db.close()
