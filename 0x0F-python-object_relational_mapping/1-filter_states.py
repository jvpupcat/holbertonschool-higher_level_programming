#!/usr/bin/python3
"""script that lists all states with name starting with N"""

if __name__ == "__main__":
    """lists all states with a name starting with N"""
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name\
                FROM states\
                WHERE name REGEXP '^N'\
                ORDER BY states.id ASC")
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    db.close()
