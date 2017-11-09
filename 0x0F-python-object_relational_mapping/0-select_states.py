#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
				passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    db.close()
